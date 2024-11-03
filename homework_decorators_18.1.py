def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with arguments {args} and keyword arguments {kwargs}. Result: {result}")
        return result
    return wrapper

@log_arguments_and_result
def add(a, b):
    return a + b

add(3, 4)

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An exception occurred in function '{func.__name__}': {e}")
            return None
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

divide(4, 2)
divide(4, 0)

