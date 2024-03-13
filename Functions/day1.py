def greet(first_name, last_name):
    print(f"hi {first_name}")
    print("hey dear")


greet("Mohit", "Rohit")    





# Types of the functions
# 1- Perform a task
# 2 - Return a value



def get_greeting(name):
    return f"hi {name}"

message  = get_greeting("mohit")
file = open("content.txt", "w")
file.write(message)





def increment(number, by):
    return number + by

result = increment(21,by=1)
print(result)



# *args
def multiply(*num):
    print(num)


multiply(9,3,2,3,24,4)    



# ***args

def save_user(**user):
    print(user["age"])

save_user(id=1,name = "Mohit", age = 2 )




# scope

message = "a"
def greet(name):
    global message 
    message = "h"
def send_email(name):

    message = "b"


greet("hlep")
print (message)