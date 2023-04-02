from django.urls import path
from . import views
from django.contrib.auth.urls import views as auth_view
app_name='account'
urlpatterns=[
    path('login/',auth_view.LoginView.as_view(),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('homepage/',views.homepage,name='homepage'),
    path('signup/',views.sign_up,name='signup'),
]