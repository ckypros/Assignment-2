from math import sqrt

data = [
    [220, 20, 60, 1],
    [255, 99, 21, 1],
    [250, 128, 14, 1],
    [144, 238, 144, 2],
    [107, 142, 35, 2],
    [46, 139, 87, 2],
    [64, 224, 208, 3],
    [176, 224, 23, 3],
    [100, 149, 237, 3]
]

distances = []
x1 = 154
y1 = 205
z1 = 50

for i, instance in enumerate(data):
    x2, y2, z2 = [instance[i] for i in range(3)]
    print(f"distance_{i+1} = sqrt( ({x1} - {x2})^2 + ({y1} - {y2})^2 + ({z1} - {z2})^2 )")
    print(f"distance_{i+1} = sqrt( ({x1-x2})^2 + ({y1-y2})^2 + ({z1-z2})^2 )")
    print(f"distance_{i+1} = sqrt( {pow(x1-x2,2)} + {pow(y1-y2,2)} + {pow(z1-z2,2)} )")
    distance = sqrt(pow(x1-x2,2) + pow(y1-y2,2) + pow(z1-z2,2) )
    print(f"distance_{i+1} = {distance}")
    print()

    distances.append([i, distance])
    sorted_distances = sorted(distances, key=lambda x: (x[1], -x[1]))

for i in range(3):
    instance = sorted_distances[i]
    print(f"instance# {instance[0] + 1} = {data[instance[0]][3]}") 