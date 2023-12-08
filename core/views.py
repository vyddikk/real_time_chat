from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, HttpResponseRedirect

from .forms import SingUpForm


def frontpage(request):
    return render(request, 'core/frontpage.html')


def singup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SingUpForm()

    return render(request, 'core/singup.html', {'form': form})


def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


