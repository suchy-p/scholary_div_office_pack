from django.db import models
from django.contrib.auth.models import AbstractUser
from . import custom_validators

# Create your models here.

class Articles(models.Model):

    PUBLICATION_STATUS_CHOICES = {
        "SUBMITTED": "Zgłoszony",
        "PRESELECTION": "Preselekcja",
        "ANTIPLAGIARISM": "Antyplagiat",
        "REVIEW": "Recenzje",
        "OK_FOR_PRINT": "Skierowany do druku",
        "WITHDRAWN_BY_AUTHOR": "Wycofany przez autora",
        "WITHDRAWN_FROM_ONLINE_ED": "Wycofany z wydania online",
        "REJECTED": "Odrzucony",
    }

    PUBLICATION_SUBMISSION_CHOICES = {
        "OJS": "Open Journal System",
        "EMAIL_EDITORIAL_BOARD": "Email redakcji",
        "EMAIL_PRIVATE": "Email prywatny"
    }

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    article_title = models.CharField(max_length=200)
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
                             validators=[
                                 custom_validators.validate_issue_number]
                             )
    # Method of article submission chosen by author.
    method_of_submission = models.CharField(max_length=30,
                                            choices=
                                                PUBLICATION_SUBMISSION_CHOICES,
                                            )
    # Any comments for article, like violation of code of ethics etc.
    comments = models.TextField()
    # Database record history logs.
    updated_by = "_"
    updated_at = models.DateTimeField(auto_now=True)
    created_by = "_"
    created_at = models.DateTimeField(auto_now_add=True)



class Users(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)

