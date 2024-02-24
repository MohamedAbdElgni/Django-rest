from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    img = models.ImageField(upload_to='products/img', null=True, blank=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    
    
    def get_img_url(self):
        return f'/media/{self.img}'
    
