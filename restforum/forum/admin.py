from django.contrib import admin

# Register your models here.
from forum.models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'user', 'created', 'updated',]


admin.site.register(Topic, TopicAdmin)
