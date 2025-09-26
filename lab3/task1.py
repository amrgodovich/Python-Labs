# 1) Math Automation
#    - Create a file called "math_report.txt".
#    - Ask the user for multiple numbers (comma-separated).
#    - For each number, calculate:
#         - floor, ceil, square root, area of a circle
#    - Write the results into "math_report.txt".
#    - Confirm file was created and print its content.
import math
from helpers import validate_coma_list
from task7 import log_time

@log_time
def math_automation():
    numbers = validate_coma_list()
    filename = "math_report.txt"
    with open(filename, "w") as f:
        f.write("Math Report\n")
        for num in numbers:
            f.write(f"Number: {num}\n")
            f.write(f"  Floor: {math.floor(num)}\n")
            f.write(f"  Ceil: {math.ceil(num)}\n")
            f.write(f"  Square Root: {math.sqrt(num)}\n")
            f.write(f"  Area of Circle: {(22/7) *math.sqrt(num)}\n")
            f.write("----------------\n")
        f.write("------------------------\n")

    print(f"\n '{filename}' is created \n")
    with open(filename, "r") as f:
        print(f.read())

if __name__ == "__main__":
    math_automation()

