from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Overriding the default Django Auth User and adding one More Field User_type
class CustomUser(AbstractUser):
	user_type_data=((1,"HOD"),(2,"MGR"),(3,"OPE"),(4,"Fin"),(0,"Client"))
	user_type= models.CharField(default=1, choices=user_type_data,max_length=10)
class AdminHOD(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	created_at= models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects=models.Manager()
class ManagerUser(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	address=models.TextField()
	created_at= models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects=models.Manager()
class OperationUser(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	address=models.TextField()
	created_at= models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects=models.Manager()
class FinanceUser(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	address=models.TextField()
	created_at= models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects=models.Manager()
class ClientUser(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	address=models.TextField()
	created_at= models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects=models.Manager()

class UploadedFile(models.Model):

    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
	
class ClientRequests(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	midle_name =  models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	date_of_birth = models.DateTimeField()
	passPort_no = models.CharField(max_length=15)
	passportcopy= models.FileField(upload_to="project_images/", blank=True)
	Payslip= models.FileField(upload_to='uploads/',blank=True)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	email =  models.CharField(max_length=100)
	zipcode =  models.CharField(max_length=20)
	departure_date=models.DateTimeField()
	date_of_return=models.DateTimeField()
	duration_of_cover=models.CharField(max_length=20)
	destination=models.CharField(max_length=20)
	other_destination=models.CharField(max_length=20)
	status=models.CharField(max_length=20, default=0)
	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	
# change
class ClientRequestss(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now_add=True)
	policy_no =models.CharField(max_length=20, null=True)
	first_name = models.CharField(max_length=50)
	midle_name =  models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	date_of_birth = models.DateTimeField()
	passPort_no = models.CharField(max_length=15)
	passportcopy= models.FileField(upload_to="project_images/", blank=True)
	Payslip= models.FileField(upload_to='uploads/',blank=True)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	email =  models.CharField(max_length=100)
	zipcode =  models.CharField(max_length=20)
	departure_date=models.DateTimeField()
	date_of_return=models.DateTimeField()
	duration_of_cover=models.CharField(max_length=20)
	destination=models.CharField(max_length=20)
	other_destination=models.CharField(max_length=20)
	status=models.CharField(max_length=20, default=0)
	def __str__(self):
		return(f"{self.first_name} {self.last_name}")