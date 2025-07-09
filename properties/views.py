from django.shortcuts import render, get_object_or_404
from .models import Property
from django.core.paginator import Paginator

# 🔹 Home Page with Search + Filters + Pagination
def home(request):
    purpose = request.GET.get('purpose')
    query = request.GET.get('query')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    property_type = request.GET.get('property_type')

    properties = Property.objects.all()

    if purpose:
        properties = properties.filter(purpose=purpose)
    if query:
        properties = properties.filter(title__icontains=query) | properties.filter(location__icontains=query)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    if property_type:
        properties = properties.filter(property_type=property_type)

    paginator = Paginator(properties, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'page_obj': page_obj,
        'selected_purpose': purpose,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'selected_type': property_type
    })

# 🔹 Property Detail View
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property': property})

# 🔹 Contact Page
def contact(request):
    return render(request, 'contact.html')

# 🔹 Buy / Rent / Sell Pages
def buy_properties(request):
    properties = Property.objects.filter(purpose='buy')
    return render(request, 'property_list.html', {'properties': properties, 'page_title': 'Buy Properties'})

def rent_properties(request):
    properties = Property.objects.filter(purpose='rent')
    return render(request, 'property_list.html', {'properties': properties, 'page_title': 'Rent Properties'})

def sell_properties(request):
    properties = Property.objects.filter(purpose='sell')
    return render(request, 'property_list.html', {'properties': properties, 'page_title': 'Sell Properties'})
