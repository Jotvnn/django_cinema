import uuid

from django.db import models

class Genres(models.Model):
    name = models.CharField(verbose_name='name genres',max_length=100,unique=True,null=False)

    class Meta:
        verbose_name_plural  = 'Genres'

    def __str__(self):
        return f'{self.name}'

class Cinema(models.Model):
    name = models.CharField(verbose_name='name cinema', max_length=200, unique=True,null=False)
    preview_image = models.ImageField(verbose_name='image',upload_to='cinema/%Y/%m/%d/',null=False)
    date = models.DateField(verbose_name='date')
    date_update = models.DateField(auto_now_add=True)
    genres = models.ForeignKey(Genres,on_delete=models.DO_NOTHING,related_name='cinema')

    class Meta:
        verbose_name_plural  = 'Cinema'
    def generate_name_image(self):
        self.preview_image = uuid.uuid4()+'.jpg'
        return self.preview_image0
def __str__(self):
    return f"{self.name}"



class Actors(models.Model):
    name = models.CharField(verbose_name='name actor',max_length=100,null=False)
    surname = models.CharField(verbose_name='surname',max_length=100,null=False)
    age = models.IntegerField(null=False)
    cinema = models.ManyToManyField(Cinema)

    class Meta:
        verbose_name_plural = 'Actors'

