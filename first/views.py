import random

from django.shortcuts import render
from datetime import datetime


def index(request):
    message = "this page is index page!!!"
    now = datetime.now()
    context = {
        'current_date' : now,
        'message' : message
    }
    return render(request, 'first/index.html', context)


def lotto(request):
    lotto_numbers = []

    while len(lotto_numbers) < 7:
        lotto_num = random.randint(1, 45)
        if lotto_num in lotto_numbers:
            lotto_num = random.randint(1, 45)
        lotto_numbers.append(lotto_num)

    context = {
        'lotto_numbers' : lotto_numbers
    }
    return render(request, 'first/lotto.html', context)


def select(request):
    message = "this page is select page!!!"
    context = {
        'number' : 5,
        'numbers' : [1, 2, 3, 4, 5, 6, 7],
        'message': message
    }
    return render(request, 'first/select.html', context)


def result(request):
    message = "this page is result page!!!"
    context = {
        'number': 10,
        'message': message
    }
    return render(request, 'first/result.html', context)