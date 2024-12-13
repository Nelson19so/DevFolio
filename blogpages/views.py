from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_page(request):
    return render(request, 'blogpages/index.html')

def portfolio_details(request):
    return render(request, 'blogpages/portfolio-details.html')

def services_page(request):
    return render(request, 'blogpages/service-details.html')

def all_testimonials(request):
    return render(request, 'blogpages/all-testimonials.html')