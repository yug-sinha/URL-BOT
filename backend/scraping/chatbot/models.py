from django.db import models

class WebsiteData(models.Model):
    url = models.URLField(unique=True)
    content = models.TextField()

    def __str__(self):
        return self.url
