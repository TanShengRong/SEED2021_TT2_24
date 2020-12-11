from django.contrib import admin

from .models import UserDetails, AccountDetails, TransactionAmounts

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(AccountDetails)
admin.site.register(TransactionAmounts)