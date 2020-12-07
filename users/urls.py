from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$',views.index,name="index"),
    url(r'^logins',views.login,name="login"),
    url(r'^registers',views.register, name="register"),
    url(r'^logouts$',views.logout,name="logout")
]