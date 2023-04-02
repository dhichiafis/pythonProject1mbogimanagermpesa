from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
@login_required()
def homepage(request):
    return redirect(reverse('mypesa:lipa_na_mpesa'))

def sign_up(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        form=SignupForm()
    return render(request,'account/signup.html',{'form':form})