from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255, db_index=True, default=False, null=False)
    href = models.ImageField(upload_to='images/category/', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'категории'

    def __str__(self):
        return self.category


class MediaItem(models.Model):
    item_img = models.ImageField(upload_to='images/', blank=True,null=True)

    class Meta:
        verbose_name = 'фото'

    def __str__(self):
        return self.item_img


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='описание')
    price = models.IntegerField(verbose_name='Цена')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    category_product = models.ForeignKey(to=Category, null=True, on_delete=models.SET_NULL)
    product_item_img = models.OneToOneField(to=MediaItem, on_delete=models.CASCADE,
                                            blank=True, null=True)

    class Meta:
        verbose_name = 'товары'

    def __str__(self):
        return self.name
