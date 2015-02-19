from celery import Celery

from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import PrimeForm


app = Celery('tasks', backend='amqp', broker='amqp://')


def is_prime(n):

    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    # for x in range(3, int(n**0.5)+1, 2):
    #     if n % x == 0:
    #         return False
    return True


class PrimeView(FormView):
    template_name = 'prime.html'
    form_class = PrimeForm

    def form_valid(self, form):
        number = form.cleaned_data['number']
        if is_prime(number):
            message = str(number) + " is prime."
        else:
            message = str(number) + " is NOT prime."

        return render(self.request, 'prime.html', {'result': message})


@app.task()
def test_prime(number):
    message = "Result will be show soon."
    result = is_prime(number)
    if result:
        message = str(number) + " is prime."
    else:
        message = str(number) + " is NOT prime."
    return message


class PrimeAsyncView(FormView):
    template_name = 'prime-async.html'
    form_class = PrimeForm

    def form_valid(self, form):
        number = form.cleaned_data['number']
        result = test_prime.delay(number)
        message = "Result will be shown soon!"
        return render(self.request, 'prime-async.html', {'result': message})
