from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255, db_index=True, default='SOME STRING', null=False)
    href = models.ImageField(upload_to='images/category/', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True, default='SOME STRING')

    class Meta:
        verbose_name = 'категории'

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True, default='SOME STRING',verbose_name='Название')
    description = models.TextField(max_length=2000, default='SOME STRING', verbose_name='описание')
    price = models.IntegerField(verbose_name='Цена')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    item_img = models.ImageField(upload_to='images/item', blank=True, null=True)
    category_product = models.ForeignKey(to=Category, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'товары'

    def __str__(self):
        return self.name