from rest_framework import serializers
from my_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        # field = "__all__"
        fields = ['name', 'email', 'url']


class BookSerializer(serializers.ModelSerializer): # noqa
    # publisher = serializers.PrimaryKeyRelatedField(read_only=True)
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='my_app:publisher_detail'
    # )

    class Meta:
        model = Book
        fields = "__all__"
        # fields = ['title', 'description', 'date_published' 'isbn', 'price', 'publisher']
        # exclude = []
