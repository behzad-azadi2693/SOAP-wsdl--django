from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=250, unique=True)


class PublisherModel(models.Model):
    name = models.CharField(max_length=250, unique=True)


class AuthoreModel(models.Model):
    name = models.CharField(max_length=250)


class BookModel(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=1000)
    descrition = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    authore = models.ForeignKey(AuthoreModel, on_delete=models.CASCADE)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.CASCADE)
    date = models.DateField()
    pages = models.PositiveBigIntegerField()
    thumbnail = models.ImageField(upload_to='book/')
    