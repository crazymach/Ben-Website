from django.conf.urls import url

form . import views


urlpatters = [
	url(r'^$', views.index, name = 'index')

]