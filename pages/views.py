from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<p>hello</p>")
    return render(request, "pages/home.html", {})

# the website requests the function
# the fuction returns back a response
# request is a GET request

def contact_view (request, *args, **kwargs):
    return render(request, "pages/contact.html", {})

def about_view(request, *args, **kwargs):
    context = {
        "my_text":"prabodh",
        "my_number":123,
        "my_list":[1,12,123],
        "my_html": "<h1>This is a html</h1>",
    }
    return render(request, "pages/about.html", context)

