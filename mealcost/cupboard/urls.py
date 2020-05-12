from django.urls import path

from . import views

app_name = 'cupboard'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.add_item, name='add_item'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
