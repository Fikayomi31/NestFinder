from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    return HttpResponse("It is working")

def register(request):
    """function to register form"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'customer':
                return redirect('customer_profile')
            elif user.user_type == 'agent':
                return redirect('agent_profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm

    def get_success_url(self):
        if self.request.user.user_type == 'customer':
            return reverse_lazy('customer_profile')
        elif self.request.user.user_type == 'agent':
            return super().get_success_url()
        return super().get_sucess_url()
    

@login_required
def customer_profile(request):
    return render(request, 'customer_profile.html')

@login_required
def agent_profile(request):
    return render(request, 'agent_profile.html')
