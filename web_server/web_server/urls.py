"""web_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/upload/$', views.upload, name='upload'),
    url(r'^api/create_album/$', views.create_album, name='create_album'),
    url(r'^api/get_album/$', views.get_album, name='get_album'),
    url(r'^api/get_album_info/$', views.get_album_info, name='get_album_info'),
    url(r'^api/get_picture/$', views.get_picture, name='get_picture'),
    url(r'^api/get_media/$', views.get_media, name='get_media'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
