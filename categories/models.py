from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100 ,unique=True)
    description = models.TextField()
    img = models.ImageField(upload_to='categories/img', null=True, blank=True)
    
    
    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()
    
    @classmethod
    def get_category_by_id(cls, id):
        return cls.objects.get(id=id)
    
    @classmethod
    def get_category_by_name(cls, name):
        return cls.objects.get(name=name)
    
    def get_img_url(self):
        
        return f'/media/{self.img}'
    

    def __str__(self):
        return self.name