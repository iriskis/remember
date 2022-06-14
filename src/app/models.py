from django.db import models
import uuid # Required for unique book instances

class Remember(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    comment = models.TextField(max_length=1000)
    date = models.DateField(null=True)

    def __str__(self):
        return '%s' % (self.title)

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="uploads/picture", blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.id, self.name)