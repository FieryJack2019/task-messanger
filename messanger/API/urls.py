from django.urls import path, include
from .views import MessageView, ConfirmationView

urlpatterns = [
    path('message/', MessageView.as_view()),
    path('message_confirmations/', ConfirmationView.as_view())
]