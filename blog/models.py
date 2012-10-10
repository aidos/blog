from django.db import models

class Entry(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('live', 'Live'),
        ('archived', 'Archived'),
    )

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    date_published = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS)

