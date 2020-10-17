from django.shortcuts import render
from rest_framework.views import APIView as API
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Users
from .serializer import UserSerializer, UsersVoiceTrySerializer
from random import randrange
import requests
import json

from .voicerecognition import start

class UsersCRUD(API):
    permission_classes = ()
    def post(self, request):
        data    = request.data
        exist_emial = Users.objects.filter(email = data['email'])
        # Revisa si ya existe un usuario con ese email   
        if(exist_emial):
            return Response([
                False,
                {
                    "username":[
                        "Ya existe un usuario con ese email"
                    ],
                }
            ])
        user_serializer = UserSerializer( data = data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                "ok":True,
                "data":user_serializer.data
            })
            
        else:
            return Response({
                "ok":False,
                "data":user_serializer.errors
            })






class Login(API):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        # Login por email 
        try:
            user = Users.objects.get(email=username)
            if user.check_password(password):
                data = self.getToken(user)
                return Response(data)
        except:
            pass
        
        # Login por nombre de usuario
        user = authenticate(username=username, password=password)
        if user:
            data = self.getToken(user)
            return Response(data)
        else:
            return Response({"ok":False, "token":None, "id":None,  "username":None, "email":None})
    
    def getToken(self, user):
        # Si el usuario no tiene un token, asignarle uno 
        #if not(user.auth_token.key):
        #    Token.objects.create(user=user)
        worlds = ["mundo", "chimpance","banco", "robot", "automovil", "teclado","cuaderno","celular"]

        random_value = randrange(len(worlds)-1)

        return {"ok":True, "token": worlds[random_value], "id":user.id, "username":user.username, "email":user.email}


class VoiceRecognition(API):
    permission_classes = ()
    def post(self,request):
        data = request.data
        user_id = data['id']
        voice_try   = data['voice']
        
        user  = Users.objects.filter(id = user_id)
        user  = user[0]
        voice = user.voice
        voice_name = 'media/' + voice.name
        
        
        url = 'https://speaker-recognition.herokuapp.com/enrollVoice/1111'
        files = {
            "audio": open(voice_name, 'rb'),
            }
        values = {
            "name":"EnrollCustomer",
        }
        r = requests.post(url, files=files, data=values)
        
        data = {
            'user': user_id,
            'voice': voice_try
        }
        serializer = UsersVoiceTrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        #print(serializer.data)
        voice_name = serializer.data['voice']
        voice_name = voice_name[1:]

        url = 'https://speaker-recognition.herokuapp.com/verifyVoice/1111'
        files = {
            "audio": open(voice_name, 'rb'),
            }
        values = {
            "name":"VerifyCustomer",
        }
         
        r = requests.post(url, files=files, data=values)
        try:
            data = start(voice_name,voice_name[17:])
            data = data['results']['transcripts'][0]['transcript']
        except:
            data = False 
        
        
        response = {
            "voice": r.json(),
            "word":data
        }
        return Response(response)
    
    