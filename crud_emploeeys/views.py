from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from crud_emploeeys.forms import CreateItemForm
from crud_emploeeys.services.get_pk_and_filter_item import get_pk_and_filter_item_by_pk
from shop.models.category import Product


class ViewCRUD(PermissionRequiredMixin, View):
    permission_required = "shop.add_category"

    def get(self, request):
        return render(request, 'crud/home.html')


class CreateItemEmploeeys(PermissionRequiredMixin, CreateView):
    permission_required = "shop.add_category"

    success_url = reverse_lazy('shop:home')

    def get(self, request, *args, **kwargs):
        form = CreateItemForm()
        context = {
            'form': form
        }
        return render(request, 'crud/create.html', context)

    def post(self, request, *args, **kwargs):
        form = CreateItemForm(request.POST, request.FILES)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
        return render(request, 'crud/create.html', context)


class ItemUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "shop.add_category"

    model = Product
    form_class = CreateItemForm
    template_name = 'crud/update.html'
    context_object_name = 'item'
    success_url = reverse_lazy('shop:home')

    def get_object(self, queryset=None):
        return get_pk_and_filter_item_by_pk(self=self)


class ItemDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "shop.add_category"

    success_url = reverse_lazy('shop:home')
    model = Product

    def get(self, request, *args, **kwargs):
        context = {
            "item": get_pk_and_filter_item_by_pk(self=self)
        }
        return render(request, 'crud/delete.html', context)

