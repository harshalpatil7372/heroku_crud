from .import views
from django.urls import path

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book_create', views.book_create, name='book_create'),
    path('book_detail/<int:pk>', views.book_detail, name='book_detail'),
    path('book_update/<int:pk>', views.book_update, name='book_update'),
    path('book_delete/<int:pk>', views.book_delete, name='book_delete'),
]
