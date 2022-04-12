from datetime import date
import inquirer
import os
from os.path import exists
import sys

actions = [
    inquirer.List(
        "action",
        message="What would you like to do today?",
        choices=["write new page", "append", "read", "delete"],
    ),
]
answer = inquirer.prompt(actions)
for key, value in answer.items():
    choice_user = value


class journal:
    def pick_name(self):
        pick = input("use date as name or type name?")
        if (pick == "date") or (pick == "1"):
            today = date.today()
            pagename = f"{today}.txt"
        elif (pick == "type") or (pick == "2"):
            pagename = f"{input(f'type name:')}.txt"
        name_exists = exists(f"B:\journal_project\{pagename}")
        return pagename if not (name_exists) else self.pick_name()

    def choose_file(self):
        pages = [n for n in os.listdir("B:\journal_project") if n.endswith(".txt")]
        for number, name in enumerate(pages):
            print(f"{number} {name}")
        return "".join(pages[int(input(f"select file:"))])

    def write(self):
        name = self.pick_name()
        with open(f"B:\journal_project\{name}", "w") as f:
            print("add your text:")
            while True:
                try:
                    txt = input()
                    if txt:
                        f.writelines(txt + "\n")
                    else:
                        sys.tracebacklimit = 0
                        raise KeyboardInterrupt("no input")
                except EOFError:
                    print("finish")

    def append(self):
        name = self.choose_file()
        print(f"working on file {name}")
        with open(f"B:\journal_project\{name}", "a") as f:
            print("add your text:")
            while True:
                try:
                    txt = input()
                    if txt:
                        f.writelines(txt + "\n")
                    else:
                        sys.tracebacklimit = 0
                        raise KeyboardInterrupt("no input")
                except EOFError:
                    print("finish")

    def read(self):
        name = self.choose_file()
        print(f"working on file {name}")
        with open(f"B:\journal_project\{name}", "r") as f:
            content = f.read()
        print(content)

    def delete(self):
        name = self.choose_file()
        print(f"working on file {name}")
        if input("are you sure? ") == "yes":
            os.remove(f"B:\journal_project\{name}")
            print("the page was deleted.")
        else:
            print("delete cancelled!")

    @property
    def dispatcher(self):
        return {
            "write new page": self.write,
            "append": self.append,
            "read": self.read,
            "delete": self.delete,
        }


journal1 = journal()
journal1.dispatcher[choice_user]()
