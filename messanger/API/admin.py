from django.contrib import admin
from .models import BlackList, Message


admin.site.register(Message)
admin.site.register(BlackList)
