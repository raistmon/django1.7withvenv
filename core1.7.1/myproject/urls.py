# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from user_conf.views import login_view, logout_view, profile,new_user,activation

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)), #admin sayfası template url'leri.
    (r'^$', TemplateView.as_view(template_name="index.html")), #giriş sayfası template.
    (r'^yeni-uye/$', new_user), # üye kayıt
    (r'^uye-giris/$', login_view), #login oluyoruz.
    (r'^uye-cikis/$', logout_view), #logout oluyoruz.
    (r'^profil/$', profile), #logout oluyoruz.
    (r'^aktivasyon/([\w\-]+)/([\w\-]+)/$',activation), #activasyon mailından gelen url
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
