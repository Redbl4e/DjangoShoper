from django.db import models


class Category(models.Model):
    OUTERWEAR = 'Верхняя одежда'
    JEANS = 'Джинсы'
    SHOES = 1
    GLASSES = 'Очки'

    CHOISE_GROUP = {
        (OUTERWEAR, 'Верхняя одежда'),
        (JEANS, 'Джинсы'),
        (SHOES, 'Обувь'),
        (GLASSES, 'Очки'),
    }

    category = models.CharField(max_length=255, choices=CHOISE_GROUP, db_index=True, default=False, null=False)

    class Meta:
        verbose_name = 'категории'

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='описание')
    price = models.IntegerField(verbose_name='Цена')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    category_product = models.ForeignKey(to=Category, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'товары'

    def __str__(self):
        return self.name


