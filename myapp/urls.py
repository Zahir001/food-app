from . import views
from django.urls import path,include
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView
)
app_name='myapp'

router = DefaultRouter()
router.register(r"items",views.ItemViewSet,basename='item')
router.register(r"orders",views.OrderViewSet,basename='order')

urlpatterns = [
  path("api/token/",TokenObtainPairView.as_view(),name='token_obtain_pair'),
  path("api/token/refresh/",TokenRefreshView.as_view(),name='token_refresh'),
  path("api/",include(router.urls)),

  # #URL patterns of api
  # path("items-json",views.item_list_json,name='item_list_json'),#NORMAL PYTHON

  #URL pattern of API built with DRF
  # path('api/items/',views.ItemListCreateAPI.as_view(),name='item-list-api'),
  #URL Pattern for single item with DRF
  # path('api/items/<int:pk>/',views.ItemRetrieveUpdateDestroyAPIView.as_view(),name='item-detail-api'),
  #url pattern of django app
  # path('',cache_page(60*15) (views.index),name='index'),
  path('',(views.index),name='index'),
  # path('<int:id>/',views.detail,name='detail'), this works in FunctionBasedViews
  path('<int:id>/',views.detail,name='detail'),
  path('add/',views.create_item,name='create_item'),
  path('update/<int:pk>',views.ItemUpdateView.as_view(),name='update_item'),
  path('delete/<int:pk>',views.ItemDeleteView.as_view(),name='delete_item'),
]
