from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from dashboard.models import OperationUser,ManagerUser,FinanceUser,CustomUser,ClientRequestss

def operation_home(request):
    
    context={
    "number_active":ClientRequestss.objects.filter(status=0).count(),
    "number_checked":ClientRequestss.objects.filter(status=1).count(),
    "number_paid": ClientRequestss.objects.filter(status=3).count()

    }
    
    return render(request,"operation_templates/operation_home_template.html",{})

# manage client requesat list all request
def manage_request(request):
     listoreqs = ClientRequestss.objects.all().order_by('created_at').values()
     return redirect(request ,"operation_templates/manage_client_request.html",{'listoreqs':listoreqs})


    

    