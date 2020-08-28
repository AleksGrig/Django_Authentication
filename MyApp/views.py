from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .form import LoginForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, 
                username = cd['username'],
                password = cd['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponse('Authentication successful')
            else:
                return HttpResponse('Authentication failed')
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })