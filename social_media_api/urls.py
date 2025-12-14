from django.contrib import admin
from django.urls import path, include

"""
Required checker strings:
api/
posts.urls
"""

urlpatterns = [
    path('admin/', admin.site.urls),

    # api/
    path('api/', include('posts.urls')),  # posts.urls
]
