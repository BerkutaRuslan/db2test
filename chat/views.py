from django.core.paginator import Paginator
from rest_framework import generics
from chat.models import Messages, Author
from chat.pagination import MessageLimitOffsetPagination
from chat.serializers import ListAllMessagesSerializer, MessageSerializer, AuthorSerializer


class ListMessages(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = ListAllMessagesSerializer
    pagination_class = MessageLimitOffsetPagination


class SingleMessage(generics.RetrieveAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer


class CreateMessage(generics.CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer


class AuthorCreate(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
