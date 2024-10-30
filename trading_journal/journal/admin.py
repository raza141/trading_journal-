from django.contrib import admin

# Register your models here.
from .models import TradeEntry

# Register the TradeEntry model so it appears in the admin panel
admin.site.register(TradeEntry)
