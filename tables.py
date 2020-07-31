#!usr/bin/python3

from prettytable import PrettyTable
import os

def cls():
    os.system('cls') if os.name == 'nt' else os.system('clear')

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

table.field_names = fields

while True:
    for value in range(count_of_fields):
        row_values.append(input('\nEnter next value: '))
    table.add_row(row_values)
    row_values = []
    
    cls()
    print(table)
    
    choice = input('\nEnter \'end\' or \'e\' for saving table and exit\n\nEnter \'next\' or \'n\' for adding next row\n\nChoice: ')

    if choice[0] == 'e':
        cls()
        print(table)
        filename = input('\nEnter name of file and extention, splitted by dot (for example, \'example.txt\', if not extention - default .txt): ')
        if len(filename.split('.')) != 1:
            table_file = open(filename, 'w')
            table_file.write(str(table) + '\n\n')
            table_file.close()
        else:
            table_file = open(filename + '.txt', 'w')
            table_file.write(str(table) + '\n\n')
            table_file.close()
        break
    elif choice[0] == 'n':
        continue
