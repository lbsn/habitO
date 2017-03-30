from django.conf.urls import url
from habito_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user', views.show_user, name='user'),
    # url(r'^habit/', views.about, name='habit'),

    
    url(r'^add_habit/$', views.add_habit, name='add_habit'),
    
]
