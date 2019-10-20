from django.shortcuts import render
from .models import CompanyData, FourInfo

# Create your views here.


def index(request):
    company_info = CompanyData.objects.all()[:1]
    four_infos = FourInfo.objects.all()
    context = {
        'company_info': company_info[0],
        'four_infos': four_infos
    }
    # print(context['CompanyName'])
    # print(context['title'])
    return render(request, 'four/index.html', context=context)

