from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, blank=True)
    artists = models.CharField(max_length=500)
    album = models.CharField(max_length=200)
    external_links = models.URLField()
    genre = models.CharField(max_length=200, blank=True, null=True)
    import_status = models.CharField(max_length=200, default="pending")
    date = models.DateField(blank=True, null=True)
