from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices, status_choices, rent_choices
from listings.forms import MaintenanceForm
from .models import Listing, Maintenance

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def properties(request):
  listings = Listing.objects.order_by('-list_date')

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/properties.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)


def maintenance(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.listing = listing
            maintenance.save()
            return redirect('listing', pk=listing.listing_id)
        else:
            form = MaintenanceForm()
        return render(request, 'listing/listings.html', {'form': form})

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
        desc = queryset_list.filter(description__icontains=keywords)
        if desc.count() == 0:
            queryset_list = queryset_list.filter(title__icontains=keywords)
        else:
            queryset_list = queryset_list.filter(description__icontains=keywords)



  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # City
  if 'neighborhood' in request.GET:
    neighborhood = request.GET['neighborhood']
    if neighborhood:
      queryset_list = queryset_list.filter(neighborhood__iexact=neighborhood)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Status
  if 'status' in request.GET:
    status = request.GET['status']
    if status:
      queryset_list = queryset_list.filter(status__iexact=status)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
        queryset_list = query_list.filter(status__=status)


  context = {
    'state_choices': state_choices,
    'status_choices': status_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)

def guest_search(request):
  queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
        desc = queryset_list.filter(description__icontains=keywords)
        if desc.count() == 0:
            queryset_list = queryset_list.filter(title__icontains=keywords)
        else:
            queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
        queryset_list = queryset_list.filter(asking_price__lte=price)

  # Rent
  if 'rent' in request.GET:
    rent = request.GET['rent']
    if rent:
        queryset_list = queryset_list.filter(target_rent__lte=rent)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'rent_choices': rent_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)
