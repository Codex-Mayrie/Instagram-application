from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect('/login')
  else:
    form = RegisterForm()
    return render(request, 'registration/sign-up.html', {"form": form})

@login_required(login_url='/login')
def index(request):
    title = 'instagram-clone'
    posts = Image.get_images()
    comments = Comment.get_all_comments()
    users = User.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        img_id = request.POST['image_id']
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            image = Image.get_image(img_id)
            comment.image = image
            comment.save()
        return redirect(f'/#{img_id}', )
    else:
        form = CommentForm(auto_id=False)

    param = {
        "title": title,
        "posts": posts,
        "form": form,
        "comments": comments,
        "users": users
    }
    return render(request, 'index.html', param)

@login_required(login_url='/login')
def profile(request):
    pictures = Image.get_images()
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('/profile')
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
    return render(request, 'profile.html', {"user_form": user_form, "profile_form": profile_form, "pictures": pictures})

