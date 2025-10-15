from django.contrib import admin
from publications_registry import models


# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Article)
admin.site.register(models.Reviewer)
admin.site.register(models.ArticleReview)