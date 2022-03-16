from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    REVIEW = 1
    BLOCKED = 2
    CORRECT = 3
    STATUS_CHOICE = (
        (REVIEW, 'review'),
        (BLOCKED, 'blocked'),
        (CORRECT, 'correct')
    )
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, verbose_name='Пользователь')
    message = models.TextField(verbose_name='Сообщение')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, verbose_name='Статус')

    def __str__(self):
        return f"{self.pk} | {self.status} | {self.message}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class BlackList(models.Model):
    word = models.CharField(max_length=50, verbose_name='Слово')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Черный список'
        verbose_name_plural = 'Черный список'