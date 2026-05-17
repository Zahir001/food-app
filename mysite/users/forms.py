from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email','password1','password2',]


# Django Auth Notes

# User model

# Database table/model
# Fields:
# username, email, first_name, last_name, password etc.

# UserCreationForm

# User input + validation form
# Default fields:
# username
# password1
# password2

# Use Cases

# Bas 3 fields chahiye:
# → direct UserCreationForm use karo
# Extra form fields chahiye:
# → UserCreationForm customize karo (inherit kr ke customize class bna lo)
# Extra database fields chahiye:
# → AbstractUser use karo

# Important

# Sirf wahi fields automatically save hote hain jo User model me already exist karte hain
# Example:
# email ✔
# emaillll ❌
# phone ❌ (unless custom user model)