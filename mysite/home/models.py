from django.db import models


# Create your models here.
class Events(models.Model):
    EVENT_TYPE= (
        ('BATTLES', 'Batlle'),
        ('WORKSHOPS', 'Workshop'),
        ('CLASSES', 'Classes'),
    )

    EVENT_CATEGORY= (
            ('Hip-HOP', 'HIP-HOP'),
            ('Popping', 'Popping'),
            ('Breaking', 'Breaking'),
        )
    Event_id = models.AutoField(primary_key=True)
    Event_name = models.CharField(max_length=50)
    Event_type = models.CharField(max_length=10, choices = EVENT_TYPE, default="")
    Event_category = models.CharField(max_length=10, choices = EVENT_CATEGORY, default= "")
    Description = models.CharField(max_length=300, default= "")
    Venue = models.CharField(max_length=50, default="")
    Entry_fee = models.IntegerField(default = 0)
    Prize = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='home/images', default="")
    City = models.CharField(max_length= 20)
    Date = models.DateTimeField()




    def __str__(self):
        return self.Event_name
