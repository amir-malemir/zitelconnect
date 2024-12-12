from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/aboutus.html'

class DrinksView(TemplateView):
    template_name = 'pages/drinks.html'

class CleaningView(TemplateView):
    template_name = 'pages/cleaning.html'

class DonateView(TemplateView):
    template_name = 'pages/donate.html'