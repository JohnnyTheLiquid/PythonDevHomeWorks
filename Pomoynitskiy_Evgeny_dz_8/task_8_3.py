def type_logger(func):
    def types(*args):
        return 'function call: {0}({1}: {2})'.format(func.__name__, *args, type(*args))
    return types

@type_logger
def calc_cube(x):
    return x ** 3

print(calc_cube(5))
