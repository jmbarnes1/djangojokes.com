from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')), #must come before admin/
    path('admin/', admin.site.urls),

    # User Managment
    # for paths that begin with /account/, Django will first check users.urls for matching paths. 
    # If it doesn’t find a match there, it will check allauth.urls.
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),

    # Local Apps
    path('jobs/', include('jobs.urls')),
    path('jokes/', include('jokes.urls')),
    path('', include('pages.urls')),  
]
