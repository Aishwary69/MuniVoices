from django.shortcuts import render,redirect
from django.contrib.auth import login

from samasya.models import Samasya,Category

from .forms import SignupForm

def index(request):
    samasyas=Samasya.objects.filter(is_solved=False)[0:6]
    categories = Category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories,
        'samasyas':samasyas,
 })


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })