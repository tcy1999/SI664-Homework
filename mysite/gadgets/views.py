from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from gadgets.models import Brand, Gadget


class GadgetList(LoginRequiredMixin, View):
    def get(self, request):
        bc = Brand.objects.all().count()
        gl = Gadget.objects.all()

        ctx = {'brand_count': bc, 'gadget_list': gl}
        return render(request, 'gadgets/gadget_list.html', ctx)


class BrandList(LoginRequiredMixin, View):
    def get(self, request):
        bl = Brand.objects.all()
        ctx = {'brand_list': bl}
        return render(request, 'gadgets/brand_list.html', ctx)


class BrandCreate(LoginRequiredMixin, CreateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class BrandUpdate(LoginRequiredMixin, UpdateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class BrandDelete(LoginRequiredMixin, DeleteView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class GadgetCreate(LoginRequiredMixin, CreateView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class GadgetUpdate(LoginRequiredMixin, UpdateView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class GadgetDelete(LoginRequiredMixin, DeleteView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')
