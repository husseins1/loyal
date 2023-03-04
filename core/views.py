from django.shortcuts import render
from core.models import costumer,Order
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.serializers import serialize
from django.core import serializers
import json
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


def print_id(request,id): 
    custom=costumer.objects.get(identity=id)
    return render(request, 'print.html', {'custom': custom})

def analytics(request):
    orders = Order.objects.all()
    myObjs = []
    for x in orders:
        dic ={}
        dic['name'] = x.customer.first_name + ' ' + x.customer.last_name
        dic['id'] = x.customer.identity.__str__()
        dic['table'] = x.invoice.tableNumber
        dic['date'] = x.date_placed.__str__()
        dic['total'] = x.invoice.totalPrice.__str__()
        myObjs.append(dic)

    data = json.dumps(myObjs)
    # data = serialize('json',orders, use_natural_primary_keys=True, use_natural_foreign_keys=True)
    # return HttpResponse(data,content_type='application/json')
    return render(request,'analytics.html',{'orders':data})

def getOrders(request):
    orders = Order.objects.all()
    myObjs = []
    for x in orders:
        dic ={}
        dic['name'] = x.customer.first_name + ' ' + x.customer.last_name
        dic['id'] = x.customer.identity.__str__()
        dic['table'] = x.invoice.tableNumber
        dic['date'] = x.date_placed.__str__()
        dic['total'] = x.invoice.totalPrice.__str__()
        myObjs.append(dic)

    data = json.dumps(myObjs)
    # data = serializers.serialize('json',orders, use_natural_primary_keys=True, use_natural_foreign_keys=True)
    return JsonResponse(data,safe=False)