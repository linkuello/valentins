from django.contrib import admin
from django.urls import path, include  # добавляем include для включения URL-адресов из других приложений

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('valentines_app.urls')),
    path('about/', include('about_me.urls')),
]
