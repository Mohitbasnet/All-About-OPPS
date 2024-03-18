
# Q-3:Computation class
# Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.

# Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method

# Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

# Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

# Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.

# Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

# Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.

class Computation:
    def __init__(self):
        pass

    def Factorial(self, n):
        if n < 0:
            return None 
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

    def naturalSum(self, n):
        if n < 0:
            return None  
        else:
            return (n * (n + 1)) // 2

    def testPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def testPrims(self, num1, num2):
        return self.testPrime(num1) and self.testPrime(num2)

    def tableMult(self, n):
        for i in range(1, 11):
            print(f"{n} * {i} = {n*i}")

    def allTablesMult(self):
        for i in range(1, 10):
            print(f"Multiplication Table for {i}:")
            self.tableMult(i)
            print()

    @staticmethod
    def listDiv(n):
        Ldiv = []
        for i in range(1, n + 1):
            if n % i == 0:
                Ldiv.append(i)
        return Ldiv

    @staticmethod
    def listDivPrim(n):
        Ldiv = []
        for i in range(2, n + 1):
            if n % i == 0 and Computation().testPrime(i):
                Ldiv.append(i)
        return Ldiv


comp = Computation()
print(comp.Factorial(5))  
print(comp.naturalSum(5))
print(comp.testPrime(7))
print(comp.testPrims(4, 9))  
comp.allTablesMult()  
print(Computation.listDiv(12))  
print(Computation.listDivPrim(12))  
