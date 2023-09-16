from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=200)

class Items(models.Model):
    Id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places= True)
    image = models.ImageField(blank=True ) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, blank = True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']