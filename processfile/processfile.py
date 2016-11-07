import os
thisfile = open("data")
print(thisfile.readlines())

with open("data") as f:
    lines = f.readlines()
f.closed
print(lines)

thisfile = open("data")
for eachline in thisfile:
    print(eachline.split())

file = open('myfile.dat', 'w+')

os.remove("myfile.dat")
