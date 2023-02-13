import sys
# column = {'a': [], 'b': [], 'c': []}
# column['a'].append('8')
# column['a'].append('10')
# print(column['a'][0])
# print(column['a'][column['a'].index('8')])

# if row[column].find('=') == -1:
#     print(f"{row[column]:{indent}}", end='')
# else:
#     evaluate()
#     print(f"{row[column]:{indent}}", end='')  # to do

table = {'1': {'a': 2, 'b': 3}, }
# table['2'] = {'a': 4, 'b': 5}
actions = ('+', '-', '*', '/')

cel = '=B1+Cell30'
# print('=' in cel)
cel = cel[1:]
# print(cel.split('+'))
action = ""
for action in actions:
    if action in cel:
        # print(cel)
        break
arg1, arg2 = cel.split(action)
# print(arg1, arg2)
# print(str(eval("2+3")))
# print(table.keys())
print(sys.argv)
