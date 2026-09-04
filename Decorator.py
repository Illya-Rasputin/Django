from functools import wraps


def log_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Arguments passed to {func.__name__}: args={args}, result={result}")
        return result
    return wrapper

def check_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        password = kwargs.get("password", args[0] if args else None)
        if password != "admin123":
            print("Доступ заборонено. Невірний пароль.")
            return
        return func(*args, **kwargs)
    return wrapper
       


@log_arguments
def Add(a, b):
    return a + b

@check_access
def password(password):
    print("Вітаю! Ви отримали доступ.")

Add(5, 3)
password("admin123")