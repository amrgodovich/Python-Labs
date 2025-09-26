import csv
import random

def random_data_generator():
    while True:
        try:
            n = int(input("How many random numbers to generate? "))
            if n > 0:
                break
            else:
                print("enter a number > 0")
        except ValueError:
            print("Enter an integer > 0.")


    numbers = [random.randint(1, 100) for _ in range(n)]


    filename = "random_numbers.csv"
    with open(filename, "w") as f:
        f.write("index,value\n")
        idx=0 
        for val in numbers:
            idx+=1
            f.write(f"{idx},{val}\n")

    avg = sum(numbers) / len(numbers)

    print(f"random numbers r saved to '{filename}")
    print(f"Average value: {avg}")

# random_data_generator()