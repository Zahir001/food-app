from . import views
from django.urls import path
from django.views.decorators.cache import cache_page

app_name='myapp'

urlpatterns = [
  # #URL patterns of api
  # path("items-json",views.item_list_json,name='item_list_json'),#NORMAL PYTHON

  #URL pattern of API built with DRF
  path('api/items/',views.ItemListAPIView.as_view(),name='item-list-api'),
  #URL Pattern for single item with DRF
  path('api/items/<int:pk>/',views.ItemDetailAPIView.as_view(),name='item-detail-api'),
  #url pattern of django app
  # path('',cache_page(60*15) (views.index),name='index'),
  path('',(views.index),name='index'),
  # path('<int:id>/',views.detail,name='detail'), this works in FunctionBasedViews
  path('<int:id>/',views.detail,name='detail'),
  path('add/',views.create_item,name='create_item'),
  path('update/<int:pk>',views.ItemUpdateView.as_view(),name='update_item'),
  path('delete/<int:pk>',views.ItemDeleteView.as_view(),name='delete_item'),
]
