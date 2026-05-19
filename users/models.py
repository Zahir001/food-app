from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  image = models.ImageField(default='profilepic.jpg',upload_to='profile_pic')
  location = models.CharField(max_length=200)

  def __str__(self):
    return self.user.username
  
# User <-> Profile

# logged in 'user' instance hai 'User' model ka aur     
# profile model one to one connected ho gya User se 
# isiliye user instance se ham access kr sakte hai user.profile.image ya location


# ForeignKey jis model ko point karta hai, wo parent hota hai.
# 👉 CASCADE me parent delete hone par child bhi delete ho jaata hai ✔🔥