from django.contrib import admin
from django.urls import path
from app.views import home,MessageView,TestimonialView

urlpatterns = [
    
    path('', home, name='home'),
    
    path('message/',MessageView, name='message'),
    path('testimonial/',TestimonialView, name='testimonial'),
]
