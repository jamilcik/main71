from django.contrib import admin
from .models import Xodim


@admin.register(Xodim)
class XodimAdmin(admin.ModelAdmin):
    list_display = ('id', 'ismi', 'familiyasi', 'yoshi', 'kasbi')
    search_fields = ('ismi', 'familiyasi', 'kasbi')
    list_filter = ('kasbi',)


from django.contrib import admin

# Register your models here.
