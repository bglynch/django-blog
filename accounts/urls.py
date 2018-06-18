# accounts url.py

from django.urls import path
from .views import login, register, logout, profile
# from django.core.urlresolvers import reverse_lazy
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile'),
    # url(r'^password-reset/$', password_reset,
    # {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    # url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    # url(r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
    # {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    # url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete')
]
