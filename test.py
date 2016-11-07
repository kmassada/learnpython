class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "long: " + str(self.x) + "\t length: " + str(self.y)

    def distance(self):
        return abs(self.x-self.y)

x = DataPoint(7.011, 24.543)
y = DataPoint(0.2311, 24.5243)

results = {}
results['x'] = [x, y, x]
results['y'] = [y, x]

for key, arr in results.items():
    listsum = 0
    for point in arr:
        listsum += point.distance()
    print('method1')
    print(key + ": " + str(listsum/len(arr)))

    print('method2')
    print([sum([point.distance() for point in arr])/len(arr)])


print('method3')
print([sum([point.distance() for point in arr])/len(arr) for key, arr in results.items()])

