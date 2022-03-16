from celery import shared_task
import django
import os

django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messanger.settings")


@shared_task(name="confirmation_messages")
def confirmation_messages(token):
    from .models import Message, BlackList
    from rest_framework.test import APIClient

    messages_review = Message.objects.filter(status=Message.REVIEW)
    auth = "Bearer {0}".format(token)
    client = APIClient()
    
    for message in messages_review:
        is_confirmation = True
        black_list_word = [item.word.lower() for item in BlackList.objects.all()]
        print(black_list_word)
        for word in message.message.lower().split():
            print(word)
            if word in black_list_word:
                is_confirmation = False
                break
        
        client.post('/api/v1/message_confirmations/',
                      HTTP_AUTHORIZATION=auth,
                      data={'message_id': message.id,
                            'success': is_confirmation})
