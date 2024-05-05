# ФУНКЦІЯ caching_fibonacci
def caching_fibonacci(n):
#     Створити порожній словник cache
    cache = {}
#     ФУНКЦІЯ fibonacci(n)
    def fibonacci(n):
#         Якщо n <= 0, повернути 0
        if n <= 0:
            return 0
#         Якщо n == 1, повернути 1
        elif n == 1:
            return 1
#         Якщо n у cache, повернути cache[n]
        elif n in cache:
            return cache[n]
#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         Повернути cache[n]
        return cache[n]
#     Повернути функцію fibonacci
    return fibonacci
# КІНЕЦЬ ФУНКЦІЇ caching_fibonacci
fib = caching_fibonacci(55)

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(55))  
