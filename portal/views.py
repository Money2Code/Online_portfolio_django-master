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

        # send_mail(
        #     'Contact',
        #     descsription,
        #     settings.EMAIL_HOST_USER,
        #     [email,],
        #     fail_silently=False
        # )
        
        # with get_connection(  
        #    host=settings.EMAIL_HOST, 
        #     port=settings.EMAIL_PORT,  
        #     username=settings.EMAIL_HOST_USER, 
        #     password=settings.EMAIL_HOST_PASSWORD, 
        #     use_tls=settings.EMAIL_USE_TLS  
        #  ) as connection:  
        #    subject = request.POST.get("email_subject")  
        #    email_from = settings.EMAIL_HOST_USER  
        #    recipient_list = [request.POST.get("email"), ]  
        #    message = request.POST.get("descsription")  
        #    EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
 
        # try:
        #     send_mail(email_subject,descsription,email,['abhinavdogra613@gmail.com'])
        # except BadHeaderError:
        #     return HttpResponse("Invalid header found") 
        email = EmailMessage('Subject', 'Body', to=[email])
        email.send()
    return render(request,'index.html')
