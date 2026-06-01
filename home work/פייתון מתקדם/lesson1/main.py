import time

# ex1
def deco(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        return (end - start)
    return wrapper


@deco
def say_hi():
    print('hello')
print(say_hi())

# ex2
# def deco2(func):
#     memo = {}
#     def wrapper2(n):
#         start = time.perf_counter()
#         if n not in memo:
#             memo[n] = func(n)
#         end = time.perf_counter()
#         print(end-start)
#         return memo.get(n)
#     return wrapper2
# @deco2
# def fibonacci(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         print(a, end=" ")
#         a, b = b, a + b
#         count += 1
#     return  b
# print(fibonacci(10))
# print(fibonacci(10))


def deco2(func):
    memo = {}
    def wrapper2(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper

@deco2
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    return a

print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(5)







