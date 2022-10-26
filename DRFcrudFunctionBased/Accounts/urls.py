from Accounts.views import UserRegastationAPI
from django.urls import path


urlpatterns = [
    path('', UserRegastationAPI),
]