from datetime import datetime
import csv
from time import strptime

TempDict = []
def read():
    global TempDict
    try:
        with open("ExpenseTracker.csv","r") as exp_tra_file:
            csv_reader = csv.DictReader(exp_tra_file)
            for line in csv_reader:
                TempDict.append(line)
                print (line)
    except FileNotFoundError:
        with open("ExpenseTracker.csv","a") as exp_tra_file:
            fieldnames = ["Expense","Date","Category","Amount","Description"]
            csv_writer = csv.DictWriter(exp_tra_file, fieldnames=fieldnames)
            csv_writer.writeheader()

def write():
    global TempDict
    try:
        with open("ExpenseTracker.csv","a") as exp_tra_file:
            csv_writer = csv.DictWriter(exp_tra_file,fieldnames=["Expense","Date","Expenses","Category","Amount","Description"])
            while True:
                expense = input("Enter the expense: ")
                date = input("Enter date of expense(yyyy-mm-dd): ")
                try:
                    date_obj = datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date")
                category = input("Enter category of expense: ")
                amount = input("Enter amount of expense: ")
                description = input("Enter description of expense: ")
                TempDict.append({"Expense":expense,"Date":date_obj.date(),"Category":category,"Amount":amount,"Description":description})
                csv_writer.writerow(TempDict[len(TempDict)-1])
                usr_option = input("would you like to add more?[y/n]")
                if usr_option == "n":
                    break
    except FileNotFoundError:
        print("file not found")

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
    avg_cloths_expense = (clothes_expense / total_expense()) *100
    avg_others_expense = (others_expense / total_expense()) *100
    print(f"Total food expense is: {food_expense}, and it is {avg_food_expense}% of total\n Total "
          f"rent expense is: {rent_expense}, and it is {avg_rent_expense}% of total\n Total "
          f"entertainment expense is: {entertainment_expense}, and it is {avg_entertainment_expense}% of total\n Total"
          f" clothes expesne is: {clothes_expense}, and it is {avg_cloths_expense}% of total\n Total"
          f" other expense is: {others_expense}, and it is {avg_others_expense}% of total.")

def monthly_report():
    global TempDict
    Current_Month = datetime.now().month
    total = 0
    totalpre = 0
    highest = 0
    highestpre = 0
    lowest = 0
    lowestpre = 0
    amt_list = []
    list_month = []
    for items in TempDict:
        list_month.append(items["Date"])
        amt_list.append(int(items["Amount"]))
    for i in range(0,len(list_month)):
        list_month[i] = datetime.strptime(list_month[i], "%Y-%m-%d")
        if list_month[i].month == Current_Month:
            total = total+amt_list[i]
            if amt_list[i] > highest:
                highest = amt_list[i]
            if amt_list[i]<lowest:
                lowest = amt_list[i]

        elif list_month[i].month== Current_Month-1:
            totalpre = totalpre+amt_list[i]
            if amt_list[i] > highestpre:
                highestpre = amt_list[i]
            if amt_list[i]<lowestpre:
                lowestpre = amt_list[i]
    print(f"your total spending this months is {total}")
    print(f"your total spending previous month was {totalpre}")
    print(f"your total highest expense was on {highest}")
    print(f"your total lowest expense was on {lowest}")


read()
print(total_expense())
expense_by_category()
monthly_report()





