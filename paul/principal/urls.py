from django.conf.urls import url

from paul.principal.views import home, contact, about

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^contato/$', contact, name='contact'),
	url(r'^sobre/$', about, name='sobre'),
]