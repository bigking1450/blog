import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    excerpt = models.CharField(max_length=255)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='cover_images')
    intro_images = ArrayField(models.CharField(
        max_length=255), blank=True, default=list)
    body_images = ArrayField(models.CharField(
        max_length=255), blank=True, default=list)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.title
