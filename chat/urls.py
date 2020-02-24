from django.urls import path

from chat.views import ListMessages, SingleMessage, CreateMessage, AuthorCreate

urlpatterns = [
    path("api/messages/create/", CreateMessage.as_view()),
    path("api/messages/list/", ListMessages.as_view()),
    path("api/messages/single/<int:pk>", SingleMessage.as_view()),
    path("api/author/create/", AuthorCreate.as_view()),
]