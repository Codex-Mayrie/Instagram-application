from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def registration(request):
  if request.method == 'POST'
  form = RegistrationForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('/login')
else:
  form = RegisterForm()
return render(request, 'registration/sign-up.html', {"form": form})