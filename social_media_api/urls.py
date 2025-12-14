from django.contrib import admin
from django.urls import path, include

# api/
# posts.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
]
