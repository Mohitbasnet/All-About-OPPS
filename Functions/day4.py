def func_a():
    print("Inside func_a")

def func_b(x):
    print('Inside func_b')
    return x()
print(func_b(func_a))




























