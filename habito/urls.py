from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from habito_app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^edit-profile/$', views.edit_profile, name='edit-profile'),
	url(r'^habits/$', views.habits, name='habits'),
	url(r'^habit/(?P<habit_title_slug>[\w\-]+)/$', views.show_habit, name='habit'),
	url(r'^admin/', admin.site.urls),
	
	# AJAX URLS
	url(r'^habits/update_habit/toogle_day/$', views.toogle_day, name='toogle_day'),
	url(r'^habits/update_habit/edit_title/$', views.edit_title, name='edit_title'),
	url(r'^habits/update_habit/set_today/$', views.set_today, name='set_today'),
]
