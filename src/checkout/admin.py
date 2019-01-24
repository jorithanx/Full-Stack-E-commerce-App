from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)


# hobby-session-57

# hobby-session-105
