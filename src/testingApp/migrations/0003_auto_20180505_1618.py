# Generated by Django 2.0.4 on 2018-05-05 14:18

from django.db import migrations, models
import testingApp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('testingApp', '0002_loginapp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginapp',
            name='email',
            field=models.EmailField(max_length=254, null=True, validators=[testingApp.validators.validate_domain_email_only]),
        ),
    ]
