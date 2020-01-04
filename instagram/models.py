from django.db import models
from PIL import Image
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_image = models.ImageField(upload_to='profile_photo/', blank=True, default='profile_photo/shee_love.jpg')
  bio = models.CharField(max_length=50, blank=True)
  
  def __str__(self):
    return f'{self.user.username} Profile'
  
  def save_profile(self):
    self.save()
    
  def update_profile(self):
    self.update_profile()
    
  def delete_profile(self):
    self.delete_profile()
    
@classmethod
def get_by_id(cls, id):
  user_images = Profile.objects.filter(user=id).first()
  return user_images