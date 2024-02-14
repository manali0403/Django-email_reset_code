from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout


from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError

# Create your views here.

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_url')
    template_name = 'authapp/register.html'
    context = {'form':form}
    return render(request,template_name,context)


def login_view(request):
    template_name = 'authapp/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un ,password = pw)

        if user is not None:
            login(request,user)
            return redirect('show_url')

    return render(request,template_name,context)


def logout_view(request):
    logout(request)
    return redirect('signup_url')

 

from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib import messages

def reset_password_form_view(request):
    try:
        form = PasswordResetForm()

        if request.method == 'POST':
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                # Save the form to generate a token but don't send the email just yet
                user = form.save(commit=False)

                # Additional logic to set/reset user's email as needed
                user.email = form.cleaned_data['email']

                # Generate the reset token and save the user instance
                user.save()

                # Now send the password reset email
                send_password_reset_email(request, user.email, user.reset_token)

                # Provide a success message to the user
                messages.success(request, 'Password reset email sent successfully.')
                return redirect('show_url')

        template_name = 'authapp/email.html'
        context = {'form': form}
        return render(request, template_name, context)

    except ValidationError as e:
        # Handle form validation errors here
        # You can customize this based on your needs
        messages.error(request, str(e))
        return render(request, 'authapp/error.html', {'error_message': str(e)})

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {str(e)}")

        # Return a generic error response to the user
        messages.error(request, 'An unexpected error occurred. Please try again later.')
        return redirect('show_url')  # Redirect to an appropriate page after an error

def send_password_reset_email(request, email, reset_token):
    try:
        # Check if the request has a valid host
        domain = request.get_host() if request.get_host() else 'example.com'

        # Use the obtained domain to construct the password reset URL
        reset_url = f'http://{domain}/reset/{reset_token}/'

        # Add your logic here to send the password reset email
        # You might want to use Django's built-in send_mail function or any other email sending mechanism
        # Example: send_mail('Subject', f'Message with reset URL: {reset_url}', 'from@example.com', [email], fail_silently=False)
        pass

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred while sending the password reset email: {str(e)}")
        raise
