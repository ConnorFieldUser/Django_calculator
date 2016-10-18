from django.shortcuts import render

# Create your views here.


def index_view(request):
    print(request.POST)
    context = {
    }
    return render(request, 'index.html', context)

# >>> d = {
# ...   "number1": 4,
# ...   "number2": 9,
# ...   "operator": "+"
# ... }
# >>> d
# {'number2': 9, 'number1': 4, 'operator': '+'}
# >>>
# >>> d
# {'number2': 9, 'number1': 4, 'operator': '+'}
# >>> # if the operator is a plus, add the two numbers together
# ...
# >>> if d['operator'] == '+':
# ...     new = d['number2'] + d['number1']
# ...
# >>> print(new)
# 13
# >>>
