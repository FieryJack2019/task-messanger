from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Message
from .serializers import MessageSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class MessageView(APIView):
    def post(self, request):
        user = User.objects.filter(id=request.data['user_id']).first()
        if user:
            serializer = MessageSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user, 
                            status=Message.REVIEW)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ConfirmationView(APIView):
    permission_classes = [TokenHasReadWriteScope]

    def post(self, request):
        message = Message.objects.filter(id=request.data['message_id']).first()
        if message:
            if request.data['success']:
                message.status = Message.CORRECT
            else:
                message.status = Message.BLOCKED
            message.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)