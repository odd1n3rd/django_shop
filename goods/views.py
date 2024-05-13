
from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Product


# Create your views here.
def catalog(request):

    goods = Product.objects.all()
    # paginator = Paginator(goods, 3)
    # current_page = paginator.page(2)

    context = {
        "title": "our goods",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Product.objects.get(slug = product_slug)

    context = {
        'product':product,
    }

    return render(request, "goods/product.html", context=context)
