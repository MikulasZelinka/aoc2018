import re
import numpy as np

with open('input.txt') as f:
    records = [x.strip() for x in f.readlines()]
records.sort()
guard_count = len([r for r in records if r.endswith('t')])
sleep_counts = np.zeros((guard_count, 60), dtype=np.uint8)

asleep = False
guard_seen_count = 0
guard_id_to_order = {}
last_guard_order = 0
last_minute = 0
for r in records:
    minute = int(r[15:17])
    if r.endswith('t'):  # begins shift
        if asleep:
            sleep_counts[last_guard_order, last_minute:60] += 1
        gid = int(re.match('.*#([0-9]+).*', r).group(1))
        if gid not in guard_id_to_order:
            guard_id_to_order[gid] = guard_seen_count
            guard_seen_count += 1
        last_guard_order = guard_id_to_order[gid]
        hour = int(r[12:14])
        if hour:
            minute = 0
        asleep = False
    elif r.endswith('ep'):  # falls asleep
        asleep = True
    else:  # wakes up
        sleep_counts[last_guard_order, last_minute:minute] += 1
        asleep = False
    last_minute = minute
if asleep:
    sleep_counts[last_guard_order, last_minute:60] += 1
guard_order_to_id = {v: k for k, v in guard_id_to_order.items()}

# part 1:
sleepiest_guard_order = np.argmax(np.sum(sleep_counts, axis=1))
print(f'1: {guard_order_to_id[sleepiest_guard_order] * np.argmax(sleep_counts[sleepiest_guard_order])}')

# part 2:
sleepiest_guard_order, sleepiest_minute = np.unravel_index(sleep_counts.argmax(), sleep_counts.shape)
print(f'2: {guard_order_to_id[sleepiest_guard_order] * sleepiest_minute}')
