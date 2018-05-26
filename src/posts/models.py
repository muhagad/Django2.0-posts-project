
from django.db import models

from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.


def upload_location(instance,filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id,instance.id, extension)
    return "%s%s" %(instance.id,filename)

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug  = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return self.title


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        # return '/posts/%s/' %(self.id)
        return reverse('posts:detail',args=[self.id])


    class Meta:
        ordering = ["-timestamp", "-updated"]

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exist()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Post)