from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('login_system:main_menu')
        return render(request, 'login_system/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_system:main_menu')
        return render(request, 'login_system/login.html', {'error': 'Invalid credentials'})


@login_required
def main_menu_view(request):
    return render(request, 'login_system/main_menu.html')


def logout_view(request):
    logout(request)
    return redirect('login_system:login')