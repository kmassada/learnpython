newdict = {
    'a': 1,
    'b': 5,
    'c': 8
 }

keys = newdict.keys()
items = newdict.items()

print(keys)
print(items)

if ('d' in newdict):
    print('d is here')
elif('a' in newdict):
    print('a is here')
else:
    print('neither')
