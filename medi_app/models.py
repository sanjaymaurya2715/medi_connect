from django.db import models

# Create your models here.

from django.utils import timezone

# contact  model
class Contact(models.Model):# inheriting model in contact 
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=55)
    phone = models.CharField(max_length=10)
    question = models.TextField()
    date= models.DateField(default=timezone.now)

# feedback

class FeedBack (models.Model):
     name = models.CharField(max_length=45)
     email = models.EmailField(max_length=55)
     rating = models.CharField(max_length=5)
     review=models.TextField()
     date=models.DateField(default=timezone.now)
     pic=models.CharField(max_length=100,default="")


# doctor
class Doctor (models.Model):
     name = models.CharField(max_length=50)
     email = models.CharField(max_length=55,primary_key=True)
     password = models.CharField(max_length=50)
     phone = models.CharField(max_length=13)
     specilization = models.CharField(max_length=100)
     qualification = models.FileField(upload_to='doctor/')
     experinces = models.CharField(max_length=100)
     profile_picture = models.FileField(upload_to='doctor_profile/')


# patient
gender=(('','select gender'),("male","male"),("female","female"))

class Patient (models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField(max_length=55,)
     patient_id= models.CharField(max_length=20,unique=True)
     password = models.CharField(max_length=20)
     phone = models.CharField(max_length=13)
     age = models.CharField(max_length=3)
     gender = models.CharField(max_length=6,choices=gender)
     problem = models.TextField()
     doctor_email = models.EmailField(max_length=50)
     profile_picture = models.FileField(upload_to='patient_profile/')
     
     def save(self, *args, **kwargs):
          if not self.patient_id:
               super().save(*args, **kwargs)
               self.patient_id = f'p-{self.id}'
               super().save(*args, **kwargs)
          else:
                super().save(*args, **kwargs)


               

class Voice_Constellation (models.Model):
     patient_id =models.CharField(max_length=50,primary_key=True)
     prescription =models.FileField(upload_to='patient/')
     report_file =models.FileField(upload_to='patient/',null=True,blank=True)
     audio_file =models.FileField(upload_to='patient/')
     submisson_date =models.DateField(default=timezone.now)
     response_audio_file =models.FileField(upload_to='patient/')
     response_date =models.CharField(default='',max_length=30)
     response_status =models.CharField(max_length=10)

    