from django.shortcuts import render

from goods.models import Product


# Create your views here.
def catalog(request):

    goods = Product.objects.all()
    context = {
        "title": "our goods",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    context = {
        "title": "chicha home page",
        "content": "bueeeeeeeeeeeeee"
          }
    return render(request, "goods/product.html", context)
