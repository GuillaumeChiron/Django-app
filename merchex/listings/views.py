from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from listings.models import Band, Listing
from listings.forms import ContactUsForm


def home_page(request):
    return render(request, "listings/home_page.html")


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


def listing_details(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, "listings/listings_details.html", {"listing": listing})


def contact(request):

    if request.method == "POST":
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("email-sent")

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request, "listings/contact.html", {"form": form})


def email_sent(request):
    return render(request, "listings/email_sent.html")
