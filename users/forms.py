from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ('username','password')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)