from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, PublisherSerializer
from .filter import BookFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from.pagination import BookPagination


# Create your views here.
from my_app.models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'isbn']
    ordering_fields = ['title', 'price']
    ordering = ['title']
    pagination_class = BookPagination

    # def partial_update(self, request, *args, **kwargs):
    #     queryset = Book.objects.all()


# from django.db import connection
# class BookList(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#
#
# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def __delete__(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class PublisherList(ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#
#
# class PublisherDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer

# class PublisherList(APIView):
#     def get(self, request):
#         querySet = Publisher.objects.all()
#         serializer = PublisherSerializer(querySet, many=True, context={"request": request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class PublisherDetail(APIView):
#     def get(self, request, pk):
#         publisher = get_object_or_404(Publisher, pk=pk)
#         serializer = PublisherSerializer(publisher)
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         publisher = get_object_or_404(Publisher, pk=pk)
#         serializer = PublisherSerializer(publisher, data=request.data, optional=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         publisher = get_object_or_404(Publisher, pk=pk)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

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

# @api_view(["GET", "POST"])
# def book_list(request):
#     if request.method == "GET":
#         querySet = Book.objects.all()
#         serializer = BookSerializer(querySet, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#
#
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#     elif request.method in ("PUT", "PATCH"):
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "DELETE":
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def publisher_detail(request, pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     if request.method == "GET":
#         serializer = PublisherSerializer(publisher)
#         return Response(serializer.data)
#     elif request.method in ("PUT", "PATCH"):
#         serializer = PublisherSerializer(publisher, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status = status.HTTP_200_OK)
#     elif request.method == "DELETE":
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(["GET", "POST"])
# def publisher_list(request):
#     if request.method == "GET":
#         querySet = Publisher.objects.all()
#         serializer = PublisherSerializer(querySet, many=True, context={"request":request})
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
