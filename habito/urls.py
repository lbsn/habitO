"""habito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include
from habito_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^habito_app/', include('habito_app.urls')),
    # above maps any URLs starting
    # with habito_app/ to be handled by
    # the habito_app application
    #url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
	
	# AJAX URLS
	 url(r'^habits/update_habit/toogle_day/$', views.toogle_day, name='toogle_day'),
	 url(r'^habits/update_habit/edit_title/$', views.edit_title, name='edit_title'),
	 url(r'^habits/update_habit/set_today/$', views.set_today, name='set_today'),
]