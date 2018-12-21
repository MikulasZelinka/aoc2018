with open('input.txt') as f:
    freqs = [int(x) for x in f.readlines()]

    # part 1:
    print(f'1: {sum(freqs)}')

    # part 2:
    result_freq = 0
    found = {result_freq}
    finished = False
    while not finished:
        for x in freqs:
            result_freq += x
            if result_freq in found:
                print(f'2: {result_freq}')
                finished = True
                break
            found.add(result_freq)
