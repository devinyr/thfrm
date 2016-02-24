from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from apps.accounts import views

urlpatterns = patterns('',
    url(r'^login/$', views.Login.as_view(), name='accounts-login'),
    url(r'^register/$', views.Register.as_view(), name='accounts-register'),
    url(r'^success/$', login_required(views.Success.as_view(),login_url='/accounts/login'), name='accounts-success'),
)