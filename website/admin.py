from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
 date_hierarchy = "created_date"
 #empty_value_display = "-empty-"
#fields = ['title','content']
 list_display = ['name','email', 'created_date']
 ist_filter=('email',)
 #ordering=['-created_date']
 search_fields=('name','message')

class Meta:
       ordering= ['-created_date']
       verbose_name_plural = "کاربرها"



admin.site.register(Contact,ContactAdmin)