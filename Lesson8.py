import time

# Напишите свой генератор последовательностей, свой тернарный оператор


def where(enum, f):
    for item in enum:
        if f(item):
            yield item


def ter(cond, on_true, on_false):
    return on_true if cond else on_false


# Напишите свой декоратор
def some_decorator(f):
    def wrapper(*args, **kwargs):
        print('decorated')
        f(*args, **kwargs)

# Напишите декоратор, замеряющий время выполнение декорируемой функции.


def log_execution_time(f):
    def wrapper():
        start = time.process_time()
        result = f()
        elapsed = time.process_time() - start
        print(f'Elapsed time {elapsed} on execution')
        return result, elapsed
    return wrapper
# Сравните время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
# (создание объектов оформить в виде функций).


@ log_execution_time
def list_gen():
    return [x+1 for x in range(1, 1_000_001)]


def gen():
    for i in range(1, 1_000_001):
        yield i


@ log_execution_time
def list_2_gen():
    items = []
    for i in gen():
        items.append(i)
    return items


result_tuple = list_gen()
result_tuple_2 = list_2_gen()
print('generator', ter(result_tuple[1] - result_tuple_2[1] >= 0, 'faster', 'slower'))


