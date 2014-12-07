from user_conf.models import *
from django.contrib import admin
from django.forms import TextInput, Textarea,ModelForm
#from suit.admin import SortableTabularInline


"""
class CountryForm(ModelForm):
    class Meta:
        widgets = {
            'NameSurname': TextInput(attrs={'style': 'width:200px;'}),
            'Phone1': TextInput(attrs={'style': 'width:100px;'}),
            'Phone2': TextInput(attrs={'style': 'width:100px;'}),
        }

class EmergencyInline(SortableTabularInline):
    
    model = EmergencyContact
    sortable = 'OrderID'
    form = CountryForm

"""   

class AdminStudent(admin.ModelAdmin):
    
    list_display = ('Kullanici','Ad','Soyad','Status',)
    list_display_links = ('Kullanici','Ad','Soyad','Status',)
    list_filter = ('Sex','Status',)
    search_fields = ['Kullanici','Ad','Soyad',]
    
    def Ad(self, instance):
        return instance.Kullanici.first_name
    
    def Soyad(self, instance):
        return instance.Kullanici.last_name
    
    
admin.site.register(Student,AdminStudent)

 