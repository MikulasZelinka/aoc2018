import numpy as np
from scipy.spatial.distance import cityblock

with open('input.txt') as f:
    coords = np.array([l.split(',') for l in f.readlines()], dtype=np.uint16)
coords[:, 0] -= np.min(coords[:, 0])
coords[:, 1] -= np.min(coords[:, 1])
x_max, y_max = np.max(coords[:, 0]), np.max(coords[:, 1])

num_closest = np.zeros((len(coords)))
distance_sums = np.zeros((x_max + 1, y_max + 1))
infinite = set()
for y in range(y_max + 1):
    for x in range(x_max + 1):
        distances = sorted({i: cityblock((x, y), (_x, _y)) for i, (_x, _y) in enumerate(coords)}.items(),
                           key=lambda z: z[1])
        distance_sums[x, y] = sum([x[1] for x in distances])
        if x == 0 or x == x_max or y == 0 or y == y_max:
            closest_distance = distances[0][1]
            for cid, d in distances:
                if d > closest_distance:
                    break
                infinite.add(cid)
        elif distances[0][1] < distances[1][1]:
            num_closest[distances[0][0]] += 1
num_closest = [x if (i not in infinite) else 0 for i, x in enumerate(num_closest)]
print(f'1: {max(num_closest)}')
print(f'2: {np.sum(distance_sums < 10000)}')
