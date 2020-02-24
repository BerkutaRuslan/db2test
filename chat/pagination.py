from rest_framework.pagination import (
    LimitOffsetPagination, PageNumberPagination
)


class MessageLimitOffsetPagination(PageNumberPagination):
    page_size = 10
