def plus(a, b):
    try:
        return a + b
    except TypeError as e:
        raise e("Only numbers are allowed")

if __name__ == "__main__":
    print(plus(1,2))