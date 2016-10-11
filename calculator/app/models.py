from django.db import models

# Create your models here.


class Calc(models.Model):
    num_1 = models.IntegerField()
    num_2 = models.IntegerField()

    @property
    def plus(self):
        return self.num_1 + self.num_2
