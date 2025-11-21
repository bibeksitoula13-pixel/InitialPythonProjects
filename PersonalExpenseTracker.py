from datetime import datetime
import csv
import calendar

TempDict = []
def read():
    global TempDict
    TempDict.clear()
    try:
        with open("ExpenseTracker.csv","r") as exp_tra_file:
            csv_reader = csv.DictReader(exp_tra_file)
            for line in csv_reader:
                TempDict.append(line)
                print (line)
    except FileNotFoundError:
        with open("ExpenseTracker.csv","w") as exp_tra_file:
            fieldnames = ["Expense","Date","Category","Amount","Description"]
            csv_writer = csv.DictWriter(exp_tra_file, fieldnames=fieldnames)
            csv_writer.writeheader()

def write():
    global TempDict
    try:
        with open("ExpenseTracker.csv","a") as exp_tra_file:
            csv_writer = csv.DictWriter(exp_tra_file,fieldnames=["Expense","Date","Category","Amount","Description"])
            while True:
                expense = input("Enter the expense: ")
                while True:
                    date = input("Enter date of expense(yyyy-mm-dd): ")
                    try:
                        date_obj = datetime.strptime(date, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Invalid date")
                category = input(
                    "Enter category of expense\n"
                    "Food\n"
                    "Clothes\n"
                    "Rent\n"
                    "Entertainment\n"
                    "Other\n>"
                ).lower()
                while True:
                    amount = input("Enter amount of expense: ")
                    if amount.isdigit():
                        amount = int(amount)
                        break
                    else:
                        print("Amount must be a number")
                description = input("Enter description of expense: ")

                expense_entry = {"Expense":expense,"Date":date_obj.strftime("%Y-%m-%d"),"Category":category,"Amount":amount,"Description":description}
                TempDict.append(expense_entry)
                csv_writer.writerow(expense_entry)
                usr_option = input("would you like to add more?[y/n]")
                if usr_option == "n":
                    break
    except FileNotFoundError:
        print("File not found")

def total_expense():
    global TempDict
    total = 0
    for items in TempDict:
        total = total+int(items["Amount"])
    return total

def expense_by_category():
    global TempDict
    food_expense = 0
    rent_expense = 0
    entertainment_expense = 0
    clothes_expense = 0
    others_expense = 0
    cat_list = []
    amt_list = []
    for items in TempDict:
        cat_list.append(items["Category"])
        amt_list.append(int(items["Amount"]))
    for i in range(0,len(cat_list)):
        if cat_list[i] == "food":
            food_expense = food_expense+amt_list[i]
        elif cat_list[i] == "rent":
            rent_expense = rent_expense+amt_list[i]
        elif cat_list[i] == "entertainment":
            entertainment_expense = entertainment_expense+amt_list[i]
        elif cat_list[i] == "clothes":
            clothes_expense = clothes_expense+amt_list[i]
        else:
            others_expense = others_expense+amt_list[i]
    avg_food_expense = (food_expense / total_expense()) *100
    avg_rent_expense = (rent_expense / total_expense()) *100
    avg_entertainment_expense = (entertainment_expense / total_expense()) *100
    avg_clothes_expense = (clothes_expense / total_expense()) *100
    avg_others_expense = (others_expense / total_expense()) *100
    print(f"Total food expense is: {food_expense}, and it is {round(avg_food_expense,2)}% of total\n Total "
          f"rent expense is: {rent_expense}, and it is {round(avg_rent_expense,2)}% of total\n Total "
          f"entertainment expense is: {entertainment_expense}, and it is {round(avg_entertainment_expense,2)}% of total\n Total"
          f" clothes expense is: {clothes_expense}, and it is {round(avg_clothes_expense,2)}% of total\n Total"
          f" other expense is: {others_expense}, and it is {round(avg_others_expense,2)}% of total.")

def monthly_report(income_month):
    global TempDict
    Current_Month = datetime.now().month
    Current_Year = datetime.now().year
    total = 0
    totalpre = 0
    highest = 0
    lowest = float("inf")
    transactions = 0
    for items in TempDict:
        amt = int(items["Amount"])
        date_obj = datetime.strptime(items["Date"], "%Y-%m-%d")

        if date_obj.month == Current_Month and date_obj.year == Current_Year:
            total += amt
            transactions += 1
            highest = max(highest, amt)
            lowest = min(lowest, amt)

        pre_month = Current_Month-1 if Current_Month > 1 else 12
        if date_obj.month == pre_month:
            totalpre += amt

    if lowest == float("inf"):
        lowest = 0

    print(f"Monthly Summary ({calendar.month_name[Current_Month]})")
    print(f"_"*50)
    print(f"Total Income: {income_month}")
    print(f"Total Expenses: {total}")
    print(f"Net Savings: {income_month-total}\n")
    print(f"Total Transactions: {transactions}")
    print(f"Highest Expense: {highest}")
    print(f"Lowest Expense: {lowest}")
    print(f"Previous Month Expenses: {totalpre}")

def main():
    read()
    while True:
        usr_choice = input(
            "\nChoose an option:\n"
            "[A] Add Expense\n"
            "[V] View Total Expense\n"
            "[C] Expense by Category\n"
            "[M] Monthly Report\n"
            "[Q] quit\n> "
        ).upper()
        try:
            if usr_choice == "A":
                write()
            elif usr_choice == "V":
                print(f"Your total expense is: {total_expense()}")
            elif usr_choice == "C":
                expense_by_category()
            elif usr_choice == "M":
                income = int(input("Enter your income for this month: "))
                monthly_report(income)
            elif usr_choice == "Q":
                break
        except ValueError:
            print("Invalid input")
main()







