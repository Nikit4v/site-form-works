from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)

    form = ReviewForm
    is_exist = False
    if request.method == 'POST':
        for object in Review.objects.all():
            if object.csrf == request.POST["csrfmiddlewaretoken"]:
                is_exist = True
        if not is_exist:
            review = Review()
            review.product = product
            review.text = request.POST["text"]
            review.csrf = request.POST["csrfmiddlewaretoken"]
            review.save()

    context = {
        'reviews': Review.objects.all(),
        'form': form,
        'product': product
    }

    return render(request, template, context)
