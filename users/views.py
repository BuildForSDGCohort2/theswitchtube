from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


# Create your views here.
def register(request):
    form2 = RegistrationForm()
    form2.order_fields(field_order=['username', 'email', 'first_name', 'last_name', 'password1', 'password2'])
    # Register a new user
    if request.method != "POST":
        # Display Blank Registration Form
        form = RegistrationForm()
    else:
        # Process completed Form
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log user in and the redirect to homepage
            login(request, new_user)
            return redirect('theswitch:home')
    #  Display a blank or completed form
    content = {'form': form, 'form2': form2}
    return render(request, 'registration/register.html', content)


