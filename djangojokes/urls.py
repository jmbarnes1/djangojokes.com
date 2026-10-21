from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')), #must come before admin/
    path('admin/', admin.site.urls),

    # User Managment
    path('account/', include('allauth.urls')),

    # Local Apps
    path('jobs/', include('jobs.urls')),
    path('jokes/', include('jokes.urls')),
    path('', include('pages.urls')),  
]
