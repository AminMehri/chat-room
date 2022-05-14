from django.contrib import admin
from .models import Message, Chat


class MessageAdmin(admin.ModelAdmin):
    list_display = ['content', 'author', 'related_chat', 'timestamp']


admin.site.register(Message, MessageAdmin)


class ChatAdmin(admin.ModelAdmin):
    list_display = ['roomname', 'member_in_room']

    def member_in_room(self, obj):
        return ", ".join([member.username for member in obj.members.all()])
    member_in_room.short_description = "members"


admin.site.register(Chat, ChatAdmin)