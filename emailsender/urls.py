from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('mailer.urls')),
    path('admin/', admin.site.urls),
]
