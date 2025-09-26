from Task.task1 import math_automation
from Task.task2 import regex_log_cleaner
from Task.task3 import reminder
from Task.task4 import product_data_transformer
from Task.task5 import os_file_manager
from Task.task6 import random_data_generator

def mainmenu():
    tasks = {
        "1": math_automation,
        "2": regex_log_cleaner,
        "3": reminder,
        "4": product_data_transformer,
        "5": os_file_manager,
        "6": random_data_generator,
    }

    while True:
        print("Python Practice Tasks")
        print(" ")
        print("1: Math Automation")
        print("2: Regex Log Cleaner")
        print("3: Datetime Reminder Script")
        print("4: Product Data Transformer")
        print("5: OS File Manager")
        print("6: Random Data Generator")
        # print("7: Decorators Task")
        print("0: Quit")

        choice = input("Choose: ")
        if choice == "0":
            print("Quitting")
            break
        elif choice in tasks:
            tasks[choice]()
        else:
            print("Invalid choice!!")



if __name__ == "__main__":
    mainmenu()
