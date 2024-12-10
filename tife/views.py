from django.shortcuts import render , get_list_or_404
from .models import Tife
from django.views import View

# def home(request):
#     return render()


def main(request):
    tife = Tife.objects.all()
    return render(request, 'index.html', {"tife":tife})


def detail(request):
    article = get_list_or_404(Tife, pk=__package__)
    return render(request, 'details.html', {"article":article})



def contact(request):
    return render(request, 'details.html')

# class Detail(View):
#     def get(request,pk):
#         article = get_list_or_404(Tife,pk=pk)
#         return render (request, 'detail.html', {"article": article})