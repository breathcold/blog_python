from django.contrib import admin

# Register your models here.
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time')
    list_filter = ('create_time', )
    #tuple只有一个元素的时候需要加上一个逗号

admin.site.register(Article, ArticleAdmin)
