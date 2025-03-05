from django.shortcuts import render
from .models import Contact


# Create your views here.
def contact_view(request):
    contact = Contact.objects.all().first()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact}
    )
