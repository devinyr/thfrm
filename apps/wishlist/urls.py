from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from apps.wishlist import views

urlpatterns = [
    url(r'^dashboard/$', login_required(views.Dashboard.as_view(),login_url='/accounts/login'),name='wishlist-dashboard'),
]
