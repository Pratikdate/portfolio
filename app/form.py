from django import forms
from .models import Messages,Testimonials

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'subject','message']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ['short_intro', 'image', 'roal','email','name']

    