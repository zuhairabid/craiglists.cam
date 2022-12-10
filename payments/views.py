from coinbase_commerce.client import Client
from django.shortcuts import render

from core import settings


def home_view(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
        'local_price': {
            'amount': '0.10',
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': 'https://craigslist.cam/' + 'success/',
        'cancel_url': 'https://craigslist.cam/' + 'cancel/',
    }
    charge = client.charge.create(**product)

    return render(request, 'home.html', {
        'charge': charge,
    })

    
def success_view(request):
    return render(request, 'success.html', {})


def cancel_view(request):
    return render(request, 'cancel.html', {})