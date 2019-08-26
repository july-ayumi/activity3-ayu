from django.urls import path
from django.conf.urls import url
from .import views

app_name = 'employee'

urlpatterns = [
    path('list/', views.IndexView.as_view(), name = 'index'),
    path('post/', views.post_new, name='post'),
    path('', views.login, name='login'),
    path('detail/', views.detail, name='detail'),
]
