from django.conf.urls import include, url
from . import views

app_name = "superadmin"
urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'index/$', views.login, name="login"),
    url(r'logout/$', views.logout, name="logout"),
]
