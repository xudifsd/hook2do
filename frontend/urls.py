from django.conf.urls import patterns, include, url

from .views import home, signup

urlpatterns = patterns(
    '',
    url(r'^$', home),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^signup/', signup, name='signup'),
)
