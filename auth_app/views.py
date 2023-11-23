from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('eruna:home'))

        messages.add_message(request, messages.ERROR, 'Account not Found.')
        return render(request, self.template_name)

class RegisterView(View):
    template_name = 'account/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm-password', '')

        if password == confirm_password:
            if not User.objects.filter(username = username):
                user = User.objects.create_user(username, email, password)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Account created successfully. Please Sign in.')
                return redirect(reverse('auth_app:login'))

            else:
                messages.add_message(request, messages.ERROR, 'Username entered not available.')
            
        else:
            messages.add_message(request, messages.ERROR, 'Passwords entered do not match.')

        return render(request, self.template_name)


def logout(request):
    auth.logout(request)
    return redirect(reverse('auth_app:login'))
