from django.db import models


# Create your models here.

class Districts(models.Model):

    dist_name = models.CharField(max_length=250)


    def __str__(self):
        return self.dist_name


class Branches(models.Model):
    branch_name = models.CharField(max_length=250)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch_name
