from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            # ratings = user.rater.rating_set.all().order_by('-stars')
            return redirect(reverse('user_detail', args=[user.rater.pk]))
        else:
            return render(request,
                          'lensview/user_login.html',
                          {'error_message': "ERROR LOGGING IN!",
                           'username': username})
    else:
        return render(request, 'lensview/user_login.html')


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = user_form.save()
            password = user_form['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Your account was successfully created.')
            return redirect('home')
    else:
        form = UserForm()
    return render(request,
                  'lensview/user_register.html',
                  {'form': form})


def user_logout(request):
    if request.user.is_authenticated():
        user_name = request.user.username
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                             "You have successfully logged out")
        return render(request,
                      'lensview/user_logout.html',
                      {'user_name': user_name})
    else:
        return redirect('/')
