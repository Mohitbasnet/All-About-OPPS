# def power(a,b):
#     return a*b
# power(3,5) 



def flexi(*number):
    product = 1
    for i in number:
        product = product * i
    print(product)


flexi(1,8,9)