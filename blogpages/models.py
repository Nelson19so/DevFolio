from django.db import models

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=300)
    date_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created_at']

    def __str__(self):
        return self.username

class Testimonial(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    work = models.CharField(max_length=50)
    testimonial = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    # profile = models.ImageField(upload_to='testimonial/')

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.username