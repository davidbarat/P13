from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    phone = forms.IntegerField(
        label="Votre Téléphone",
        max_value=999999999,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}))
        # group_admin = models.BooleanField(default=False)

    class Meta:
        model = UserProfile
        exclude = ['user','group_id','group_admin']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone']

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(
        label="Votre email",
        max_length=50,
        widget=forms.TextInput(attrs={"style": "color:black", "type": "text"}),
    )
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(
        label="Nom d utilisateur",
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