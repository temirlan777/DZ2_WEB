from django.contrib import admin
from article.models import Article, Comments


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_title', 'article_text']
	#list_filter = ['article_date']

class ArticleInline(admin.StackedInline):
	model = Comments
	extra = 2



admin.site.register(Article, ArticleAdmin)