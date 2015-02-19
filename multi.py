from celery import Celery

app = Celery(backend='amqp', broker='amqp://')


@app.task()
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


# primes = [15485689, 15485711]


# def calculate():
#     for prime in primes:
#         is_prime(prime)


# def calculate_task():
#     for prime in primes:
#         is_prime.delay(prime)

# primes = [15485669, 15485677, 15485689, 15485711, 15485737, 15485747,
#           15485761, 15485773,   15485783, 15485801, 15485807, 15485837,
#           15485843, 15485849, 15485857, 15485863]
