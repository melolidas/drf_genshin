
from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=15)
    story = models.TextField(blank=1)
    element = models.ForeignKey('Element', on_delete=models.PROTECT, null=1)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, null=1)
    photo = models.ImageField(upload_to='images/', blank=1, verbose_name= 'Изображение')

    def __str__(self):
        return '{}/{}'.format(self.name, self.story, self.photo)



class Element(models.Model): 
    name_element = models.CharField(max_length=10,db_index=1)

    def __str__(self):
        return self.name_element



class Country(models.Model):
    city = models.CharField(max_length=25, db_index=1)

    def __str__(self):
        return self.city