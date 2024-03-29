from django.contrib import admin
from .models import Snippet

# snippets/admin.py
from django.contrib import admin
from . models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)


admin.site.register(Snippet, SnippetAdmin)

# admin.site.register(Snippet)