from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
   """ Form to be used to register user """
   password1   = forms.CharField(label='Password', widget=forms.PasswordInput)
   password2   = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
      help_texts = {
            'username': None,
        }

   def clean_email(self):
      email = self.cleaned_data.get('email')
      username = self.cleaned_data.get('username')
      qs = User.objects.filter(email=email).exclude(username=username)
      if qs.exists():
         raise forms.ValidationError("This email address already exists!")
      return email

   def clean_password(self):
      password1 = self.clean_email.get('password1')
      password2 = self.clean_email.get('password2')

      if not password1 or not password2:
         raise forms.ValidationError("Password must not be empty")

      if password1 != password2:
         raise forms.ValidationError("Passwords do not match")

      return password2

class UserLoginForm(forms.Form):
   """ Form to be used to log user in """
   username = forms.CharField()
   password = forms.CharField(widget=forms.PasswordInput)