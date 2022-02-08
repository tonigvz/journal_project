# importing datetime to name a new file with the current date,importing inquirer for choosing an option from list,importing os to show the files in folder
from datetime import date
import inquirer
import os

# inquirer list with the actions that the user can perform
actions = [
    inquirer.List(
        "action",
        message="What would you like to do today?",
        choices=["Write new page", "Add to existing page", "Read page", "Delete page"],
    ),
]
# launching prompt interface
answer = inquirer.prompt(actions)
for key, value in answer.items():
    choice = value


# creating filename as datetime
today = date.today()
filename = f"{today}.txt"


# function that lists the txt files in the folder and the user can choose what to work on from the list of files
def choose_file():
    pages = [n for n in os.listdir("D:\Journal") if n.endswith(".txt")]
    for number, filename in enumerate(pages):
        print(f"{number} {filename}")
    return "".join(pages[int(input(f"select file:"))])


# function to write new page
def write():
    with open(filename, "w") as f:
        print("Add your text:")
        while True:
            try:
                f.writelines(input() + "\n")
            except EOFError:
                break


# function to append to a page
def append():
    name = choose_file()
    print(f"working on file {name}")
    with open(name, "a") as f:
        print("Add your text:")
        while True:
            try:
                f.writelines(input() + "\n")
            except EOFError:
                break


# function to read a page
def read():
    name = choose_file()
    print(f"working on file {name}")
    with open(name, "r") as f:
        content = f.read()

    print(content)


# function to delete a page
def delete():
    name = choose_file()
    print(f"working on file {name}")
    if input("Are you sure? ") == "yes":
        os.remove(name)
        print("The page was deleted")
    else:
        print("Delete cancelled")


# function to perform based on user choice
def perform(choice):
    act = {
        "Write new page": write,
        "Add to existing page": append,
        "Read page": read,
        "Delete page": delete,
    }
    act[choice]()


perform(choice)
