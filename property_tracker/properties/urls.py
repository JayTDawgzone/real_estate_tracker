from django.conf.urls import url
from properties import views

urlpatterns = [
    url(r'^$',views.PropertyListView.as_view(),name='property_list'),
    url(r'property/(?P<pk>\d+)$', views.PropertyDetailView.as_view(),name='property_detail'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^property/new/$',views.CreatePropertyView.as_view(),name='property_new'),
    url(r'^property/(?P<pk>\d+)/edit/$',views.PropertyUpdateView.as_view(),name='property_edit'),
    url(r'^property/(?P<pk>\d+)/remove/$',views.PropertyDeleteView.as_view(),name='property_remove'),
    url(r'^unlisted/$',views.DraftListView.as_view(),name='property_unlisted'),
    url(r'^property/(?P<pk>\d+)/publish/$', views.property_publish, name='property_publish'),
    url(r'^api/properties/$', views.get_properties, name='get_properties'),
]
