from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    full_name = forms.CharField(max_length=100, required=True, label='Full Name')

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

