from django.db import models
from django.utils import timezone
import os
from uuid import uuid4
from django.contrib.auth.models import User
# User._meta.get_field('email')._unique = True



def path_and_rename(instance, filename):        #used for renaming image
    upload_to = 'images'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Image(models.Model):
    
    image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    caption_1 = models.TextField(max_length=30,null=True,blank=False)
    caption_2 = models.TextField(max_length=30,null=True,blank=False)
    caption_3 = models.TextField(max_length=30,null=True,blank=False)
    caption_4 = models.TextField(max_length=30,null=True,blank=False)
    caption_5 = models.TextField(max_length=30,null=True,blank=False)
    


#     # def __str__(self):
#     #     return self.title