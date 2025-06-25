from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone # Required for date filtering
from django.db.models import Sum, F # Required for annotations

# Import models - uncomment and use as needed
# from products.models import Product
# from customers.models import Customer
# from sales.models import Sale

@login_required # Ensure only logged-in users can access
def dashboard_view(request):
    context = {
        'welcome_message': 'Bem-vindo ao CRM de Semijoias!',
        'new_customers_count': 0,
        'recent_sales_count': 0,
        'low_stock_products_count': 0,
    }
    # Example data fetching (requires models to be migrated and populated):
    # try:
    #     from customers.models import Customer
    #     context['new_customers_count'] = Customer.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7)).count()
    # except Exception: # Broad exception for now, refine later
    #     pass # Keep placeholder if error
    # try:
    #     from sales.models import Sale
    #     context['recent_sales_count'] = Sale.objects.filter(sale_date__gte=timezone.now() - timezone.timedelta(days=7)).count()
    # except Exception:
    #     pass # Keep placeholder if error
    # try:
    #     from products.models import Product
    #     from inventory.models import Inventory # Assuming Inventory model links Product and quantity
    #     # This query is more complex and illustrative
    #     # It assumes 'min_quantity' is part of the Inventory model or accessible via Product
    #     # For simplicity, this example might need adjustment based on final model structure.
    #     # low_stock_products = Inventory.objects.filter(quantity__lt=F('min_quantity')).count()
    #     # context['low_stock_products_count'] = low_stock_products
    # except Exception:
    #     pass
    return render(request, 'core/dashboard.html', context)
