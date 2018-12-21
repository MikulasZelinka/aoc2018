import re
import numpy as np

with open('input.txt') as f:
    claims = [[int(x) for x in
               re.match('^#(?P<id>[0-9]+) @ (?P<x>[0-9]+),(?P<y>[0-9]+): (?P<w>[0-9]+)x(?P<h>[0-9]+)$', l).groups()]
              for l in f.readlines()]

# part 1:
counts = np.zeros((1000, 1000), dtype=np.uint16)
for _, x, y, w, h in claims:
    counts[x:x + w, y:y + h] += 1
print(f'1: {np.sum(counts >= 2)}')

# part 2:
for id, x, y, w, h in claims:
    if np.all(counts[x:x + w, y:y + h] == 1):
        print(f'2: {id}')
        break
