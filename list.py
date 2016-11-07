a = [0, 1, 4, 8, 17]

print(a)

print('append 12')
a.append(12)
print(a)

print('pop')
a.pop()
print(a)


squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

print('lamda')
nusquares = list(map(lambda x: x**2, range(10)))
print(nusquares)

print('list-comp')
compsquares = [x**2 for x in range(20)]
print(compsquares)

print('double array')
doub = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(doub)