from django.db import models
from django.urls import reverse
from .validators import validate_domain_email_only
# Create your models here.
class LoginApp(models.Model):

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(null = True, validators=[validate_domain_email_only])


    def __str__(self):
        return self.username


    def __unicode__(self):
        return self.username


    def get_absolute_url(self):
        return reverse('success')
