from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ We are telling Django to register our model with a custom
        view. In this case, we are telling it to display listed attributes
        in admin object list page. """
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title', )}

    # in the book(django-1.8), type is tuple,
    # however, django wanted the type to be a list.
    raw_id_fields = ['author', ]

    date_hierarchy = 'publish'
    ordering = ['status', 'publish']



