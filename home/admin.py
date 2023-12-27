from django.contrib import admin
from .models import writer , writing

# Register your models here.

class writing_admin(admin.ModelAdmin):
    list_display  = ("writer_id", "heading", "sub_category", "language","publishing_date",)

admin.site.register(writing, writing_admin)