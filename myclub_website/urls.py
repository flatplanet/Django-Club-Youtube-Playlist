from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
]

# Configure Admin Titles
admin.site.site_header = "My Club Administration Page"
admin.site.site_title = "Browser Title"
admin.site.index_title = "Welcome To The Addmin Area..."