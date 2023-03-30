from shop.models.category import Product
from shop.serializer import ShopSerializer


def context_filter(**kwargs) -> dict:
    queryset = Product.objects.filter(**kwargs)
    serializer = ShopSerializer(queryset, many=True).data
    context = {
        "product": serializer
    }
    return context

