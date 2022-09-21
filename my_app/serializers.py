from rest_framework import serializers
from my_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']


class BookSerializer(serializers.ModelSerializer): # noqa
    publisher = serializers.PrimaryKeyRelatedField(read_only=True)
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='my_app:publisher_detail'
    # )

    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn', 'price', 'publisher']
        # exclude = []
