from rest_framework import serializers

from products.models import Product



class ProductSerializer(serializers.ModelSerializer):

    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.img = validated_data.get('img', instance.img)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    
    
    class Meta:
        model = Product
        fields = '__all__'
        