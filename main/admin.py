from django.contrib import admin
from publications_registry import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "orcid", "email",)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("article_title", "author", "article_status", "issue",)
    list_filter = ("issue", "article_status", )
    search_fields = ("article_title","author__last_name", "author__first_name",
                     )


@admin.register(models.Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "orcid", "email",)


@admin.register(models.ArticleReview)
class ArticleReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer", "article_title", "author", "recommendation")

# Register your models here.
# admin.site.register(models.Author)
# admin.site.register(models.Article)
# admin.site.register(models.Reviewer)
# admin.site.register(models.ArticleReview)
