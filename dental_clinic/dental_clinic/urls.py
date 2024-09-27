from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("landpage.urls")),
    path('admin/', include("scheduling.urls")),
    path('admin_sys/', admin.site.urls),
]
