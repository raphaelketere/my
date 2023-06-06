from django.urls import path
from .import views

urlpatterns = [
    path ('',views.signup,name='signup.html'),
    path ('home/',views.home,name='home.html'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('electronics/', views.electronics, name='electronics'),
    path('sports/', views.sports, name='sports'),
 
]