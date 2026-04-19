<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    
    path('', include('game.urls')),
]


=======
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    
    path('', include('game.urls')),
]


>>>>>>> 8ada485e1e7684880b2e8dfde05d8b4234635a24
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)