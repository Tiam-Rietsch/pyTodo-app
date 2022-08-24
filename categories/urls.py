from django.urls import path 
from .views import CategoryListView, CreateCategoryView, CategoryDetailView, DeleteCategoryView, CategoryUpdateView


urlpatterns = [ 
    path('new/', CreateCategoryView.as_view(), name='create_cat'),
    path('all/', CategoryListView.as_view(), name='cat_list'),
    path('<slug:slug>/edit', CategoryUpdateView.as_view(), name='cat_update'),
    path('<slug:slug>/delete', DeleteCategoryView.as_view(), name='cat_delete'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='cat_detail'),

]