from django import forms
from .models import User
import bcrypt

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput
        }
    
    def clean_password(self):
        password = self.cleaned_data['password']
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')