from django.db import models


class Primes(models.Model):
    number = models.BigIntegerField()
    status = models.CharField(max_length=20)
    prime = models.BooleanField()
