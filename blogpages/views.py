from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm

# Create your views here.

#Home View start
def home_page(request):
    form = ContactForm

    # handling form submission for contact form
    if request.method == "POST":
        print(request.POST)
        form = ContactForm(request.POST)

        # validating contact form
        if form.is_valid():

            # adding custom form here if form is valid
            contact = Contact(
                # connectng username model with custom input form
                username = form.cleaned_data["username"],
                # ------------------------------------------> ends
                # connectng emalmodel with custom input form
                email = form.cleaned_data["email"],
                # ------------------------------------------> ends
                # connectng subject model with custom input form
                subject = form.cleaned_data["subject"],
                # ------------------------------------------> ends
                # connectng message model with custom input form
                message = form.cleaned_data["message"]
            )
            # saves the contact form to the admin site
            contact.save()
            # return HttpResponse("successful")
            page = "seccessfull"
            return render(request, 'SubmitSuccessfulandError.html', {'successful': True, "page":page})
        else:
            return render(request, 'SubmitSuccessfulandError.html', {'error': True})
    else:
        form = ContactForm()

    # adding context for the form
    context = {"form":form}
    
    # renders the template for the home page
    return render(request, 'blogpages/index.html', context)
# home page view ends
# ----------------------------------------------------------------------------> ends

# portfolio details start
def portfolio_details(request):
    return render(request, 'blogpages/portfolio-details.html')
# portfolio details view ends
# ----------------------------------------------------------------------------> ends

# services page view start
def services_page(request):
    return render(request, 'blogpages/service-details.html')
# service page view ends
# -----------------------------------------------------------------------------> ends

# all testmonial view start
def all_testimonials(request):
    return render(request, 'blogpages/all-testimonials.html')
# all testimonial view ends