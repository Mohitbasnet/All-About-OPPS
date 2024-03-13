def is_even(number):
    """
    This function tells if a given number is odd or even
    Input- any valide integer
    output - odd/even
    created by - Mohit
    Last edited - 15 jan 2023


    """
    if type(number) == int:

       if number % 2 == 0:
           return 'Even'
       else:
           return 'Odd'
    else:
        return "Not allowed"
for i in range(1,11):
    print(is_even(i))  