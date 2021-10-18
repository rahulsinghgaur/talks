from django.contrib import admin
from .models import Friend
from .models import Messages
# Register your models here.
@admin.register(Friend)
class Friends(admin.ModelAdmin):
    f = ['id','username','friends']

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    m = ['id','sender','receiver','message','timestamp']