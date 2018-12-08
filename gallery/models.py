from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_category(self):
        self.update()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()


    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=30)
    Description = models.TextField()
    location = models.ForeignKey('Location')
    category = models.ManyToManyField('Category')


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    def __str__(self):
        return self.name


