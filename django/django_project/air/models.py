from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=5)
    description = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name	

class City(models.Model):
    chinese_name = models.CharField(max_length=15)
    english_name = models.CharField(max_length=30)
    cityid = models.CharField(max_length=30)
    region = models.ForeignKey(Region)
    intro = models.CharField(max_length=250, null=True)
    coordinate = models.CharField(max_length=20, null=True)
    url = models.URLField(null=True)
    click = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.chinese_name

class Counter(models.Model):
    city = models.ForeignKey(City)
    night4 = models.PositiveIntegerField(default=0)
    morning5 = models.PositiveIntegerField(default=0)
    afternoon5 = models.PositiveIntegerField(default=0)
    night5 = models.PositiveIntegerField(default=0)
    morning6 = models.PositiveIntegerField(default=0)
    afternoon6 = models.PositiveIntegerField(default=0)
    night6 = models.PositiveIntegerField(default=0)
	
    def __str__(self):
        return self.city.chinese_name	

class Comment(models.Model):
    visitor = models.CharField(max_length=20, default='cool anteater')
    email =models.EmailField(max_length=100, default='xxx@mail')
    content = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    
    def __str__(self):
        return self.visitor
	
    class Meta:
        ordering = ['date_time']
       