from django.contrib import admin

from tweet.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user','content')
    


admin.site.register(Tweet, TweetAdmin)
