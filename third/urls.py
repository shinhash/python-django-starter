from django.urls import path
from . import views

urlpatterns = [
    path('list/page/<int:page_num>/', views.list, name="restaurant-list"),
    path('create/', views.create, name="restaurant-create"),
    path('update/<int:restaurant_id>/', views.update, name="restaurant-update"),
    # path('detail/', views.detail, name="restaurant-detail"),
    path('restaurant/<int:restaurant_id>/delete/', views.delete, name="restaurant-delete"),

    path('restaurant/<int:restaurant_id>/', views.detail, name="restaurant-detail"),
    path('restaurant/<int:restaurant_id>/review/create/', views.review_create, name="review-create"),
    path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>/', views.review_delete, name="review-delete"),
    path('review/list/', views.review_list, name="review-list"),


    path('api/restaurant/create/', views.api_rest_create, name="api-restaurant-create"),
    path('api/restaurant/delete/', views.api_rest_delete, name="api-restaurant-delete"),
    path('api/restaurant/update/', views.api_rest_update, name="api-restaurant-update"),
]