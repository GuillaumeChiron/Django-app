from django.shortcuts import render
from django.shortcuts import get_object_or_404
from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_details(request, id):
    band = get_object_or_404(Band, id=id)
    return render(request, "listings/band_details.html", {"band": band})


def about(request):
    return render(request, "listings/about.html")


def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings": listings})


def contact(request):
    return render(request, "listings/contact.html")
