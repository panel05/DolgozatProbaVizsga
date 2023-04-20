from django.db import models

# Create your models here.


class Szakdoga(models.Model):
    szakdoga_nev = models.CharField(max_length=50, unique=True, verbose_name="szakdoga_nev")
    githublink = models.CharField(max_length=200, unique=True, verbose_name="githublink")
    oldallink = models.CharField(max_length=200, unique=True, verbose_name="oldallink")
    tagokneve = models.TextField(verbose_name="tagokneve")

