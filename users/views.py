from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import RegistrationForm, ProfilePicForm, EdithProfileForm
from .models import ProfilePic, User


# Create your views here.
def register(request):
    form_arrange = RegistrationForm()
    form_arrange.order_fields(field_order=['username', 'email', 'first_name', 'last_name', 'password1', 'password2'])

    # Register a new user
    if request.method != "POST":
        # Display Blank Registration Form
        form1 = RegistrationForm()

    else:
        # Process completed Form
        form1 = RegistrationForm(request.POST)

        if form1.is_valid():
            new_user = form1.save()

            # Log user in and the redirect to homepage
            login(request, new_user)

            return redirect('users:register2')

    #  Display a blank or completed form
    content = {'form_arrange': form_arrange, 'form1': form1}
    return render(request, 'registration/register.html', content)


@login_required
def edith_profile(request, profile_id):
    userprofile = ProfilePic.objects.get(id=profile_id)
    if request.method != 'POST':

        profile_form = ProfilePicForm(instance=userprofile)

    else:

        profile_form = ProfilePicForm(request.POST, request.FILES, instance=userprofile)
        if profile_form.is_valid():
            edith = profile_form.save(commit=False)
            edith.user = request.user
            profile_form.save()

            return redirect('theswitch:profile')

    content = {'form': profile_form}
    return render(request, 'registration/edith_profilepic.html', content)


@login_required
def profilepic(request):

    form1_arrange = ProfilePicForm()
    form1_arrange.order_fields(field_order=['bio', 'profile_image'])
    # Register a new user
    if request.method != "POST":
        # Display Blank Registration Form
        form = ProfilePicForm()

    else:
        # Process completed Form
        form = ProfilePicForm(request.POST, request.FILES)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.user = request.user
            new_user.save()

            return redirect('theswitch:home')

    #  Display a blank or completed form
    content = {'form': form, 'form_set': form1_arrange}
    return render(request, 'registration/register_extend.html', content)


@login_required
def edith_profile_page(request, user_id):
    userprofile = User.objects.get(id=user_id)
    if request.method != 'POST':

        profile_form = EdithProfileForm(instance=userprofile)

    else:

        profile_form = EdithProfileForm(request.POST, request.FILES, instance=userprofile)
        if profile_form.is_valid():
            edith = profile_form.save(commit=False)
            edith.user = request.user
            profile_form.save()

            return redirect('theswitch:profile')

    content = {'form': profile_form}
    return render(request, 'registration/edith_main_profile.html', content)




