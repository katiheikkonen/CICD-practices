def plus(a, b):
    try:
        return a + b
    except TypeError as e:
        raise e("Only numbers are allowed")