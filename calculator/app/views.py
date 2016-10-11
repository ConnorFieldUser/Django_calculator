from django.shortcuts import render

from app.models import Calc

# Create your views here.


def index_view(request):
    print(request.POST)
    if request.POST:
        num_1 = request.POST["num_1"]
        num_2 = request.POST["num_2"]
        if type(num_1) == 'int' and type(num_2) == 'int':
            Calc.objects.create(num_1=num_1, num_2=num_2)
    context = {
    }
    return render(request, 'index.html', context)
