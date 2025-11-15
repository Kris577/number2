# catalog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser
import re

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=150, label="ФИО")
    email = forms.EmailField(label="Email")

    class Meta:
        model = CustomerUser
        fields = ("username", "full_name", "email", "password1", "password2")

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # Регулярное выражение для проверки ФИО: кириллические буквы, пробелы, дефисы
        if not re.match(r'^[а-яёА-ЯЁ\s\-]+$', full_name):
            raise forms.ValidationError("ФИО может содержать только кириллические буквы, пробелы и дефисы.")
        return full_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Регулярное выражение для проверки логина: латиница и дефис
        if not re.match(r'^[a-zA-Z\-]+$', username):
            raise forms.ValidationError("Логин может содержать только латинские буквы и дефисы.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Подтверждение пароля не совпадает.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data["full_name"]
        user.email = self.cleaned_data["email"]
        # username и password уже установлены в UserCreationForm
        if commit:
            user.save()
        return user
