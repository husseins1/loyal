from django.contrib import admin
from django.urls import reverse_lazy
from core.models import costumer,Group,Invoice,Order
from django.utils.html import format_html
# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    search_fields = ['first_name','identity']
    list_display = ('first_name', 'last_name','phone_number','identity','credit','birthday','my_url_field','history')

    def my_url_field(self, obj):
        return format_html(f'<a href="{reverse_lazy("print id", kwargs={"id":obj.identity})}" class="btn btn-primary">print</a>')
    my_url_field.allow_tags = True
    my_url_field.short_description = 'actions'
    def history(self, obj):
        return format_html(f'<a href="{reverse_lazy("history", kwargs={"id":obj.identity})}" class="btn btn-primary">History</a>')
    
    
    


admin.site.register(costumer, MyUserAdmin)

class GroupCore(admin.ModelAdmin):
    
    pass

admin.site.register(Group,GroupCore)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('totalPrice','tableNumber')
    pass
    


admin.site.register(Invoice,InvoiceAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','total')
    pass

admin.site.register(Order,OrderAdmin)