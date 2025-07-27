from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from apps.prestataires.models import Prestataire
from apps.wilayas.models import Wilaya, Commune
from django import forms
from .models import Prestataire

class PrestataireUpdateForm(forms.ModelForm):
    class Meta:
        model = Prestataire
        fields = ['phone', 'service_type', 'wilaya', 'commune']


User = get_user_model()

class PrestataireRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Prénom")
    last_name = forms.CharField(label="Nom")
    phone = forms.CharField(label="Téléphone", required=False)
    address = forms.CharField(label="Adresse", required=False)
    
    # name_ar = forms.CharField(label="Nom en arabe", required=True)
    # name_fr = forms.CharField(label="Nom en français", required=True)
    # service_type = forms.ChoiceField(label="Type de service", choices=Prestataire._meta.get_field('service_type').choices)
    # wilaya = forms.ModelChoiceField(queryset=Wilaya.objects.all(), required=True)
    # commune = forms.ModelChoiceField(queryset=Commune.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'address', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(PrestataireRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_prestataire = True
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address = self.cleaned_data['address']
        
        if commit:
            user.save()
            Prestataire.objects.create(
                user=user,
               name_fr = self.cleaned_data['first_name'],
               phone = user.phone,
               email=user.email,
            )
        return user


                # name_ar=self.cleaned_data['name_ar'],
                # name_fr=self.cleaned_data['name_fr'],
                # service_type=self.cleaned_data['service_type'],
                # wilaya=self.cleaned_data['wilaya'],
                # commune=self.cleaned_data['commune'],
                # phone=self.cleaned_data['phone'],
                # email=self.cleaned_data['email'],