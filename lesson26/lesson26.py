def call_counter(path):

    def decorator(func):

        def wrapper(*args, **kwargs):

            wrapper.counter += 1

            with open(path, 'a') as a_file:
                a_file.write(f'Function {func.__name__} was called {wrapper.counter} times\n')

            return func(*args, **kwargs)

        wrapper.counter = 0

        return wrapper

    return decorator

@call_counter('counter.txt')
def add(a, b):
    return a + b

print(add(4, 6))
print(add(3, 5))
print(add(3, 5))
