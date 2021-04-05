from django.db import models

# Create your models here.


class Link(models.Model):
    link = models.URLField()
    abbreviated_link = models.URLField()
    data = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def clicked(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return f'{self.pk} - {self.link} - ' \
               f'{self.abbreviated_link} - {self.data} - {self.clicks}'
