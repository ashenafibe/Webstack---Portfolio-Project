from django import forms
from .models import UploadedFile,ClientRequestss
from django.forms import ModelForm,TextInput,FileInput,DateInput,NumberInput,EmailInput

class DateInput(forms.DateInput):
	input_type='date'

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)

class clientRequestForm(forms.ModelForm):
    date_of_birth = forms.DateTimeField(required=True,widget=DateInput)
    departure_date=forms.DateTimeField(required=True,widget=DateInput)
    date_of_return=forms.DateTimeField(required=True,widget=DateInput)
    email = forms.EmailInput()
    class Meta:
        model = ClientRequestss
        exclude = ('status','policy_no',)

class clientRequestSearchForm(forms.ModelForm):
     class Meta:
        model= ClientRequestss
        fields= ('passPort_no',)
class clientRequestOperationForm(forms.ModelForm):
     class Meta:
          model= ClientRequestss
          exclude=('email',)
class clientRequestmanagerForm(forms.ModelForm):
     class Meta:
          model = ClientRequestss
          exclude = ('email',)
