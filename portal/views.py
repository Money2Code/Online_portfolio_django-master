from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail,BadHeaderError
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.core.mail import EmailMessage
# Create your views here.
from .models import contact_details
def home(request):
    if request.method =='POST':
        Full_name=request.POST['Full_name']
        email=request.POST['email']
        mobile_number=request.POST['mobile_number']
        email_subject=request.POST['email_subject']
        descsription=request.POST['descsription']
        new_contact=contact_details(Full_name=Full_name, email=email, mobile_number=mobile_number, email_subject=email_subject, descsription=descsription)
        new_contact.save() 
        email = EmailMessage('Subject', 'Body', to=[email])
        email.send()
    return render(request,'index.html')
