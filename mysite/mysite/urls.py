from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('kakao/', include('kakao.urls', namespace='kakao')),

]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)