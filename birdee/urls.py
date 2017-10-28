"""birdee URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from frontend.views import MainView, AccountRegisterView

urlpatterns = [
    url(r'^$', MainView.as_view(), name='index'),
    url(r'^status/', include('status.urls', namespace='status')),
    url(r'^social/', include('social_django.urls', namespace='social')),
    url(r'^avatar/', include('avatar.urls', namespace='avatar')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^account/register/$', AccountRegisterView.as_view(), name='account-register'),

    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', serve, name='static', kwargs={'document_root': settings.STATIC_ROOT}),
]
