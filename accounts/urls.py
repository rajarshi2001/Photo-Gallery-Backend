from django.urls import path, include
from . import views
from knox import views as knox_views
urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', views.RegisterApi.as_view()),
    path('api/auth/login', views.LoginApi.as_view()),
    path('api/auth/user', views.UserApi.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name="knox_logout")
]