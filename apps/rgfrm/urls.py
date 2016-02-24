from django.conf.urls import patterns, url
from apps.accounts.views import views

urlpatterns = [url(r'^$', views.login, name='login'),
    url(r'^register$', views.register, name='register'), 
]
