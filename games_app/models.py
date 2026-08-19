from django.db import models
class Game(models.Model):
    name = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
# Create your models here.
