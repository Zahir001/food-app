from . import views
from django.urls import path

app_name='myapp'

urlpatterns = [
  path('',views.IndexClassView.as_view(),name='index'),
  # path('<int:id>/',views.detail,name='detail'), this works in FunctionBasedViews
  path('<int:pk>/',views.FoodDetailView.as_view(),name='detail'),
  path('add/',views.ItemCreateView.as_view(),name='create_item'),
  path('update/<int:pk>',views.ItemUpdateView.as_view(),name='update_item'),
  path('delete/<int:pk>',views.ItemDeleteView.as_view(),name='delete_item'),
]