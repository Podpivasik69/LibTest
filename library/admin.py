from django.contrib import admin
from.models import Book , Author


class bookAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','description','count_pages','publish_date','cover_type','size')
    list_display_links = ('id','title')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields =('title')
    list_editable = ('price')
    list_filter = ('author','cover_type','size')



admin.site.register(Book)
admin.site.register(Author)

# Register your models here.
