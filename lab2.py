import random



    # 1 - Ask the user to enter 5 numbers.
    #     Store them, then display them in ascending order and descending order.
def ls_order():
    num = []
    print("Enter 5 numbers:")
    while (len(num)<5):
        try:
            n=int(input("Enter number: "))
            num.append(n)
        except:
            print("not vaild number, , enter int")
    print("Ascending:", sorted(num))
    print("Descending:", sorted(num, reverse=True))


    # 2 - Write a function that takes two numbers: (length, start).
    #     Generate a sequence of numbers with the given length,
    #     starting from the given start number and increasing by one each time.
    #     Print the result.

def validate_int(usrinput):
    while True:
        try:
            return int(input(usrinput))
        except ValueError:
            print("not valid input. enter int.")

def seq():
    length = validate_int("Enter sequence length: ")
    start = validate_int("Enter start number: ")
    sequence=[]
    for i in range(length):
            sequence.append(start + i)
    print("resulted seq:", sequence)



    # 3 - Keep asking the user for numbers until they type "done".
    #     When finished, print:
    #         * The total of all numbers entered
    #         * The count of valid entries
    #         * The average
    #     If the user enters something invalid, show an error and continue.
def cal_numbers():
    nums = []
    while True:
        inputt = input("Enter a number (type 'done' to exit): ")
        if inputt == "done":
            break
        try:
            nums.append(float(inputt))
        except ValueError:
            print("not valid number! use int or float")
    if nums:
        total = sum(nums)
        count = len(nums)
        avg = total / count
        print(f"Total = {total}, Count = {count}, Average = {avg}")
    else:
        print("numbers doent exist.")


    # 4 - Ask the user to enter a list of numbers.
    #     Remove any duplicates, sort the result, and display it
def del_dupliacte():
    print("enter number separated by sapce")
    while True:
        try:
            nums = list(map(int,input().split()))
            sort_sett = sorted(set(nums))
            print("ordered sorted set:", sort_sett)
            break
        except ValueError:
            print("not valid number, int separted by space ")



    # 6 - Ask the user to enter a sentence.
    #     Count how many times each word appears in the sentence
    #     and display the result.
def word_count():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    counts = {}
    for word in set(words): 
        counts[word] = words.count(word)
    print("Word counts:")
    for word, count in counts.items():
        print(f"{word}: {count}")


    # 7 - Create a small gradebook system:
    #     - The user enters 5 students names and their scores.
    #     - At the end, show:
    #         * The highest score
    #         * The lowest score
    #         * The average score.
def gradbook_sys():
    students = {}
    
    while len(students) < 2:
        name = input("Enter name for student: ")
        while True:
            try:
                score = float(input(f"Enter score for {name}: "))
                break
            except ValueError:
                print("Invalid input! enter number for score.")
        
        students[name] = score

    first_name = list(students.keys())[0]
    highest_name = lowest_name = first_name
    highest_score = lowest_score = students[first_name]
    total = 0
    scores=list(students.values())
    total= sum(scores)

    for name, score in students.items():
        if score > highest_score:
            highest_score = score
            highest_name = name
        if score < lowest_score:
            lowest_score = score
            lowest_name = name

    avg_score = total / len(students)

    print("Highest score:", highest_score, "by", highest_name)
    print("Lowest score:", lowest_score, "by", lowest_name)
    print("Average score:", avg_score)

    # 8 - Write a program that simulates a shopping cart:
    #     - The user can add items with a name and a price.
    #     - The user can remove items by name.
    #     - The user can view all items with their prices.
    #     - At the end, display the total cost.
def shopping():
    cart = {}
    while True:
        print("Shopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View items")
        print("4. Checkout")
        choice = input("Choose any option: ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                cart[name] = price
            except ValueError:
                print("Invalid price! Must be a number.")

        elif choice == "2":
            name = input("Enter item name to remove: ")
            if name in cart:
                del cart[name]
            else:
                print("Item not found.")

        elif choice == "3":
            if not cart:
                print("Cart is empty.")
            else:
                for name, price in cart.items():
                    print(f"{name}: ${price}")

        elif choice == "4":
            total = sum(cart.values())
            print("Final Cart:", cart)
            print("Total cost:", total)
            break
        else:
            print("Invalid choice! Please enter 1-4.")


    # 9 - Create a number guessing game:
    #     - The program randomly selects a number between 1 and 20.
    #     - The user keeps guessing until they get it right.
    #     - After each guess, show if the guess was too high or too low.
    #     - When correct, display the number of attempts.
def guess_secret():
    secret = random.randint(1, 20)
    attempts = 0
    print("Guess int number between 1 - 20")
    while True:
        guess = validate_int("Your guess: ")
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! The number was {secret}. Attempts: {attempts}")
            break



def mainmenu():
    tasks = {
        "1": ls_order,
        "2": seq,
        "3": cal_numbers,
        "4": del_dupliacte,
        "6": word_count,
        "7": gradbook_sys,
        "8": shopping,
        "9": guess_secret,
    }

    while True:
        print("Python Practice Tasks")
        print(" ")
        print("1: List in order")
        print("2: Sequence")
        print("3: Numbers calculations")
        print("4: Rm duplicates")
        print("6: Word count")
        print("7: Gradebook")
        print("8: Shopping cart")
        print("9: Guess secret")
        print("0: Quit")

        choice = input("Choose: ")
        if choice == "0":
            print("Quitting")
            break
        elif choice in tasks:
            tasks[choice]()
        else:
            print("Invalid choice!!")



mainmenu()
