from django.urls import path
from . import views


app_name = 'clothes'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:cloth_pk>/', views.detail, name='detail'),
    path('<int:cloth_pk>/delete/', views.delete, name='delete'),
    path('<int:cloth_pk>/update/', views.update, name='update'),
    path('search/', views.search, name='search'),
    # path('tags/<int:tag_pk>/', views.tagged_clothes, name='tagged_clothes'),
    path('<int:cloth_pk>/likes/', views.likes, name='likes'),
    path('category/<str:subject>/', views.category, name='category'),
    path('recommend_create/', views.recommend_create, name='recommend_create'),
    path('recommend_detail/<int:recommend_pk>/', views.recommend_detail, name='recommend_detail'),
    path('recommend_delete/<int:recommend_pk>/', views.recommend_delete, name='recommend_delete'),
    path('recommend_update/<int:recommend_pk>/', views.recommend_update, name='recommend_update'),
    path('recommend_detail/<int:recommend_pk>/comments/', views.comments_create, name='comments_create'),
    path('recommend_detail/<int:recommend_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('recommend_detail/<int:recommend_pk>', views.recommend_detail, name='recommend_detail'),
    path('<int:recommend_pk>/delete/', views.recommend_delete, name='recommend_delete'),
    path('shop/', views.shop, name='shop'),
]