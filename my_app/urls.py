from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    # path("", views.index, name="index"),
    # path("redirect/", views.redirect),
    # path("about/", views.about, name="about"),
    # path("book_details/<int:pk>/", views.book_details, name="book_details"),
    # path("book-list/", views.book_list, name="book_list")

    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("books/", views.book_list, name="book_list"),
    path("publishers/<int:pk>/", views.publisher_detail, name="publisher_detail"),
    path("publishers/", views.publisher_list, name="publisher_list")

]