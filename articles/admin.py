from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display =('name','body','post','created_on','active')
    list_filter = ('active','created_on')
    search_fields =('name','body')
    #actions=['approve_comments']
    
    #def approve_comments(self,request,queryset):
        #queryset.update(active=True)