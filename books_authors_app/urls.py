from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('process_books', views.process_books),
    path('book_detail/<int:val>', views.book_detail),
    path('add_author/', views.add_author ),
    path('authors/', views.authors),
    path('process_authors', views.process_authors),
    path('author_detail/<int:val>', views.author_detail),
    path('add_book/',views.add_book)
]
