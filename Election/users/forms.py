from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    regno = forms.CharField(max_length=20)
    branch = forms.CharField(max_length=100)
    semester = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'regno', 'branch', 'semester', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(
                user=user,
                regno=self.cleaned_data['regno'],
                branch=self.cleaned_data['branch'],
                semester=self.cleaned_data['semester']
            )
            user_profile.save()
        return user
