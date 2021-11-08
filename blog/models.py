from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images_files/')

    def abbreviated_form_of_description(self):
        return self.body[:50]

    def dated_form(self):
        return self.pub_date.strftime('%b %d %Y ')

    def __str__(self):
        return self.title