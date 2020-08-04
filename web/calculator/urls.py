from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('submitquery',views.submitquery,name='submitquery'),
    url(r'^$', views.api_root, name='api_root'),
    url(r'^add/?$', views.add, name='add'),
    url(r'^sub/?$', views.sub, name='sub'),
    url(r'^mul/?$', views.mul, name='mul'),
    url(r'^div/?$', views.div, name='div'),
]
