from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Supplier
from .forms import SupplierForm
from django.db.models import Q

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'suppliers/supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(cnpj__icontains=query) |
                Q(email__icontains=query) |
                Q(contact_person__icontains=query) |
                Q(address_city__icontains=query)
            ).distinct()
        return queryset

class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = 'suppliers/supplier_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/supplier_form.html'
    success_url = reverse_lazy('suppliers:supplier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Novo Fornecedor'
        return context

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/supplier_form.html'
    success_url = reverse_lazy('suppliers:supplier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Editar Fornecedor'
        return context

class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'suppliers/supplier_confirm_delete.html'
    success_url = reverse_lazy('suppliers:supplier_list')
    context_object_name = 'supplier'
