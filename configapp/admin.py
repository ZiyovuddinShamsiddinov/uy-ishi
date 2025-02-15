from django.contrib import admin
from configapp.models import Student,Kurs

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone_number','email','kurs','created_ed','updated_ed')
    list_display_links = ['full_name']
    search_fields = ['full_name','kurs']
    # list_editable = ['is_bool']

class KursAdmin(admin.ModelAdmin):
    list_display = ('title','start_date','end_date','description','created_ed','updated_ed')
    list_display_links = ['title']
    search_fields = ['title']
    # list_editable = ['is_bool']


admin.site.register(Student,StudentAdmin)
admin.site.register(Kurs,KursAdmin)

