from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        # Instantiate with the post
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # This will automatically save the new user
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('blog-home')
    else:
        # Instantiate an empty form
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
