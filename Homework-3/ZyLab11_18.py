# Name-Rhozalin Nath
# PS ID: 2050395

string = input()
int_list = string.split()
l=[]
for i in int_list:
    if int(i)>=0:
        l.append(int(i))

l.sort()
for i in l:
    print(i,end=" ")
