from django.urls import path

from . import views

app_name = 'recipe'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.add_recipe, name='add_recipe'),
    path('createfromurl/', views.add_recipe_from_url, name='add_recipe_from_url'),
    # path('create/submit', views.add_recipe_form, name='add_recipe_form'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.RecipeDelete.as_view(), name='delete_recipe'),
]
