from django.forms import ModelForm, TextInput, ClearableFileInput

from shop.models.category import Product


class CreateItemForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'in_stock', 'category_product', 'item_img')
        widgets = {
            'name': TextInput(attrs={
                'type': 'text'
            }),
            'description': TextInput(attrs={
                'type': 'text'
            }),
            'price': TextInput(attrs={
                'type': 'text'
            }),
            'in_stock': TextInput(attrs={
                'type': 'checkbox'
            }),
            'item_img': ClearableFileInput(attrs={
                'type': 'file'
                })
        }

