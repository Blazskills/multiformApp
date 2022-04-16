from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blogapp.urls')),
    path('vueapp', include('vue_app.urls')),
    path('admin/', admin.site.urls),
]