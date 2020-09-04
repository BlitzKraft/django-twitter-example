from django.contrib import admin
from .models import MyUser, MyTweet

# Register your models here.

class MyUserAdmin(admin.ModelAdmin):
    list_display = [ 'username', "email_verified", "verified_user"]

class TweetAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'tweet']


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MyTweet, TweetAdmin)
