import datetime
import csv

TempDict = {}
def read():
    global TempDict
    try:
        with open("ExpenseTracker.csv","r") as exp_tra_file:
            csv_reader = csv.DictReader(exp_tra_file)
            for line in csv_reader:
                TempDict={"Date":line["Date"],"Category":line["Category"],
                         "Amount":line["Amount"],"Description":line["Description"]}

                print (line)
    except FileNotFoundError:
        with open("ExpenseTracker.csv","w") as exp_tra_file:
            fieldnames = ["Date","Category","Amount","Description"]
            csv_writer = csv.DictWriter(exp_tra_file, fieldnames=fieldnames)
            csv_writer.writeheader()

def write():
    global TempDict
    try:
        with open("ExpenseTracker.csv","a") as exp_tra_file:
            csv_writer = csv.DictWriter(exp_tra_file,fieldnames=["Date","Category","Amount","Description"])
            while True:
                date = input("Enter date and time of expense: ")
                category = input("Enter category of expense: ")
                amount = input("Enter amount of expense: ")
                description = input("Enter description of expense: ")
                TempDict.update({"Date":date,"Category":category,"Amount":amount,"Description":description})
                csv_writer.writerow(TempDict)
                usr_option = input("would you like to add more?[y/n]")
                if usr_option == "n":
                    break
    except FileNotFoundError:
        print("file not found")

read()
write()







