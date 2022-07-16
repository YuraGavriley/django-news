from calendar import c
from django.contrib import admin

from .models import New, Location, Journalist, Category, Comment
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    list_filter = ("location", "journalist")
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "new")

admin.site.register(New, NewsAdmin)
admin.site.register(Location)
admin.site.register(Journalist)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)