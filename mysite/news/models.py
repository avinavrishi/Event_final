from django.db import models


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='home/images', default="")

    def __str__(self):
        return self.headline
    