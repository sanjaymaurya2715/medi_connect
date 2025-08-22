from django.contrib import admin

from .models import Contact,FeedBack,Doctor,Patient,Voice_Constellation 
class PatientAdmin(admin.ModelAdmin):
    list_display=("patient_id","name","email","password","phone","age","gender","problem","doctor_email","profile_picture")
    readonly_fields=('patient_id',)

admin.site.register(Contact)
admin.site.register(FeedBack)
admin.site.register(Doctor)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Voice_Constellation)