from django.contrib import admin

from .models import Remember, Userpic

# Register your models here.

admin.site.register(Userpic)
admin.site.register(Remember)