from django.contrib.auth import login, authenticate, forms, logout
from django.shortcuts import render, redirect
from django.views.generic import View

class Dashboard(View):
    template = 'wishlist/dashboard.html'
    user = ''
    context = {'templateData' : user}
    def get(self, request):
        return render(request, self.template, self.context)

