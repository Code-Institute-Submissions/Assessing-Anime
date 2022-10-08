from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="anime_post", null=True)
    item_content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='AnimeLikes', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.item_name.replace(" ", '-')
        super().save(*args, **kwargs)


    def __str__(self):
        return self.item_name


    def number_of_likes(self):
        return self.likes.count()
