from aiohttp import request
from django.test import TestCase
from API.models import Message, BlackList
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from oauth2_provider.models import Application, AccessToken
from django.utils import timezone
import datetime as dt
from rest_framework import status


class MessageViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.user_test = User.objects.create(username='test', password='test')
        self.client = APIClient()

    def test_message_view(self):
        request = self.client.post('/api/v1/message/',
                              data={'user_id': self.user_test.id,
                                    'message': "Hello World!"})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


class ConfirmationViewTest(TestCase):
    
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username='test', password='test')
        BlackList.objects.create(word="АБРАКАДАБРА")
        self.message_1 = Message.objects.create(user=self.user, 
                                                message='Hello world',
                                                status=Message.REVIEW)
        self.message_2 = Message.objects.create(user=self.user, 
                                                message='Hello аБраКаДаБрА',
                                                status=Message.REVIEW)
        self.application = Application(name="Test Application",
                                       redirect_uris="http://localhost",
                                       user=self.user,
                                       client_type=Application.CLIENT_CONFIDENTIAL,
                                       authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE)
        self.application.save()
        self.token = AccessToken.objects.create(user=self.user, token='1234567890',
                                                application=self.application, scope='read write',
                                                expires=timezone.now() + dt.timedelta(days=1))
        self.token.save()
        self.auth = "Bearer {0}".format(self.token.token)
        self.client = APIClient()

    def test_confirmation_view_true(self):
        request = self.client.post('/api/v1/message_confirmations/',
                                   data={'message_id': self.message_1.id,
                                         'success': True},
                                   HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(request.status_code, status.HTTP_202_ACCEPTED)

    def test_confirmation_view_true(self):
        request = self.client.post('/api/v1/message_confirmations/',
                                   data={'message_id': self.message_2.id,
                                         'success': False},
                                   HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(request.status_code, status.HTTP_202_ACCEPTED)
                            
        
