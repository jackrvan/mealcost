from django.urls import path

from . import views

app_name = 'cupboard'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.add_item, name='add_item'),
    path('create/submit', views.add_item_form, name='add_item_form'),
    # /cupboard/detail/flour/
    path('detail/<str:item_name>/', views.item_detail, name='detail'),
]
