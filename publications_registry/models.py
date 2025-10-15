from django.db import models
from . import custom_validators


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    orcid = models.CharField(max_length=19,
                             unique=True,
                             validators=[custom_validators.validate_orcid]
                             )
    comments = models.TextField(blank=True)

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

    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False)
    article_title = models.CharField(max_length=200, blank=False)
    # Signing a license agreement allowing publication.
    license_agreement = models.BooleanField(default=False)
    # Check for plagiarism; True if check commited, regardless of result.
    antiplagiarism_check = models.BooleanField(default=False)
    # Status of publication process.
    article_status = models.CharField(max_length=30,
                                      choices=PUBLICATION_STATUS_CHOICES,
                                      default="SUBMITTED",
                                      )
    # Issue in which the article will be published.
    issue = models.CharField(max_length=20,
                             default=None,
                             blank=True,
                             validators=[
                                 custom_validators.validate_issue_number]
                             )
    # Method of article submission chosen by author.
    method_of_submission = models.CharField(max_length=30,
                                            blank=False,
                                            choices=
                                                PUBLICATION_SUBMISSION_CHOICES,
                                            )
    # Any comments for article, like violation of code of ethics etc.
    comments = models.TextField()

    def __str__(self):
        return f"{self.article_title}"


class Reviewer(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    orcid = models.CharField(max_length=19,
                             blank=False,
                             validators=[custom_validators.validate_orcid]
                             )
    comments = models.TextField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class ArticleReview(models.Model):
    RECOMMENDATION_CHOICES = [
        ("ACCEPT", "Przyjąć do druku"),
        ("ACCEPT_CONDITIONALLY", "Przyjąć do druku po poprawkach"),
        ("REJECT", "Odrzucić"),
    ]

    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article_title = models.OneToOneField(Article, on_delete=models.CASCADE)
    recommendation = models.CharField(max_length=30, choices=
        RECOMMENDATION_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f"{self.reviewer}, rec. {self.author}, {self.article_title}"
