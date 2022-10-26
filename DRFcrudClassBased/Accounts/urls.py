from Accounts import views
from django.urls import path


urlpatterns = [

    path('', views.UserRegastationClassBasedAPI.as_view()),
    path('<int:pk>/', views.UserRegastationClassBasedAPI.as_view()),

]