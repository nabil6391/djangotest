from django.contrib import admin

# Register your models here.

from .models import Product ,Family ,Location ,Transaction
# Register your models here.

admin.site.register(Product)
admin.site.register(Family)
admin.site.register(Location)
admin.site.register(Transaction)
