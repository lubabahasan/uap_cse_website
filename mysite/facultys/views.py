from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

from .forms import SignUpForm, ProfileForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {
                'form': form,
                'profile_form': profile_form
            })
    else:
        form = SignUpForm()
        profile_form = ProfileForm()

    return render(request, 'signup.html', {
        'form': form,
        'profile_form': profile_form
    })

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            return redirect('home')
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')



def home(request):
    return render(request, 'home.html')



