from django.db import models
from . import custom_validators

#todo: in Author model add ordering in Meta class

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Imię",)
    last_name = models.CharField(max_length=100, verbose_name="Nazwisko",)
    email = models.EmailField(max_length=100, unique=True)
    orcid = models.CharField(max_length=19,
                             blank=True,
                             unique=True,
                             validators=[custom_validators.validate_orcid],
                             )
    comments = models.TextField(blank=True, verbose_name="Uwagi",)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Article(models.Model):

    PUBLICATION_STATUS_CHOICES = [
        ("SUBMITTED", "Zgłoszony"),
        ("PRESELECTION", "Preselekcja"),
        ("ANTIPLAGIARISM", "Antyplagiat"),
        ("REVIEW", "Recenzje"),
        ("OK_FOR_PRINT", "Skierowany do druku"),
        ("WITHDRAWN_BY_AUTHOR", "Wycofany przez autora"),
        ("WITHDRAWN_FROM_ONLINE_ED", "Wycofany z wydania online"),
        ("REJECTED", "Odrzucony"),
    ]

    PUBLICATION_SUBMISSION_CHOICES = [
        ("OJS", "Open Journal System"),
        ("EMAIL_EDITORIAL_BOARD", "Email redakcji"),
        ("EMAIL_PRIVATE", "Email prywatny"),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               verbose_name="Autor",
                               )
    article_title = models.CharField(max_length=200,
                                     unique=True,
                                     verbose_name="Tytuł",
                                     )
    # Signing a license agreement allowing publication.
    license_agreement = models.BooleanField(default=False,
                                            verbose_name="Umowa licencyjna",
                                            )
    # Check for plagiarism; True if check commited, regardless of result.
    antiplagiarism_check = models.BooleanField(default=False,
                                               verbose_name="Antyplagiat",
                                               )
    # Status of publication process.
    article_status = models.CharField(max_length=30,
                                      choices=PUBLICATION_STATUS_CHOICES,
                                      default="SUBMITTED",
                                      verbose_name="Status artykułu",
                                      )
    # Issue in which the article will be published.
    issue = models.CharField(max_length=20,
                             default=None,
                             blank=True,
                             validators=[
                                 custom_validators.validate_issue_number],
                             verbose_name="Numer",
                             )
    # Method of article submission chosen by author.
    method_of_submission = models.CharField(max_length=30,
                                            choices=
                                                PUBLICATION_SUBMISSION_CHOICES,
                                            verbose_name="Sposób zgłoszenia",
                                            )
    # Any comments for article, like violation of code of ethics etc.
    comments = models.TextField(blank=True, verbose_name="Uwagi",)

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

    def __str__(self):
        return f"{self.article_title}"


class Reviewer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Imię",)
    last_name = models.CharField(max_length=100, verbose_name="Nazwisko",)
    email = models.EmailField(max_length=100, unique=True)
    orcid = models.CharField(max_length=19,
                             validators=[custom_validators.validate_orcid],
                             )
    comments = models.TextField(blank=True, verbose_name="Uwagi",)

    class Meta:
        verbose_name = "Recenzent"
        verbose_name_plural = "Recenzenci"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class ArticleReview(models.Model):
    RECOMMENDATION_CHOICES = [
        ("ACCEPT", "Przyjąć do druku"),
        ("ACCEPT_CONDITIONALLY", "Przyjąć do druku po poprawkach"),
        ("REJECT", "Odrzucić"),
    ]

    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE,
                                 verbose_name="Recenznet",
                                 )
    article_title = models.OneToOneField(Article, on_delete=models.CASCADE,
                                         verbose_name="Tytuł",
                                         )
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               verbose_name="Autor",
                               null=True,
                               )
    recommendation = models.CharField(max_length=30,
                                      choices=RECOMMENDATION_CHOICES,
                                      verbose_name="Ocena",
                                      )
    comments = models.TextField(blank=True, verbose_name="Uwagi",)

    class Meta:
        verbose_name = "Recenzja"
        verbose_name_plural = "Recenzje"

    def __str__(self):
        return f"{self.reviewer}, rec. {self.article_title}"
