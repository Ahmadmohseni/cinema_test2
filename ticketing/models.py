from django.db import models
from django.db.models.base import Model
#from django.db.models.enums import Choices

# Create your models here.
class Movie(models.Model):
    class Meta:
        verbose_name='فیلم'
        verbose_name_plural='فیلم ها'
    name = models.CharField(max_length=100)
    directior=models.CharField(max_length=50)
    year=models.IntegerField() 
    length=models.IntegerField() 
    discription=models.TextField()
    #poster=models.ImageField('پوستر', upload_to='movie_poster/')

    def __str__(self):
        return self.name

class Cinema(models.Model):
    class Meta:
        verbose_name='سینما'
        verbose_name_plural='سینما ها'
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=30 ,default='تهران')
    capacity=models.IntegerField()
    phone=models.CharField(max_length=20,null=True)
    address=models.TextField()
    #image=models.ImageField('عکس' , upload_to='cinema_image/' , null=True)

    def __str__(self):
        return self.name

class ShowTime(models.Model):
    class Meta:
        verbose_name='سانس'
        verbose_name_plural='سانس ها'
    movie=models.ForeignKey('Movie',on_delete=models.PROTECT)
    Cinema=models.ForeignKey('Cinema', on_delete=models.PROTECT)
    start_time=models.DateTimeField()
    price=models.IntegerField()
    salable_seat=models.IntegerField()
    free_seat=models.IntegerField()

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED,'فروش آغاز نشده'),
        (SALE_OPEN,'در حال فروش بلیط'),
        (TICKETS_SOLD,'بلیط ها تمام شد'),
        (SALE_CLOSED,'فروش بلیط بسته شد'),
        (MOVIE_PLAYED,'فیلم پخش شد'),
        (SHOW_CANCELED,'سانس لغو شد'),
    )
    status =models.IntegerField(choices =status_choices)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.Cinema , self.start_time)
    
    def get_price_display(self):
        return 'تومان  {}'.format(self.price)
    
    def is_full(self):
        return self.free_seat ==0