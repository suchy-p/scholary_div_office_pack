from django.contrib import admin
from publications_registry import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "orcid", "email",)

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("article_title", "author", "article_status", "issue",)


class ReviewerAdmin(admin.ModelAdmin):
    pass


class ArticleReviewAdmin(admin.ModelAdmin):
    pass


# Register your models here.
#admin.site.register(models.Author)
#admin.site.register(models.Article)
admin.site.register(models.Reviewer)
admin.site.register(models.ArticleReview)