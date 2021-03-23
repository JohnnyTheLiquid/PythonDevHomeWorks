def val_checker(condition):
    def _val_checker(func):
        def checker(args):
            if condition(args):
                return func(args)
            else:
                raise ValueError(f'wrong val {args}')
        return checker
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(5))
print(calc_cube(-5))
