from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name

class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Journalist(models.Model):
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.author

class New(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    text = models.TextField(max_length=500)
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name="comments")
