from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=35, blank=False)
    mail = models.CharField(max_length=35, blank=False)
    admission = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} > {self.admission}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'
