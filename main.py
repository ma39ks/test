import csv
import sys

indent = 11
actions = ('+', '-', '*', '/')


def meaning(cell: str) -> int:
    row = ''
    column = ''

    for x in table.keys():
        for y in table[x].keys():
            if y != '':
                if y in cell:
                    row = cell.split(y)[1]
                    column = y
                    break
        break
    for x in table.keys():
        if table[x][''] == row:
            return table[x][column]

    return -1


def evaluate(cell: str) -> str:
    action = ''

    for i in actions:
        if i in cell:
            arg1, arg2 = cell.split(i)
            action = i
            break
    evArg1 = meaning(arg1)
    evArg2 = meaning(arg2)

    if evArg2 == -1 or evArg1 == -1:
        return "ERROR"
    if '=' in evArg2:
        evArg2 = evaluate(evArg2)
    if '=' in evArg1:
        evArg1 = evaluate(evArg1)
    try:
        return str(eval(evArg1 + action + evArg2))
    except ZeroDivisionError:
        return "ERROR"


table = {}
file = sys.argv[-1]
if file.split('.')[-1] != 'csv':
    print("Invalid file extension or non-existent file")
    exit(1)
with open('test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    columns = reader.fieldnames
    print(f"{'':{indent}}".join(columns))
    for row in reader:
        table[reader.line_num] = {}
        for column in columns:
            table[reader.line_num][column] = row[column]
            # print(f"{row[column]:{indent}}", end='')
        # print()

for i in table.keys():
    for j in table[i].keys():
        if '=' in table[i][j]:
            print(f"{evaluate(table[i][j][1:]):{indent}}", end='')
        else:
            print(f"{table[i][j]:{indent}}", end='')
    print()
