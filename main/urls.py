from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views

app_name = "main"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'signup/$', views.signup, name="signup"),
    url(r'login/$', views.login, name="login"),
    url(r'demo/$', views.demo, name="demo"),
]
