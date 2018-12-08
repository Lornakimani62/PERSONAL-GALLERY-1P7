from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self,update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        location = Location.objects.get(pk = id)
        return location

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category


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
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    @classmethod
    def get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        return images

    def __str__(self):
        return self.name


