from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices, status_choices, rent_choices

from listings.models import Listing
from managers.models import Manager

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'status_choices': status_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'rent_choices': rent_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    managers = Manager.objects

    # Get MVP
    mvp_managers = Manager.objects.all().filter(is_mvp=True)

    context = {
        'managers': managers,
        'mvp_manager': mvp_managers
    }

    return render(request, 'pages/about.html', context)
