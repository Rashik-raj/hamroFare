from django.contrib import admin
from .models import User, Transaction, Card

admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(Card)