from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from crud_emploeeys.forms import CreateItemForm


class ViewCRUD(PermissionRequiredMixin, View):
    permission_required = "shop.add_category"

    def get(self, request):
        return render(request, 'crud/home.html')


class CreateItemEmploeeys(PermissionRequiredMixin, CreateView):
    permission_required = "shop.add_category"

    def get(self, request, *args, **kwargs):
        form = CreateItemForm()
        context = {
            'form': form,

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
