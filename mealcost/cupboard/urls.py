from django.urls import path

from . import views

app_name = 'cupboard'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.ItemAddView.as_view(), name='add_item'),
    # /cupboard/detail/flour/
    path('detail/<str:item_name>/', views.item_detail, name='detail'),
]