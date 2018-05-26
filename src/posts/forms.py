from django import forms

from .models import Post

#
# def validate_content_word_count(value):
#     count = len(value.split())
#     if count < 10:
#         raise forms.ValidationError(('Please provide at least a 10 word message, %(count)s words is not descriptive enough'),
#                                     params={'count':count},)

class PostForm(forms.ModelForm):
    # title = forms.CharField(label='Title')
    # content = forms.CharField(label='content')
    #
    # content = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #         'class': 'materialize-textarea',
    #         'placeholder': 'write a content ...',
    #     }
    # ))


    # image = forms.CharField(widget=forms.FileInput(
    #     attrs = {
    #         'class':'file-field input-field',
    #     }
    # ))



    class Meta:
        model = Post
        fields=['title','content','image',]
        widgets={
            'title': forms.TextInput(attrs={'class':'validate','placeholder':'title'}),
            'content':forms.Textarea(attrs={'class':'materialize-textarea','id':'textarea1'}),


        }
