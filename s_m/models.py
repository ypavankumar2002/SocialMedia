from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User_post(models.Model):
#     title = models.TextField(max_length=40)
#     # image = models.ImageField(upload_to='media/images/', blank=True, null=True)
#     # video = models.FileField(upload_to='media/videos/', blank=True, null=True)
#     image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.title

class Media(models.Model):
    title = models.TextField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    user = models.ForeignKey(User,related_name='media',  on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return self.title
    

