# import requests
from django.conf import settings
from django.core.mail import send_mail

def send_email_token(email,token):
    try:
        
        subject = 'welcome to Budget Buddy'
        # print("hello")
        message = f'Hi,click on the given link to verify http://127.0.0.1:8000/verify/{token}/'
        # print("ujell")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        print(settings.EMAIL_HOST_USER)
        send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
                
        
        
        
    except Exception as e:
        print("failed")
        print(e)
        return False
    return True
    
    