
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
                path('admin/', admin.site.urls),
                path('', include('django.contrib.auth.urls')),
                url(r'^api-auth/', include('rest_framework.urls')),
                path('', include('users.urls')),
              ]
