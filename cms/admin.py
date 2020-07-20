from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Paymentmethod)
admin.site.register(Shippers)
admin.site.register(Supplier)
admin.site.register(Tag)

