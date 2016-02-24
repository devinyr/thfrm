from django.contrib.auth import forms
from django.shorcuts import render, redirect
from django.views.generic import View

class Register(View):
    form = forms.UserCreationForm
    def get(self, request):
        context = {'form' : self.form()}
        return render(request, 'account/register.html', context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/success')
        else:
            context = {'form' : form}
            return render(request,'accounts/register.html', context)