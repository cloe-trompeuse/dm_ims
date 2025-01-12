from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
# from .models import CustomerOrder, CustomerCart

class CreateCustomer(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CreateSiteCustomer(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'textinput form-control', 'pattern': '[a-zA-Z]{1-30}', 'title':'Alphabets only', 'required':'true'})
        self.fields['last_name'].widget.attrs.update({'class':'textinput form-control', 'pattern': '[a-zA-Z]{1-30}', 'title':'Alphabets only', 'required':'true'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['address'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '^[a-zA-Z0-9 ]*${1,100}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']