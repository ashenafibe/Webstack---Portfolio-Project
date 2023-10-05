from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import UploadedFile,ClientRequestss
from .forms import UploadFileForm,clientRequestForm,clientRequestSearchForm,clientRequestmanagerForm,clientRequestOperationForm
from django.db.models import Q
from django.contrib import messages

# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from dashboard.EmailBackEnd import EmailBackEnd

# Client module

def index (request):
    return render(request, 'index.html', {})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.all()
    return render(request, 'upload_file.html', {'form': form, 'files': files})

def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response
#cleint request method
def client_req(request):
    if request.method =='POST':
        form = clientRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully saved')
    else:
        form= clientRequestForm()
    files = ClientRequestss.objects.all()
    return render(request, 'main/Add_client_request.html', {'form': form, 'files': files})

def success(request):
    return HttpResponse('successfully saved')
# sear result by passport no
def search_post(request):
    if request.method == 'POST':
        form= clientRequestSearchForm(request.POST)
        
        search_query=request.POST.get('passPort_no')
        results=ClientRequestss.objects.filter(passPort_no=search_query).values()
        return render(request, 'main/search.html', {'query':search_query, 'results':results})
    else:
        form= clientRequestSearchForm()
        return render(request, 'main/search.html',{'form':form})
def search_request(request):
    return render(request, 'main/search.html',{})
# search form
def search_form(request):
    
    if request.method == 'POST':
        
        search_query=request.POST.get('search')
        listoreq=ClientRequestss.objects.filter(passPort_no=search_query).values()
        return render(request, 'main/detail_client_request.html', {'listoreqs':listoreq})
    
# update request
def update_request(request, pk):
    current_record =  ClientRequestss.objects.get(id=pk)
    form = clientRequestForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('search_form')
    return render(request, 'main/update_record.html', {'form':form})


# find especific client request	
def customer_request (request, pk):
    customer_request = ClientRequestss.objects.get(id=pk)
    return render(request, 'main/detailsview.html', {'customer_request':customer_request})
	
# print schedule
def print_record(request, pk):
        # Look Up request
    customer_request =ClientRequestss.objects.get(id=pk)
    return render(request, 'main/Print_client_request.html', {'customer_request':customer_request})

# staff module

def loginPage(request):
    return render(request, 'login.html')
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type=='0':
                return redirect("home_client")
            elif user_type == '1':
               return redirect("admin_home")
                
            elif user_type == '2':
               
                return redirect('manager_home')
                
            elif user_type == '3':
               return redirect('current_page')
            elif user_type == '4':
                
                return redirect('finance_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')
        
def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')



def current_page(request):
     return render(request,"operation_templates/operation_home_template.html",{})

def manage_requests(request):
   listoreqs = ClientRequestss.objects.all().order_by('created_at').values()
   context = {
        "listoreqs": listoreqs
    }
   return render(request, 'operation_templates/manage_requests_templates.html', context)

# view details of record
def viewclient_details(request, request_id):
    customer_requests = ClientRequestss.objects.get(id=request_id)
    context = {
        "customer_request":customer_requests,
        "id": request_id
    }
    return render(request, 'operation_templates/view_details_template.html', context)

def edit_requests(request, request_id):
    customer_requests = ClientRequestss.objects.get(id=request_id)
    context = {
        "customer_request":customer_requests,
        "id": request_id
    }
    form = clientRequestOperationForm(request.POST or None, instance=customer_requests)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('search_form')

    return render(request, 'operation_templates/update_request.html', {'form':form})


# for manager 
def current_page_manager(request):
     return render(request,"manager_templates/manager_home_template.html",{})


def manage_requests_manager(request):
   listoreqs = ClientRequestss.objects.all().order_by('created_at').values()
   context = {
        "listoreqs": listoreqs
    }
   return render(request, 'manager_templates/manage_requests_templates.html', context)


def edit_requests_manager(request, request_id):
    customer_requests = ClientRequestss.objects.get(id=request_id)
    context = {
        "customer_requests":customer_requests,
        "id": request_id
    }
    return render(request, 'manager_templates/edit_course_template.html', context)

			
	


    
	
			
    
   
		

    

    
