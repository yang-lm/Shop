from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^listS',views.list,name="list"),#商品列表
    url(r'^list/(P<page>[0-9]+)$',views.list,name="list"),#商品列表展示
    url(r'^detail/(?P<gid>[0-9]+)&',views.detail,name="detail")#商品详情
]
