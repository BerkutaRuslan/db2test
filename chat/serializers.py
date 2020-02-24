from rest_framework.serializers import ModelSerializer

from chat.models import Messages, Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class ListAllMessagesSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Messages
        fields = ['id', 'author', 'email', 'text']


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = "__all__"

