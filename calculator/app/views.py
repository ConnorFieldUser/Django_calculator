from django.shortcuts import render

# Create your views here.


def index_view(request):
    print(request.POST)
    context = {
        "number1": '',
        "number2": '',
        "operator": ''
    }
    if request.POST:
        number1 = int(request.POST['num_1'])
        number2 = int(request.POST['num_2'])
        operator = request.POST['operator']
        print()

        if operator == '+':
            new = number1 + number2
        elif operator == '-':
            new = number1 - number2
        elif operator == '*':
            new = number1 * number2
        elif operator == '/':
            new = number1 / number2
        context['newnum'] = new
        print(new)
        context['1'] = number1
        context['op'] = operator
        context['2'] = number2

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
