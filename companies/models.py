from django.db import models

# Create your models here.

class Company(models.Model):                        # КОМПАНИИ/ПРОДАВЦЫ
    name_company = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # description = models.TextField(null=True)

    class Meta:
        ordering = ['name_company']



class Category(models.Model):
    cloth = models.CharField(max_length=50)
    shoes = models.CharField(max_length=50)
    accessories = models.CharField(max_length=50)


class Season(models.Model):
    summer = models.CharField(max_length=50)
    winter = models.CharField(max_length=50)
    spring = models.CharField(max_length=50)
    autumn = models.CharField(max_length=50)
    demi_season = models.CharField(max_length=50)


class SizeCloth(models.Model):
    sizeOne = models.IntegerField(max_length=10)
    sizeTwo = models.IntegerField(max_length=10)
    sizeThree = models.IntegerField(max_length=10)
    sizeFour = models.IntegerField(max_length=10)
    sizeFive = models.IntegerField(max_length=10)

class SizeShoes(models.Model):
    sizeOne = models.IntegerField(max_length=10)
    sizeTwo = models.IntegerField(max_length=10)
    sizeThree = models.IntegerField(max_length=10)
    sizeFour = models.IntegerField(max_length=10)
    sizeFive = models.IntegerField(max_length=10)

class Reserv(models.Model):
    is_reserved = models.BooleanField(default=False)


class Product(models.Model):
    name_prod = models.CharField(max_length=50)
    description = models.TextField(null=True)
    product_composition = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.FloatField()
    product_count = models.IntegerField(max_length=200)  # (наличие товара на складе, единиц)
    # photo = models.ImageField(null=True, blank=True)   # (ФОТОГРАФИИ товара)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)        # ForeignKey
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)    # ForeignKey
    size_cloth = models.ForeignKey(SizeCloth, on_delete=models.SET_NULL, null=True) # ForeignKey
    size_shoes = models.ForeignKey(SizeShoes, on_delete=models.SET_NULL, null=True)
    reserv = models.ForeignKey(Reserv, on_delete=models.SET_NULL, null=True)        # ForeignKey

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)      # ForeignKey

    class Meta:
        ordering = ['name_prod']




