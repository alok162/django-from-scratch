from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^users/$', views.user_list),
]
