def validate_coma_list(prompt="Enter numbers (comma-separated): "):
    while True:
        user_input = input(prompt)
        try:
            numbers = [float(num.strip()) for num in user_input.split(",")]
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

def validate_coma_list_st(prompt="Enter strings (comma-separated): "):
    while True:
        user_input = input(prompt)
        try:
            numbers = [str(num.strip()) for num in user_input.split(",")]
            return numbers
        except ValueError:
            print("Invalid input. Please enter strings separated by commas.")
