'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import sys

if __name__ == '__main__':
    N = int(input())

my_list = []
inputs  = []

for line in sys.stdin:
    inputs.append(line)

for item in inputs:
    if item[0:5] == 'print':
        print(my_list)
    elif item[0:2] == 'in':
        inserts = [s for s in item.split()][1:3]
        inserts = list(map(int, inserts))
        my_list.insert(inserts[0], inserts[1])
    elif item[0:3] == 'rem':
        inserts = list(map(int, [s for s in item.split()][1]))
        my_list.remove(inserts[0])
    elif item[0:2] == 'ap':
        inserts = list(map(int, [s for s in item.split()][1]))
        my_list.append(inserts[0])
    elif item[0:4] == 'sort':
        my_list.sort()
    elif item[0:3] == 'pop':
        my_list.pop()
    elif item[0:7] == 'reverse':
        my_list.reverse()
