from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    img = models.ImageField(upload_to='products/img', null=True, blank=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    
    @classmethod
    def get_all_products(cls):
        return cls.objects.all()
    
    @classmethod
    def get_product_by_id(cls, id):
        return cls.objects.get(id=id)
    
    @classmethod
    def get_product_by_name(cls, name):
        return cls.objects.get(name=name)
    
    def get_img_url(self):
        return f'/media/{self.img}'
    
    def __str__(self):
        return self.name
