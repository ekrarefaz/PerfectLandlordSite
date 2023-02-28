from io import BytesIO
from PIL import Image

from django.core.files import File
from django.contrib.auth.models import User
from django.db import models


class Property(models.Model):
    id = models.BigAutoField(primary_key=True)
    landlord = models.ForeignKey(User, on_delete = models.CASCADE)
    type = models.CharField(max_length=30, blank=False)
    slug = models.SlugField()    
    address= models.CharField(max_length=30, blank=False)
    description= models.CharField(max_length=100, blank=False)
    price= models.IntegerField(default=0, blank=False)

    # Images
    image = models.ImageField(upload_to='images/properties/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/properties/', blank=True, null=True)

    # Features
    room = models.IntegerField(default=0, blank=False)
    bathroom = models.IntegerField(default=0, blank=False)
    furnished = models.CharField(max_length=30, default='')
    airConditioning= models.CharField(max_length=30, default=0)
    gym= models.CharField(max_length=30, default=0)
    pool= models.CharField(max_length=30, default=0)

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.address
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class SavedProperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete = models.CASCADE)
    tenant = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        unique_together = (("property", "tenant"),)