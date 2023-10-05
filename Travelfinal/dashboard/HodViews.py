from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from dashboard.models import OperationUser,ManagerUser,FinanceUser,CustomUser,ClientUser

def admin_home(request):
    finance_count= FinanceUser.objects.all().count()
    operation_count= OperationUser.objects.all().count()
    manager_count= ManagerUser.objects.all().count()

    context= {
            "all_finance_count": finance_count,
            "all_operations_count": operation_count,
            "all_manager_count": manager_count

    }
    return render(request ,"admin_templates/home_content.html")
# add new finance officer

def add_operation(request):
    return render(request,"admin_templates/add_opertion_template.html")

def add_operation_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_operation')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.staffs.address = address
            user.save()
            messages.success(request, "New Operation added  Successfully!")
            return redirect('add_operation')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_operation')
        
def manage_operation(request):
    operations = OperationUser.objects.all()
    context = {
        "operations": operations
    }
    return render(request, "admin_templates/manage_operation_template.html", context)

def edit_operation(request,oper_id):
    operation = OperationUser.objects.get(admin=oper_id)

    context = {
        "operation": operation,
        "id": oper_id
    }
    return render(request,"admin_templates/edit_operation_template.html", context)

def edit_operation_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            staff_model = OperationUser.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Staff Updated Successfully.")
            return redirect('/edit_staff/'+staff_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/'+staff_id)



def delete_operation(request, staff_id):
    staff = OperationUser.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "Staff Deleted Successfully.")
        return redirect('manage_operation')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_moperation')
    
def add_client(request):
    return render(request,"admin_templates/Add_client_templates.html")

def add_saveclient_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_client')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=0)

            user.ClientUser.address = address
            user.save()
            messages.success(request, "New Client added  Successfully!")
            return redirect('add_client')
        except:
            messages.error(request, "Failed to Add Client!")
            return redirect('add_client')
        
def manage_client(request):
    client = ClientUser.objects.all()
    context = {
        "Clients": client
    }
    return render(request, "admin_templates/manage_client_templates.html", context)

def edit_client(request,client_id):
    Clients = ClientUser.objects.get(admin=client_id)

    context = {
        "Clients": Clients,
        "id": client_id
    }
    return render(request,"admin_templates/edit_client_template.html", context)

def edit_client_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            staff_model = OperationUser.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Staff Updated Successfully.")
            return redirect('/edit_staff/'+staff_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/'+staff_id)



def delete_client(request, staff_id):
    staff = OperationUser.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "Staff Deleted Successfully.")
        return redirect('manage_client')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_client')
    


# manager
def add_managers(request):
    #return redirect (request,"admin_templates/ttt.html")
    return render(request,"admin_templates/add_manager_templates.html")

def add_manager_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_manager')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            
            user.ManagerUser.address = address
            user.save()
            messages.success(request, "New manager added  Successfully!")
            return redirect('add_manager')
        except:
            messages.error(request, "Failed to Add Manager!")
            return redirect('add_manager')
        
def manage_Manager(request):
    manager = ManagerUser.objects.all()
    context = {
        "managers": manager
    }
    return render(request, "admin_templates/manage_manager_templates.html", context)

def edit_manager(request,manager_id):
    Manager = ManagerUser.objects.get(admin=manager_id)

    context = {
        " Managers": Manager,
        "id": manager_id
    }
    return render(request,"admin_templates/edit_Manager_template.html", context)

def edit_Manager_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        manager_id = request.POST.get('manager_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = ManagerUser.objects.get(id=manager_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            manager_model = ManagerUser.objects.get(admin=manager_id)
            manager_model.address = address
            manager_model.save()

            messages.success(request, "Manager Updated Successfully.")
            return redirect('/edit_manager/'+ manager_id)

        except:
            messages.error(request, "Failed to Update Manager.")
            return redirect('/edit_manager/'+manager_id)



def delete_Manager(request, staff_id):
    manager = OperationUser.objects.get(admin=staff_id)
    try:
        manager.delete()
        messages.success(request, "manager Deleted Successfully.")
        return redirect('manage_manager')
    except:
        messages.error(request, "Failed to Delete manager.")
        return redirect('manage_manager')


@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    

def add_manager(request):
    return render(request,"admin_templates/Add_client_templates.html")

def add_savemanager_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_client')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=0)
            
            user.ManagerUser.address = address
            user.save()
            messages.success(request, "New manager added  Successfully!")
            return redirect('add_manager')
        except:
            messages.error(request, "Failed to Add Manager!")
            return redirect('add_client')
        
def manage_Manager(request):
    manager = ManagerUser.objects.all()
    context = {
        "managers": manager
    }
    return render(request, "admin_templates/manage_Manager_templates.html", context)

def edit_manager(request,manager_id):
    Manager = ManagerUser.objects.get(admin=manager_id)

    context = {
        " Managers": Manager,
        "id": manager_id
    }
    return render(request,"admin_templates/edit_Manager_template.html", context)

def edit_Manager_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        manager_id = request.POST.get('manager_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = ManagerUser.objects.get(id=manager_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            manager_model = ManagerUser.objects.get(admin=manager_id)
            manager_model.address = address
            manager_model.save()

            messages.success(request, "Manager Updated Successfully.")
            return redirect('/edit_manager/'+ manager_id)

        except:
            messages.error(request, "Failed to Update Manager.")
            return redirect('/edit_manager/'+manager_id)



def delete_Manager(request, staff_id):
    manager = OperationUser.objects.get(admin=staff_id)
    try:
        manager.delete()
        messages.success(request, "manager Deleted Successfully.")
        return redirect('manage_manager')
    except:
        messages.error(request, "Failed to Delete manager.")
        return redirect('manage_manager')