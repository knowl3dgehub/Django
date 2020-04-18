from django.conf.urls import url
from django.urls import path
from . import views
from . import models


"""
URL's for API's
"""


urlpatterns = [
    path('admin_login/', views.login_view, name='admin_login'),
    url(r'^dashboard/', views.DashboardListView.as_view(), name='dashboard'),
    path('create_admin/', views.AdminCreateView.as_view(), name='create_admin'),
    path('list_admin/', views.AdminListView.as_view(), name='list_admin'),
    url(r'^details_admin/(?P<pk>\d+)/$', views.AdminDetailView.as_view(), name='details_admin'),
    url(r'^update_admin/(?P<pk>\d+)/$', views.AdminUpdateView.as_view(), name='update_admin'),
    url(r'^delete_admin/(?P<pk>\d+)/$', views.AdminDeleteView.as_view(), name='delete_admin'),
    ]