# Lab:
# 	- write a program that prints hello world

print("hello world")

# 	- application to take a number in binary form from the user, and print it as a decimal
def convbindec():
    bin_num = input("enter binary")
    setbin=set(bin_num)
    # print(setbin)
    for n in setbin:
        if n != '1' and n !='0':
            print("not valid")
            return
    dec=int(bin_num, 2)
    print(dec)

convbindec()


# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"

def isdivby(num):
    try:
        num=int(num)
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
            print("Buzz")
    except:
        print("not int")

isdivby(input("is div "))

# 	- Ask the user to enter the radius of a circle print its calculated area and circumference

def calcircle(r):
    radius=float(r)
    area=(22/7)*(radius**2)
    circum=2*(22/7)*radius
    print("area=",area)
    print("circumference",circum)

calcircle(input("circle "))

# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
def user():
    while True:
        name = input("enter name: ").strip()

        if not name:
            print("empty")
            continue

        has_digit = False
        for c in name:
            if c.isdigit():
                has_digit = True
                break

        if has_digit:
            print("have digits")
            continue

        break

    email = input("enter email: ")
    print("name:", name)
    print("email:", email)

            
user()
# 	- Write a program that prints the number of times the substring 'iti' occurs in a string

def caliti(string):
    cnt= string.count('iti')
    for x in range(cnt):
        print("iti")

caliti(input("iti "))