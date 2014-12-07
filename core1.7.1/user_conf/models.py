# -*- coding: utf-8 -*-
from django.db import models
#from settings.uploadmodel import FileFieldProcessor
from django.utils.translation import ugettext as _ 
from django.template.defaultfilters import slugify 
from django.conf import settings
import datetime , os
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import models
from django.contrib.auth.models import User, UserManager, Group
from django.db import models
from django.contrib.auth.backends import ModelBackend
#from places.models import *



class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


SEX_TYPES = (
    ("Erkek", u"Erkek"),
    (u"Kadın", u"Kadın"),
)

class Student(models.Model):
    
    """def defContentFileName( instance, filename):
        base, extension = os.path.splitext(os.path.basename(filename))
        file_dir = "upload/user_conf/student/" + slugify(filename.split('.')[0][:20]) + "_" + datetime.datetime.today().strftime("%y%m%d%H%M%S") + extension
        return file_dir"""
    
    Kullanici = models.ForeignKey(User,unique=True,verbose_name="Kullanıcı Adı")
    Grup = models.ForeignKey(Group,verbose_name="Yetki")
    BirthDate = models.DateField(blank=True,null=True,verbose_name="Doğum Tarihi")
    Sex = models.CharField(blank=True,null=True,max_length=200,verbose_name=_(u'Cinsiyet'), choices=SEX_TYPES, default="Kadın")
    #Image = FileFieldProcessor(blank=True,null=True, upload_to=defContentFileName, file_extention=settings.UPLOADABLE_IMAGE_TYPES, max_file_size=settings.MAX_UPLOAD_SIZE,verbose_name="Profil Fotoğrafı", help_text="Yüzün Ön Planda Olduğu Bir Fotoğraf Yükleyin")
    #Country = models.ForeignKey('places.City',related_name='İl', blank=True,null=True,max_length=200, verbose_name="İlçe")
    #City = models.ForeignKey('places.City',related_name='İl', blank=True,null=True,max_length=200, verbose_name="İlçe")
    #State = models.ForeignKey('places.State',related_name='İlçe', blank=True,null=True,max_length=200, verbose_name="İlçe")
    Status = models.BooleanField(default=True ,verbose_name="Aktif")
    Activation = models.CharField(blank=True,unique=True,max_length=200,null=True,verbose_name="Aktivasyon Kodu")
    MadeTime = models.DateTimeField(blank=True,null=True,verbose_name="Oluşturulma Tarihi")
    
    class Meta:
        verbose_name_plural = 'Öğrenci Profilleri'
        verbose_name = 'Öğrenci Profili'
        app_label = string_with_title("user_conf", u"Öğrenci Profilleri")  
        ordering = ['Kullanici']

    def __unicode__(self):
        return self.Kullanici.username 

