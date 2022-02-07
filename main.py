from datetime import date
import inquirer
import os
today = date.today()
filename = f"{today}.txt"

actions = [
    inquirer.List('action',
                  message='What would you like to do today?',
                  choices=['Write new page', 'Add to existing page',
                           'Read page', 'Delete page']
                  ),
]

answer = inquirer.prompt(actions)


for key, value in answer.items():
    if value == 'Write new page':
        with open(filename, 'w') as f:
            print('Add your text:')
            while True:
                try:
                    f.writelines(input() + '\n')
                except EOFError:
                    break
    elif value == 'Add to existing page':
        name = input('Choose file:')
        with open(name, 'a') as f:
            print('Add your text:')
            while True:
                try:
                    f.writelines(input() + '\n')
                except EOFError:
                    break
    elif value == 'Read page':
        name = input('Choose file:')
        with open(name, 'r') as f:
            content = f.read()

        print(content)
    elif value == 'Delete page':
        name = input('Choose file:')
        if input('Are you sure? ') == 'yes':
            os.remove(name)
        else:
            print('Delete cancelled')
