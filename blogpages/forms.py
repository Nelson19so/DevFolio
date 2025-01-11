from django import forms
from .models import Contact, Testimonial

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ("username",
               "email",
                 "subject",
                   "message")
  
class TestimonialForm(forms.ModelForm):
  class Meta:
    model = Testimonial
    fields = ("username",
               "email",
                 "work",
                   "testimonial")