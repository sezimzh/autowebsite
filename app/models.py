from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=223)
    
    def __str__(self):
        return self.title
class Car(models.Model):
    title=models.CharField(max_length=123)
    model=models.CharField(max_length=123)
    price=models.DecimalField(decimal_places=2,max_digits=12)
    year=models.PositiveSmallIntegerField()
    image=models.ImageField(upload_to='media/car_images')
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    description = models.TextField()
    
    def __str__(self):
        return self.title