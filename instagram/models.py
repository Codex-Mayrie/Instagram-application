from django.db import models
from PIL import Image
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_image = models.ImageField(upload_to='profile_photo/')
  bio = models.TextField(max_length=255)
  
  def __str__(self):
    """
    method that returns the profile
    """
    return f'{self.user.username} Profile'
  
  def save_profile(self):
    """
    A method that saves the profile
    """
    self.save()
    
  def update_profile(self):
    """
    A method that updates the profile
    """
    self.update_profile()
    
  def delete_profile(self):
    """
    A method that deletes the profile
    """
    self.delete_profile()
    
@classmethod
def get_by_id(cls, id):
  """
  A method that gets the user image by id
  """
  user_images = Profile.objects.filter(user=id).first()
  return user_images

class Image(models.Model):
  image = models.ImageField(upload_to='picture_folder/')
  image_name = models.CharField(max_length=25)
  image_caption = models.CharField(max_length=400, blank=True)
  post_date = models.DateTimeField(auto_now_add=True)
  image_likes = models.IntegerField(default=0)
  author = models.ForeignKey(User,on_delete=models.CASCADE, default='1')
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE, default='1')
  
  def save_image(self):
    self.save()
  
  def __str__(self):
    return f'{self.profile.user.username}'
  
  @classmethod
  def get_image(request, id):
    try:
      image = Image.objects.get(pk=id)
    except ObjectDoesNotExist:
      raise Http404()
    return image
  
  @classmethod
  def get_author(cls, search_term):
    image = cls.objects.filter(author__username__icontains=search_term)
    return image
  
  class Meta:
    ordering = ['-post_date']
    
  def update_image(self):
    self.update_image()
  
  def update_caption(self, caption):
    self.image_caption = caption
    self.save()
    
  def delete_image(self):
    self.delete()
    
  @classmethod
  def get_images(cls):
    images = cls.objects.all()
    return images
  
  @classmethod
  def get_profile_images(cls, profile):
    user_images = Image.objects.filter(profile__id=profile)
    return user_images
  
class Comment(models.Model):
  comment = models.CharField(max_length=400)
  date = models.DateTimeField(auto_now_add=True)
  total_comments = models.IntegerField(default=0)
  author = models.ForeignKey(User,on_delete=models.CASCADE,default='1')
  image = models.ForeignKey(Image, on_delete=models.CASCADE, default='picture_folder/chipeenss.jpg')
  
  def __str__(self):
    return f'{self.username}'
  
  class Meta:
    ordering = ['-date']
    
  @classmethod
  def get_all_comments(cls):
    comments = Comment.objects.all()
    return comments