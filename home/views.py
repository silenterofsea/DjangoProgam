from django.shortcuts import render
from django.views import generic
from .models import ProductsList, MyCompanyInfo
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, HttpResponse


# Create your views here.


class ProductsIndexView(generic.ListView):
    model = ProductsList
    template_name = 'home/products.html'
    context_object_name = 'products_list'

    def get_queryset(self):
        return ProductsList.objects.all()


class ProductDetailsView(generic.DetailView):
    model = ProductsList
    template_name = 'home/product_details.html'


def home_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('successful!')
            # 123123123
            client_name = form.cleaned_data['client_name']
            client_email = form.cleaned_data['client_email']
            client_phone = form.cleaned_data['client_phone']
            client_message = form.cleaned_data['client_message']
            print(client_name, client_email, client_phone, client_message)
            # return HttpResponseRedirect('/home?submitted=True')
            # return HttpResponseRedirect(reverse("home:home"))
            return HttpResponse('提交成功')
            # return HttpResponse("Successfully submitted")
        else:
            form = ContactForm()
            my_info = MyCompanyInfo.objects.all()[0]

            context = {
                'my_info': my_info,
                'form': form
            }
            return render(request, 'home/index.html', context=context)
            # return render(request, 'home/index.html', form=form)
    form = ContactForm()
    my_info = MyCompanyInfo.objects.all()[0]

    context = {
        'my_info': my_info,
        'form': form
    }
    return render(request, 'home/index.html', context=context)


def home_products(request):
    context = {
        'title': 'I am home_products'
    }
    return render(request, 'home/products.html', context=context)


def home_product_details(request):
    context = {
        'title': 'I am home_product_details'
    }
    return render(request, 'home/product_details.html', context=context)
