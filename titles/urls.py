from django.conf.urls import include, url,patterns
from titles import views

urlpatterns=patterns('',url('^index/$',views.index,name="index"))