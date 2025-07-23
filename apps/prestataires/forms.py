# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# from apps.services.models import ServiceType, Service
# from .models import Prestataire
# User = get_user_model()


# class PrestataireRegisterForm(UserCreationForm):
#     first_name = forms.CharField(label="Prénom")
#     last_name = forms.CharField(label="Nom")
#     phone = forms.CharField(label="Téléphone", required=False)
#     address = forms.CharField(label="Adresse", required=False)

#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name', 'phone', 'address', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_prestataire = True
#         if commit:
#             user.save()
#         return user

from django import forms
from apps.prestataires.models import Prestataire
from apps.services.models import Service, ServiceCategory
from django.forms.utils import ErrorList
from django.template.defaultfilters import register


class PrestataireRegisterForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=ServiceCategory.objects.all(),
        label="Type de service",
        required=True
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.none(),
        label="Service",
        required=True
    )
    email = forms.EmailField(label="Adresse e-mail", required=False)
    first_name = forms.CharField(label="Prénom", max_length=30, required=True)
    last_name = forms.CharField(label="Nom", max_length=30, required=True)
    phone = forms.CharField(label="Numéro de téléphone", max_length=15, required=False)
    address = forms.CharField(label="Adresse", max_length=255, required=False)

    class Meta:
        model = Prestataire
        fields = ['email', 'first_name', 'last_name', 'phone', 'address', 'category', 'service']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['service'].queryset = Service.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.category:
            self.fields['service'].queryset = self.instance.category.services.all()


@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})
