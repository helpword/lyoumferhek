from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationForm, UserChangeForm as DjangoUserChangeForm)
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ( UserCreationForm as DjangoUserCreationForm )
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from . import models 
from django.utils.translation import gettext_lazy as _

import logging

from django import forms

logger = logging.getLogger(__name__)
User = get_user_model()

class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ("email",'first_name', "last_name","groups", "is_staff", "is_active","password1")
        field_classes = {"email": UsernameField}
        
  

class UserEditionForm(forms.ModelForm):
    
    class Meta(DjangoUserChangeForm.Meta):
        model = User
        fields = ("email", 'first_name', "last_name","is_active","is_staff","groups")
    def __init__(self,request,*args , **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        if not self.request.user.is_superuser and self.request.user.has_perm('users.change_user') :
            self.fields.pop('is_active',None)
            self.fields.pop('is_staff' , None)
            self.fields.pop('groups',None)
            

class ChangePasswordForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = models.User
        fields = ('password',)
        widgets = {
            # 'first_name': forms.TextInput(attrs={'class' : 'form-control' }),
            'password'  : forms.PasswordInput(attrs={'class' : 'form-control' }),
        }
    # def __init__(self, ticket=None, *args, **kwargs):   
    #     super().__init__(*args, **kwargs)
    #     self.fields["password"].widget.attrs.update()

    #     self.fields['password'].error_messages = {
    #         'required': 'Veuillez renseigner ce champ.',
    #         'invalid': 'Custom error message for field1 is invalid.',
    #         # Add more custom error messages for different errors if needed
    #     }
    #     self.fields['password2'].error_messages = {
    #         'required': 'Veuillez renseigner ce champ.',
    #         'invalid': 'Custom error message for field1 is invalid.',
    #         # Add more custom error messages for different errors if needed
    #     }


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2:
            if password != password2:
                self.add_error('password2', _("Les mots de passe ne correspondent pas."))
        return cleaned_data
    
  


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name','permissions', )

    def __init__(self, *args, **kwargs):
        super(AddGroupForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {
            'required': 'veuillez choisir.',
            'invalid': 'Custom error message for field1 is invalid.',
          
        }




# --------------------------------------Authentication-------------------------------------------------
class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
            strip=False, widget=forms.PasswordInput 
    )
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email is not None and password:
            self.user = authenticate(
                self.request, email=email.lower(), password=password
            )
            if self.user is None:
                raise forms.ValidationError(
                    "Invalid email/password combination."
            )
        logger.info(
            "Authentication successful for email=%s", email
            )
        return self.cleaned_data
    def get_user(self):
        return self.user 



class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = models.User
        fields = ('email' , 'password')
        widgets = {
            # 'first_name': forms.TextInput(attrs={'class' : 'form-control' }),
            'email'     : forms.EmailInput(attrs={'class' : 'form-control' }),
            'password'  : forms.PasswordInput(attrs={'class' : 'form-control' }),
        }




