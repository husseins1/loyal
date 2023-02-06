from django.contrib import admin
from django.urls import reverse_lazy
from core.models import costumer,Group
from django.utils.html import format_html
# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','phone_number','identity','credit','birthday','my_url_field','send')

    def my_url_field(self, obj):
        return format_html(f'<a href="/" class="btn btn-primary">print</a>')
    my_url_field.allow_tags = True
    my_url_field.short_description = 'actions'
    def send(self, obj):
        return format_html(f'<a href="{reverse_lazy("send", kwargs={"phone_number":obj.phone_number})}" class="btn btn-primary">Send</a>')
    send.allow_tags = True
    send.short_description = 'actions'


admin.site.register(costumer, MyUserAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ['type']
    pass

admin.site.register(Group,GroupAdmin)