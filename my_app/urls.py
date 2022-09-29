from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

app_name = "my_app"
# router = SimpleRouter()
router = DefaultRouter()
router.register('books', views.BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path("", views.index, name="index"),
    # path("redirect/", views.redirect),
    # path("about/", views.about, name="about"),
    # path("book_details/<int:pk>/", views.book_details, name="book_details"),
    # path("book-list/", views.book_list, name="book_list")

    # path("books/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    # path("books/", views.BookList.as_view(), name="book_list"),
    # path("publishers/<int:pk>/", views.PublisherDetail.as_view(), name="publisher_detail"),
    # path("publishers/", views.PublisherList.as_view(), name="publisher_list")

]