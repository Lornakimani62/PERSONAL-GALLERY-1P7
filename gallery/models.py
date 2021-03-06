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
    category = models.ForeignKey('Category')
    pic = models.ImageField(upload_to = 'photos/')


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name, Description , location,category):
        update = cls.objects.filter(id = id).update(name = name, Description = Description ,location = location,category = category)
        # return update

    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images
        print(images)

    @classmethod
    def get_image_by_id(self,image):
        image= Image.objects.get(id = id)
        return image

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images
    @classmethod
    def filter_by_location(cls,location):
        images = cls.objects.filter(category__name__icontains=location)

        return images
    def __str__(self):
        return self.name


