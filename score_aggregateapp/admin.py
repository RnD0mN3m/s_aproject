from django.contrib import admin

# Register your models here.
from .models import Category, ScoreAggregateappPost
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
class ScoreAggregateappPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
admin.site.register(Category, CategoryAdmin)
admin.site.register(ScoreAggregateappPost, ScoreAggregateappPostAdmin)