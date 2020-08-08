#!usr/bin/python3

try:
    from prettytable import PrettyTable
except ImportError:
    print('Install requirement modules via \'$ pip3 install -r requirements.txt\''); exit()

import os
import random

def cls():
    os.system('cls') if os.name == 'nt' else os.system('clear')

def saving_table():
    pass

def loading_table():
    pass

table = PrettyTable()

fields = []
row_values = []

while True:
    cls()
    try:
        count_of_fields = int(input('Enter count of fields: '))
    except:
        print('Enter a number, biatch!')
    else:
        break

for field in range(count_of_fields):
    fields.append(input('\nEnter field title: '))

try:
    table.field_names = fields
except:
    print('\nAll column titles must be unique!\n'); exit()

while True:
    for value in fields:
        row_values.append(input(f'\nEnter value for {value}: '))
    table.add_row(row_values)
    row_values = []
    
    cls()
    print(table)
    
    choice = input('\nEnter \'end\' or \'e\' for saving table and exit\n\nEnter \'next\' or \'n\' for adding next row\n\nChoice: ')
    if choice == '':
        print('\nNo, you must enter something!\n')
        break
    if choice[0].lower() == 'e':
        cls()
        print(table)
        table_html = table.get_html_string()
        table_title=input('\nEnter table title: ')
        filename = input('\nEnter name of file and extention, splitted by dot (for example, \'example.txt\', if not extention - default .txt): ')
        file_name, file_ext = filename.split('.')[0], filename.split('.')[-1]
        if os.path.exists(filename) == True:
            if input('This file already exists. Type \'rewrite\' for re-write the file or something for magic: ').lower() != 'rewrite':
                filename = f'{file_name}_{random.randint(0, 9)}.{file_ext}'
        if len(filename.split('.')) != 1:
            table_file = open(filename, 'w')
            table_file.write(table.get_string(title=table_title) + '\n\n')
            table_file.close()
            table_html_file = open(filename.split('.')[0] + '.html', 'w')
            table_html_file.write(str(table_html) + '\n\n')
            table_html_file.close()
        else:
            table_file = open(filename + '.txt', 'w')
            table_file.write(table.get_string(title=table_title) + '\n\n')
            table_file.close()
            table_html_file = open(filename + '.html', 'w')
            table_html_file.write(str(table_html) + '\n\n')
            table_html_file.close()
        break
    elif choice[0].lower() == 'n':
        continue
    else:
        print('\nHey you, cocksucker! Read my ass instruction before penetrating!\n')
        break
