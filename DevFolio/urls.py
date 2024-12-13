from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_nelson/', admin.site.urls),
    path('', include('blogpages.urls'))
]
