from django.urls import path

from . import views

app_name = 'recipe'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.add_recipe, name='add_recipe'),
    path('create/submit', views.add_recipe_form, name='add_recipe_form'),
    path('detail/<str:recipe_name>', views.recipe_details, name='detail'),
]
