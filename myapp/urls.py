from . import views
from django.urls import path
from django.views.decorators.cache import cache_page

app_name='myapp'

urlpatterns = [
  # path('',cache_page(60*15) (views.index),name='index'),
  path('',(views.index),name='index'),
  # path('<int:id>/',views.detail,name='detail'), this works in FunctionBasedViews
  path('<int:id>/',views.detail,name='detail'),
  path('add/',views.ItemCreateView.as_view(),name='create_item'),
  path('update/<int:pk>',views.ItemUpdateView.as_view(),name='update_item'),
  path('delete/<int:pk>',views.ItemDeleteView.as_view(),name='delete_item'),
]