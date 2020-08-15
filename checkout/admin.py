from django.contrib import admin
from .models import Order,  OrderLineItem

class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)
    
    readonly_fields = ('order_number', 'order_date', 
                       'delivery_cost', 'order_total', 'grand_total',
                       'original_cart', 'stripe_pid')
    
    fields = ('order_number', 'order_date', 'full_name', 'email',
              'phone_number', 'delivery_cost', 'order_total', 
              'grand_total', 'original_cart', 'stripe_pid')


    list_display = ('order_number','order_date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total',)
    
    ordering = ('-order_date',)
    
admin.site.register(Order, OrderAdmin)    