from django.shortcuts import render
from core.models import costumer
from django.http import HttpResponseRedirect
from twilio.rest import Client
# Create your views here.
def send(request,phone_number): 
    # account_sid = 'ACc27bb9e9b7a2007fd5e2f5b7116b5dad'
    # auth_token = '16e0dde1344db104c25583319e5dfd74'
    # client = Client(account_sid, auth_token)


    # from_number = '+16693364094'
    # message_body = 'Hello from Twilio!'
    # message = client.messages.create(
    # to='whatsapp:+9647806969277', 
    # from_=from_number,
    # body=message_body)
    # print(f"Sent message to {message}")
    # account_sid = 'AC2f2416b15c52267e36c04b78d1d26748' 
    # client = Client(account_sid, auth_token) 
 
    # message = client.messages.create(from_='whatsapp:+17013142921',body='Ahmed shab',to='whatsapp:+9647710639740') 
 
    # print(message.sid)
    account_sid = 'AC2f2416b15c52267e36c04b78d1d26748' 
    auth_token = '857390d32a998d017096583e4f0ba795' 

    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='اسمي',      
                              to='whatsapp:+9647834400514' 
                          ) 
 
    print(message.sid)

    return HttpResponseRedirect("/admin/core/costumer/")