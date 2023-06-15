from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='NoName_Article')
    anons = models.CharField('Announcement', max_length=250, default='NoName_Announcement')
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'