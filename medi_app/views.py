from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from.models import FeedBack,Contact,Patient,Doctor,Voice_Constellation
from django.views.decorators.cache import cache_control
from datetime import date
from django.contrib import messages 
def home(request):
    FeedBack_list=FeedBack.objects.order_by('-date')[:5]
    context={"feedback_key":FeedBack_list}# created dictonary


    return render(request,'medi_app/html/index.html',context)#send it on index.html

def about(request):
    return render(request,'medi_app/html/about_us.html')

def contact(request):
    if request.method=="GET":#http prtocol method
        return render(request,'medi_app/html/contact_us.html')
    if request.method=="POST":#request .post are built in dictonery
        nm=request.POST["u_name"]# fetch the value from control
        em=request.POST["u_email"]
        ph=request.POST["u_phone"]
        qs=request.POST["u_question"]
        # object of feedback model        
        Contact_obj=Contact(name=nm,email=em,phone=ph,question=qs)
        Contact_obj.save()#it will map in colum table 
        messages.success(request,"Thanku For Response 😊😊")

        return render(request,'medi_app/html/contact_us.html')
    




def patient_feedback(request):
    if request.method=="GET":#http prtocol method

        return render(request,'medi_app/patient/patient_feedback.html')
    if request.method=="POST":#request .post are built in dictonery
        nm=request.POST["u_name"]# fetch the value from control
        em=request.POST["u_email"]
        rt=request.POST["rating"]
        rw=request.POST["u_review"]
        pic = request.session["pt_pic"]
        # object of feedback model        
        FeedBack_obj=FeedBack(name=nm,email=em,rating=rt,review=rw,pic = pic)
        FeedBack_obj.save()#it will map in colum table 
        messages.success(request," Thanku For Your Feedback😊😊")
        return render(request,'medi_app/patient/patient_feedback.html')



def patient_login(request):
    if request.method=="GET":
        return render(request,'medi_app/patient/patient_login.html')
    if request.method=="POST":
        em = request.POST["user_email"]
        pwd = request.POST["user_pass"]
        patient_list = Patient.objects.filter(patient_id=em,password=pwd)
        if len(patient_list)>0:
            # student_obj = student_list[0]
            # session creation and binding email in that session to identify user request
            request.session["session_key"]=patient_list[0].patient_id
            request.session["pt_pic"]=patient_list[0].profile_picture.url

            return redirect("patient_home")
        else:
            messages.error(request,"Ivalid Credential")
            return redirect("patient_login")
        
@cache_control(no_cache=True, must_revalidate=True,no_store=True)


def patient_dashboard(request):
    patient_id = request.session["session_key"]#fetching the value for session
    patient_obj = Patient.objects.get(patient_id = patient_id)
    context = {"patient_key":patient_obj}

    return render(request,"medi_app/patient/patient_home.html",context)


def doctor_login(request):
    if request.method=="GET":
        return render(request,'medi_app/doctor/doctor_login.html')
    if request.method=="POST":
        em = request.POST["user_email"]
        pwd = request.POST["user_pass"]
        doctor_list = Doctor.objects.filter(email=em,password=pwd)
        if len(doctor_list)>0:
            # doctor_obj = doctor_list[0]
            # session creation and binding email in that session to identify user request
            request.session["session_key"]=em
           
            return redirect("doctor_home")
        else:
            messages.error(request,"Ivalid Credential")
            return redirect("doctor_login")
        
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required(login_url="doctor_login")
def doctor_dashboard(request):
    email = request.session["session_key"]#fetching the value for session
    doctor_obj = Doctor.objects.get(email = email)
    context = {"doctor_key":doctor_obj}

    return render(request,"medi_app/doctor/doctor_home.html",context)
    

def patient_registration(request):
    return render(request,'medi_app/patient/patient_registration.html')

def doctor_logout(request):
    del request.session["session_key"]#delete the session
    return redirect("/doctor_login/")

def patient_logout(request):
    del request.session["session_key"]#delete the session
    return redirect("/patient_login/")

def update_recording(request):
    if request.method=="GET":
        return render(request,'medi_app/patient/update_recording.html')
    if request.method=="POST":
        report = request.FILES.get("report")
        prescription = request.FILES.get("prescription")
        patient_id = request.session["session_key"]
        audio_file = request.FILES.get("audio_file")
        voice = Voice_Constellation(patient_id=patient_id,prescription=prescription,report_file=report,audio_file=audio_file)
        voice.save()
        return redirect("update_recording")
def view_patient(request):
    patient = Voice_Constellation.objects.all()
    return render(request,"medi_app/doctor/view_patient.html",{"recordings":patient})

def doctor_response(request,patient_id):
    if request.method=="GET":
        return render(request,"medi_app/doctor/doctor_response.html")

    if request.method == "POST":
        recording = get_object_or_404(Voice_Constellation, patient_id=patient_id)

        # Handle the file upload for the doctor's response
        response_file = request.FILES.get("audio_file")
        if response_file:
            # Update the response field of the recording
            recording.response_audio_file = response_file
            recording.response_date=date.today()
            recording.response_status="True"
            recording.save()  # Save the updated recording object
            return redirect('home')
def response(request):
    patient_id = request.session["session_key"]
    recordings = Voice_Constellation.objects.filter(patient_id=patient_id)
    print(patient_id)  # Fetch all uploaded recordings
    return render(request, 'medi_app/patient/response.html', {'recordings': recordings})



def patient_edit_profile(request):
    
    if request.method=="GET":
     
        patient_id = request.session["session_key"]#fetching the value for session
        patient_obj = Patient.objects.get(patient_id = patient_id)
        context={
             "patient_key":patient_obj
         } 


        return render(request,'medi_app/patient/patient_edit_profile.html',context)
    if request.method=="POST":
        patient_id = request.session["session_key"]#fetching the value for session
        patient_obj = Patient.objects.get(patient_id = patient_id)
        ph=request.POST["u_phone"]
        ag=request.POST["u_age"]
        patient_obj.phone=ph
        patient_obj.age=ag
        patient_obj.save()# it will modify the old object with new values
        return redirect("patient_home")

def doctor_edit_profile(request):
    
    if request.method=="GET":
     
        email = request.session["session_key"]#fetching the value for session
        doctor_obj = Doctor.objects.get(email = email)
        context={
             "doctor_key":doctor_obj
         } 


        return render(request,'medi_app/doctor/doctor_edit_profile.html',context)
    if request.method=="POST":
        email = request.session["session_key"]#fetching the value for session
        doctor_obj = Doctor.objects.get(email = email)
        ph=request.POST["u_phone"]
        doctor_obj.phone=ph
     
        doctor_obj.save()# it will modify the old object with new values
        return redirect("doctor_home")
def about_vitamins(request):
    return render(request,"medi_app/html/about_vitamins.html")
def about_blood(request):
    return render(request,"medi_app/html/about_blood.html")