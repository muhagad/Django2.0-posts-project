from django import forms
from django.core.validators import validate_email
from django.core import validators
from .validators import validate_domain_email_only
from .models import LoginApp

class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    # email = forms.EmailField(validators=[validate_domain_email_only])

    username.widget.attrs.update({'class':'form-control','placeholder':'username'})
    password.widget.attrs.update({'class':'form-control','placeholder':'password'})
    # email.widget.attrs.update({'class':'form-control','placeholder':'E-mail'})


    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder':'username'})
    #     self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'password'})
    #     self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'E-mail'})
    # # field level validation
    # def clean_email(self):
    #     #validate here or normalize the data
    #     email_passed = self.cleaned_data['email']
    #     email_req = "yourdomain.com"
    #     if email_req not in email_passed:
    #         raise forms.ValidationError("Not a valid Email!")
    #     return email_passed


    # def clean(self):
    #     cleaned_data = super(LoginForm, self).clean()
    #     email_passed = self.cleaned_data.get("email")
    #     email_req = "yourdomain.com"
    #     if email_req not in email_passed:
    #         raise forms.ValidationError("Not a valid Email")
    #     return email_passed



    class Meta:
        model = LoginApp
        fields=["username","password"]


class regForm(forms.Form):
    username = forms.CharField()
    email=forms.EmailField(validators=[validate_domain_email_only])
    
