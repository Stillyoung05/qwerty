
"""Sum1"""
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# numbers_list = [2, 3, 5, 7, 11, 13, 4, 8, 9, 15]
#
# iterator = iter(numbers_list)
#
# prime_nums = [num for num in iterator if is_prime(num)]
#
# print("Prime numbers: ", prime_nums)


"""Sum2"""


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def get_twin_primes(numbers):
#     iterator = iter(numbers)
#     twin_primes = []
#
#     try:
#         while True:
#             current_number = next(iterator)
#             next_number = next(iterator)
#
#             if is_prime(current_number) and is_prime(next_number) and abs(current_number - next_number) == 2:
#                 twin_primes.append((current_number, next_number))
#
#     except StopIteration:
#         pass
#
#     return twin_primes
#
#
# inp_nums = input()
# numbers_list = [int(a) for a in inp_nums.split()]
#
# twin_primes = get_twin_primes(numbers_list)
#
# print("Twin primes:", twin_primes)


"""Sum3"""


# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
#
# def get_leap_years(years):
#     iterator = iter(years)
#     leap_years = []
#
#     try:
#         while True:
#             current_year = next(iterator)
#             if is_leap_year(current_year):
#                 leap_years.append(current_year)
#
#     except StopIteration:
#         pass
#
#     return leap_years
#
#
# inp_nums = input()
# years_list = [r for r in inp_nums]
#
# leap_years = get_leap_years(years_list)
#
# print("Leap years:", leap_years)


"""Sum4"""


def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_numbers(user_input_list):
    user_input_list = [int(m) for m in input().split()]
    fibonacci_generator = generate_fibonacci()
    fibonacci_numbers = []

    for _ in range(len(user_input_list)):
        fib_number = next(fibonacci_generator)
        if fib_number in user_input_list:
            fibonacci_numbers.append(fib_number)

    return fibonacci_numbers


fibonacci_numbers = get_fibonacci_numbers()
print("Fibonacci numbers in the input list are :", fibonacci_numbers)
