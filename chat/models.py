from django.core.validators import RegexValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "author"


class Messages(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # email = models.CharField(max_length=255, validators=RegexValidator[r'@']) # YOU ASKЕD FOR REGEX
    # VALIDATION, HERE IT IS
    email = models.EmailField()
    text = models.CharField(max_length=100)

    create_date = models.DateTimeField(auto_now_add=True)
    update_field = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name_plural = "Messages"
