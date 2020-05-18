from django.db import models

class Question(models.Model):
    question = models.CharField(max_lenth=255, blank=True, null=True)
