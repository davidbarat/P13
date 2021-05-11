from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Group


class UserProfileForm(forms.ModelForm):
    phone = forms.IntegerField(
        label="Téléphone",
        max_value=999999999,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}))

    class Meta:
        model = UserProfile
        exclude = ['user', 'group_id', 'group_admin', 'group']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone']


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        max_length=50,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=30,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )
    first_name = forms.CharField(
        label="Prénom",
        max_length=30,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )
    last_name = forms.CharField(
        label="Nom",
        max_length=30,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name", "username")


class UserForm(forms.ModelForm):

    email = forms.EmailField(
        label="Votre email",
        max_length=50,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password")


class GroupForm(forms.ModelForm):

    group_name = forms.CharField(
        label="Le nom du groupe",
        max_length=50,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )
    adress = forms.CharField(
        label="Adresse",
        max_length=50,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )
    zipcode = forms.IntegerField(
        label="Code Postal",
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )
    city = forms.CharField(
        label="Ville",
        max_length=30,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )

    class Meta:
        model = Group
        fields = ("group_name", "adress", "zipcode", "city")


class ContactForm(forms.Form):

    Nom = forms.CharField(max_length=50)
    Email = forms.EmailField(max_length=50)
    Mobile = forms.CharField()
    Message = forms.CharField(widget=forms.Textarea, max_length=2000)
