from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.AboutUsView.as_view(), name='aboutus'),
    path('cleaning/', views.CleaningView.as_view(), name='cleaning'),
    path('donate/', views.DonateView.as_view(), name='donate'),
]