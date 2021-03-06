"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books, name='books'),
    path('books/new/', views.new_book, name='new-book'),
    path('books/<int:pk>', views.books_detail, name="books-detail"),
    path('books/edit/<int:pk>', views.edit_book, name='edit-book'),
    path('books/delete/<int:pk>', views.delete_book, name='delete-book'),
    path('books/<slug:slug>/', views.books_by_category, name="books-by-category"),
    path('books/favorites/user', views.get_favorite_books_for_user,
         name="books-by-favorites"),
    path('books/edit/', views.edit_book, name='edit-book'),
    path('accounts/', include('registration.backends.default.urls')),
]
