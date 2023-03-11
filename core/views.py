from django.shortcuts import render
from core.models import costumer,Order
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.serializers import serialize
from django.core import serializers
import json
# Create your views here.
def history(request,id): 
    customer = costumer.objects.get(identity=id)
    orders = Order.objects.filter(customer_id = id).order_by('-date_placed')
    context = {'orders': orders}
    return render(request,'history.html',context)


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