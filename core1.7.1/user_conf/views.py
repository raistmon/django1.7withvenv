# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.template import RequestContext
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMessage
from smtplib import SMTP
from django.contrib import messages
from django.utils.translation import get_language_info
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
import datetime, random, sha,hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMessage
from smtplib import SMTP
from user_conf.models import Student
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


        
"""
 yapılacaklar:
        
         * email validation
         * password1 != password2
         * deactivation
         * activation kodunun belirli bir süre sonra silinmesi
         * profil dataları güncelleme
         * facebook login
         * güvenlik testleri
"""


def login_view(request):
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None and user.is_active and user.username != "egnity" :

        auth.login(request, user)
        
        return HttpResponseRedirect('/profil/')

    elif user is not None and user.is_active and user.username == "egnity" :
  
        auth.login(request, user),
        
        return HttpResponseRedirect('/admin/')
    
    else:
        hata = "Kullanıcı Adı veya Şifreniz Hatalı"
        return render_to_response('index.html',{'hata':hata},context_instance=RequestContext(request))
 

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/?next=%s' % request.path)



def new_user(request):

    if request.POST:
        
        #formdan gelen verileri alıyoruz
        username = request.POST['username']
        first_name =  request.POST['first_name']
        last_name =  request.POST['last_name']
        password = request.POST['password1']

        exsisting_user = User.objects.filter(username__exact=username)
        
        if exsisting_user:
            
            exsist_message = "Bu e-posta adresine zaten bir üyelik tanımlanmış durumda"
            return render_to_response('index.html',{'exsist_message':exsist_message},context_instance=RequestContext(request))
        
        else:
            
            #formdan gelen verileri kullanarak djangonun user modeline kayıt ediyoruz böylece yeni bir user oluşturabiliriz
            user = User.objects.create_user(username, username, password) #sadece 3 alan koyabiliyoruz fonksiyon buna izin veriyor       
            # ad soyad ve login olabilme özelliğini ayarlıyoruz.
            user.first_name = first_name 
            user.last_name = last_name
            user.is_active = False #false yapma nedenimiz aktivasyon kodunu maila gönderip aktive edebilmemiz için
            user.save()

            current_user = User.objects.get(username=username) #oluşturduğumuz userı çekiyoruz
    
            # oluşturulan user a basic bir profil oluşturuyoruz bu profilde sadece 
            create_student_profile = Student(Kullanici_id = current_user.id, Grup_id = 1)
            create_student_profile.save()
            
            current_student = Student.objects.get(Kullanici__username=username)
            
            key = hashlib.sha1(str(random.random())).hexdigest()[:40]
            now = datetime.datetime.now()
        
            current_student.MadeTime = now 
            current_student.Activation = key
            current_student.save()
            
            #üye mailına activasyon linki yolluyoruz...
            Body = u"Sayın " + current_user.first_name + " " + current_user.last_name + "<br />"
            Body += u"Aşağıdaki linke tıklayarak üyelik aktivasyonunuzu gerçekleştirebilirsiniz." + "<br />"
            Body += u"http://127.0.0.1:8000/aktivasyon/" + str(current_student.Kullanici_id) + "/" + current_student.Activation +"/"
            
            from_addr = u"seymen.sipahi@egnity.com"
            to_addr = username
            subj = u"Mobidemy Üyelik Aktivasyon Mailı"
            
            message_text = Body
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subj
            msg['From'] = from_addr
            msg['To'] = to_addr
    
            html = "<html><head></head><body>"+message_text.encode('utf-8')+"</body></html>"
    
            htmlBody = MIMEText(html, 'html', _charset="UTF-8")
            msg.attach(htmlBody)
    
            smtp = SMTP()
            smtp.set_debuglevel(0)
            smtp.connect( 'smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login('seymen.sipahi@egnity.com', 'egnity1881*')
            smtp.sendmail(from_addr, to_addr, msg.as_string())
            smtp.quit()
              
    return HttpResponseRedirect('/')



def activation (request,id,key):
    
    student = Student.objects.get(Kullanici_id=id,Status=True)
    message =""
    if student.Activation == key:
        
        current_user = User.objects.get(id=id)
        
        if current_user.is_active == False:
        
            current_user.is_active = True
            current_user.save()
            message = "Üyeliğiniz başarıyla aktifleştirilmiştir."
        else:
            
            message = "Üyeliğiniz zaten aktifleştirilmiş. Sisteme giriş yapmanız için login olmanız yeterli." 
    else:
        
         message = "Aktivasyon kodunuz eşleşmiyor"
        
    return render_to_response('activation.html',{'student':student,'message':message},context_instance=RequestContext(request))



@login_required(login_url='/')
def profile (request):
    
    
    return render_to_response('profil.html',{},context_instance=RequestContext(request))


