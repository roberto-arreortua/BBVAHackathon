from django.db import models
from django.contrib.auth.models import  User, AbstractBaseUser,AbstractUser, BaseUserManager, User

class Users(AbstractUser):
    face_1 = models.FileField(upload_to="Faces",  default = None, null = True, blank = True)
    face_2 = models.FileField(upload_to="Faces",  default = None, null = True, blank = True)
    voice  = models.FileField(upload_to="Voices", default = None, null = True, blank = True)
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username


class UsersVoiceTry(models.Model):
    user        = models.ForeignKey(Users,on_delete=models.SET_NULL,verbose_name="Usuario", null = True, blank=True)
    voice       = models.FileField(upload_to="VoicesTry", default = None, null = True, blank = True)
    created_dt  = models.DateTimeField(auto_now=True, verbose_name="Fecha", editable=False)

    class Meta:
        verbose_name = 'Reconocimiento de voz'
        verbose_name_plural = 'Reconocimientos de voces'
    
    def __str__(self):
        return self.user