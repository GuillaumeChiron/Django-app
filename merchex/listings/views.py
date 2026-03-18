from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    return HttpResponse("<h1>About-us</h1> <p>Nous adorons Merch !!!</p>")


def listings(request):
    return HttpResponse(
        "<h1>Listings</h1> "
        "<ul>"
        "<li>first merch</li>"
        "<li>second merch</li>"
        "<li>third merch</li>"
        "</ul>"
    )


def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>contact@gmail.com</p>")
