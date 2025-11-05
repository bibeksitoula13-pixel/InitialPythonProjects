def Task():
    global Tasks
    Tasks = []
    with open("/home/bibeksitoula/PycharmProjects/roadtomastery/InitialPythonProjects/to do list", "r") as To_do_file:
        for line in To_do_file:
            Tasks.append(line)
def display():
    global Tasks
    num = 1
    for task in Tasks:
        print(str(num) + ": " + task)
        num = num + 1
    usr_option_function()
def add():
    global Tasks
    while True:
        task = input("Enter a task: ")
        with open("/home/bibeksitoula/PycharmProjects/roadtomastery/InitialPythonProjects/to do list","a") as To_do_file:
            Tasks.append(task)
            To_do_file.write(task+"\n")
            usr_option = input("Would you like to add another task?[y/n]")
            if usr_option.lower() == "n":
                break
    usr_option_function()
def delete():
    global Tasks
    while True:
        with open("/home/bibeksitoula/PycharmProjects/roadtomastery/InitialPythonProjects/to do list","w") as To_do_file:
            num = 1
            for task in Tasks:
                print(str(num) + ": " + task)
                num = num + 1
            usr_option = int(input("which number task would you like to delete? "))
            delval = Tasks[usr_option-1]
            Tasks.remove(delval)
            for task in Tasks:
                To_do_file.write(task+"\n")
            usr_option2 = input("Would you like to delete another task?[y/n]")
            if usr_option2.lower() == "n":
                break
    usr_option_function()

def usr_option_function():
    usr_option = input("would you like to add/delete/view task/do nothing? ")
    if usr_option.lower() == "add":
        add()
    elif usr_option.lower() == "delete":
        delete()
    elif usr_option.lower() == "view":
        display()
    else:
        print("Thank you!")
Task()
usr_option_function()






