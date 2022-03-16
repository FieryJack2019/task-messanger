from django.test import TestCase
from API.models import Message
from django.contrib.auth.models import User


class MessageModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        user = User.objects.create(username='test', password='test')
        Message.objects.create(user=user, 
                               message='Hello world',
                               status=Message.REVIEW)

    def test_user_label(self):
        message=Message.objects.get(id=1)
        field_label = message._meta.get_field('user').verbose_name
        self.assertEquals(field_label,'Пользователь')

    def test_message_label(self):
        message=Message.objects.get(id=1)
        field_label = message._meta.get_field('message').verbose_name
        self.assertEquals(field_label,'Сообщение')

    def test_status_label(self):
        message=Message.objects.get(id=1)
        field_label = message._meta.get_field('status').verbose_name
        self.assertEquals(field_label,'Статус')

    def test_object_name(self):
        message=Message.objects.get(id=1)
        expected_object_name = '%s | %s | %s' % (message.pk, message.status, message.message)
        self.assertEquals(expected_object_name,str(message))