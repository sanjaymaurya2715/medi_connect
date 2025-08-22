from django.urls import path
from.import views
urlpatterns = [
   path("",views.home,name="home"),
   path("about_us/",views.about,name="about"),
   path("contact_us/",views.contact,name="contact"),
   path("patient_feedback/",views.patient_feedback,name="patient_feedback"),
   path("patient_login/",views.patient_login,name="patient_login"),
   path("doctor_login/",views.doctor_login,name="doctor_login"),
   path("patient_registration/",views.patient_registration,name="patient_registration"),
   path("patient_dashboard/",views.patient_dashboard,name="patient_home"),
   path("doctor_dashboard/",views.doctor_dashboard,name="doctor_home"),
   path("doctor_logout/",views.doctor_logout,name="doctor_logout"),
   path("patient_logout/",views.patient_logout,name="patient_logout"),
   path("update_recording/",views.update_recording,name="update_recording"),
   path("view_patient/",views.view_patient,name="view_patient"),
   path('doctor_response/<str:patient_id>',views.doctor_response,name="doctor_response"),
   path("response/",views.response,name="response"),
   path("patient_edit_profile/",views.patient_edit_profile,name="patient_edit_profile"),
   path("doctor_edit_profile/",views.doctor_edit_profile,name="doctor_edit_profile"),
   path("about_vitamins/",views.about_vitamins,name="about_vitamins"),
   path("about_blood/",views.about_blood,name="about_blood"),


  
]
