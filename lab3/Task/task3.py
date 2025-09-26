from datetime import datetime,date

def reminder():
    while True:
        usr_date=input("Enter a date (YYYY-MM-DD)")
        try:
            target_date = datetime.strptime(usr_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    today_date=date.today()

    diff= target_date-today_date
    diff_days=diff.days

    if diff_days<0:
        print("dat already passed")
    else:
        rem_file="reminder.txt"
        with open(rem_file,"a") as f:
            f.write(f"{target_date} ---> {diff_days} days left \n")

            print("reminder saved")
            print(f"{target_date} ---> {diff_days} days left \n")

# reminder()