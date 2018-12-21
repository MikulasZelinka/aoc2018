from collections import Counter

with open('input.txt') as f:
    items = [x.strip() for x in f.readlines()]

# part 1:
l2 = l3 = 0
for x in items:
    counts = set(Counter(x).values())
    l2 += 2 in counts
    l3 += 3 in counts
print(f'1: {l2 * l3}')

# part 2:
finished = False
for x in items:
    if finished:
        break
    for y in items:
        found_diff = False
        correct = True
        for i, (_x, _y) in enumerate(zip(x, y)):
            diff = _x != _y
            if found_diff and diff:
                correct = False
                break
            if diff:
                found_diff = True
                diff_idx = i
        if correct and found_diff:
            print(f'2: {x[:diff_idx]}{x[diff_idx + 1:]}')
            finished = True
            break
