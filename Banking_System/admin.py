from django.contrib import admin
from .models import Customer, TransactionHistory

# Register your models here.
admin.site.register(Customer)
admin.site.register(TransactionHistory)