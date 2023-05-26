from shop.models.category import Product


def get_pk_and_filter_item_by_pk(self) -> list:
    item_pk = self.kwargs.get('pk')
    item = Product.objects.filter(pk=item_pk).first()
    return item
