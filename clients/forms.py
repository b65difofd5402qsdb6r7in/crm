from django import forms
from .models import Client, Utilisateur
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )
        fields_classes = {'username': UsernameField}

class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
        'nom',  
        'prenom', 
        'civilite',
        'numero_telephone', 
        'email', 
        'siret',
        'adresse',
        'ville',
        'code_postal',
        'nom_societe',
        'statut_juridique',
        'commentaire',
        'responsable_commercial'
        )

class UtilisateurModelForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    fonction = forms.CharField(max_length=150)
    nom = forms.CharField(max_length=150)
    prenom = forms.CharField(max_length=150)
    numero_telephone = forms.CharField(max_length=150)
    email = forms.EmailField()
    class Meta:
        model = Utilisateur
        fields = (
            'username',
            'password',
            'fonction',
            'nom',
            'prenom', 
            'numero_telephone',
            'email',
        )


    def save(self, commit=True):
        utilisateur = super().save(commit=False)
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        fonction = self.cleaned_data['fonction']
        nom = self.cleaned_data['nom']
        prenom = self.cleaned_data['prenom']
        numero_telephone = self.cleaned_data['numero_telephone']
        email = self.cleaned_data['email']
        
        user = User.objects.create_user(username=username, password=password)
        utilisateur.utilisateur = user
        
        utilisateur.fonction = fonction
        utilisateur.nom = nom
        utilisateur.prenom = prenom
        utilisateur.numero_telephone = numero_telephone
        utilisateur.email = email

        if commit:
            utilisateur.save()
        return utilisateur
