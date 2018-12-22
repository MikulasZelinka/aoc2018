import re
import string

with open('input.txt') as f:
    polymer = f.readline().strip()


def collapse(polymer):
    while True:
        new = []
        skip_next = False
        for i, c in enumerate(polymer[:-1]):
            if skip_next:
                skip_next = False
                continue
            if c != polymer[i + 1] and c.upper() == polymer[i + 1].upper():
                skip_next = True
                continue
            new.append(c)
        if not skip_next:
            new.append(polymer[-1])
        new = ''.join(new)
        if polymer == new:
            return polymer
        polymer = new


# part 1:
l = len(collapse(polymer))
print(f'1: {l}')

# part 2:
min_len = l
for c in string.ascii_lowercase:
    min_len = min(len(collapse(re.subn(f'[{c}{c.upper()}]', '', polymer)[0])), min_len)
print(f'2: {min_len}')
