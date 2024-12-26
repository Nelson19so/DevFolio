from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('service-details/', views.services_page, name="service-page"),
    path('testimonial/', views.all_testimonials, name="testimonial")
]