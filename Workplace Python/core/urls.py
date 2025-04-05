from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # URLs do app tasks
    path('accounts/', include('allauth.urls')),  # URLs do allauth
]