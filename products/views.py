
from django.shortcuts import render

from .models import Products
from .forms import ProductForm, RawProductForm


# Create your views here.

def product_create_view(request):

    # DJANGO MODEL FORMS USING form.as_p() in html
    # form = ProductForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = ProductForm()
    #
    # context = {
    #     'form': form
    # }

    # RAW HTML FORMS
    # print(request.POST)
    # name = request.POST.get('title')
    # print("name " + name)



    form = RawProductForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        Products.objects.create(**form.cleaned_data)
    context = {
        'form' : form,
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Products.objects.get(id=1)

    # context = {
    #     'title': obj.title,
    #     'description':obj.description,
    # }

    context = {
        'product': obj  # pass the object as a context
    }
    return render(request, "products/detail.html", context)
