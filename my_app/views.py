import http

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Publisher
from .serializers import BookSerializer, PublisherSerializer

# Create your views here.
from my_app.models import Book


# from django.db import connection


# def index(request):
#     context = [1, 2, 5]
#     text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
#            "dolore magna aliqua."
#     return render(request, "my_app/index.html", context={"obj": context,
#                                                          "name": "Wale", "is_major": False, "text": text})
#
#
# def redirect(request):
#     return HttpResponseRedirect(reverse("my_app:index"))


# def about(request):
#     return render(request, "my_app/about.html")
#
#
# def book_details(request,pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, "my_app/book_details.html", {"book": book})


# def book_list(request):
# books = Book.objects.all()
# books = Book.objects.filter(genre="FICTION")
# books = Book.objects.filter(price=39888.80)
# books = Book.objects.filter(title__contains="and")
# Book.objects.select_related('publisher').all()
# books = Book.objects.raw("select * from my_app_book")

# books = Book.objects.filter(publisher__id__in=(1,4,6)).order_by('title')
# return render(request, "my_app/book-list.html", {"books":list(books)})

@api_view(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        querySet = Book.objects.all()
        serializer = BookSerializer(querySet, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method in ("PUT", "PATCH"):
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "GET":
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    elif request.method in ("PUT", "PATCH"):
        serializer = PublisherSerializer(publisher, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "DELETE":
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def publisher_list(request):
    if request.method == "GET":
        querySet = Publisher.objects.all()
        serializer = PublisherSerializer(querySet, many=True, context={"request":request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
