from django.contrib import admin
from django.urls import path, include
from django.conf import settings # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
