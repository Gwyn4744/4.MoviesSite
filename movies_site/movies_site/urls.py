"""movies_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Auth
    path('signup/', views.SignUpView.as_view(), name='signupview'),
    path('login/', auth_views.LoginView.as_view(), name='loginview'),
    path('logout/', auth_views.LogoutView.as_view(), name='logoutview'),

    # Hall
    path('halloffame/create/', views.CreateHall.as_view(), name='crate_hall'),
    path('halloffame/<int:pk>/', views.DetailHall.as_view(), name='detail_hall'),
    path('halloffame/<int:pk>/update/', views.UpdateHall.as_view(), name='update_hall'),
    path('halloffame/<int:pk>/delete/', views.DeleteHall.as_view(), name='delete_hall'),

    # Video
    path('halloffame/<int:pk>/addvideo/', views.add_video, name='add_video'),
    path('video/search/', views.video_search, name='video_search'),
    path('video/<int:pk>/delete/', views.DeleteVideo.as_view(), name='delete_video'),
]