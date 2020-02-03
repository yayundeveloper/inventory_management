from django.db import models

class Officesupplies(models.Model):

    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )
    status = models.CharField(max_length=10, choices=choices, default="SOLD")  # Available, Sold, Restocking
    issues = models.CharField(max_length=10, default="No issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price: {1}'.format(self.type, self.price)

class Pen(Officesupplies):
    pass

class Notebook(Officesupplies):
    pass

class Pencilcase(Officesupplies):
    pass
