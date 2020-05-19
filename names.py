import sys

items = []

def first_char(menu_item):
    return menu_item[0:1].lower()

def add_item():
    while True:
        item = input('Enter the name (hit Enter to menu): ')
        if item == '':
            break
        else:
            items.append(item)
            print(f'{item} was added')

def show_menu():
    choice = input('Your choice [a]dd [r]emove [p]rint [e]xit: ')
    if first_char(choice) == 'e':
        sys.exit()
    elif first_char(choice) == 'a':
        add_item()
        show_menu()
    elif first_char(choice) == 'p':
        print_items()
        show_menu()
    else:
        show_menu()

def print_items():
    if len(items) > 0:
        for item in items:
            print(item)
    else:
        print('No names, please add')

show_menu()