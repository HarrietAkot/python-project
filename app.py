num1 = ["3", "6", "9", "12", "15"]
num2 = ["5", "10", "15", "20", "25"]
num3 = num1 + num2
num4 = len(num3)

def Fizzbuzz(num):
    if ((num % 5 == 0) & (num % 3 == 0)):
        print("Fizzbuzz")
    elif (num % 5 == 0):
        print("Buzz")
    elif (num % 3 == 0):
        print("Fizz")
    else:
        print("Not divisible")

Fizzbuzz(num4)