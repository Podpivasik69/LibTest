from django.shortcuts import render, redirect
from django.contrib import messages
from auth_user.forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'users/profile.html')

def logout_view(request):
    logout(request)
    return render(request , template_name='users/logout.html')