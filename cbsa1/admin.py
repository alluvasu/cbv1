from django.contrib import admin
from cbsa1.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display=['title','name','pages']

admin.site.register(Book,BookAdmin)

# Register your models here.
