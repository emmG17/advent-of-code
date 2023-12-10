def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.read()
    return lines

def expand_seeds(seed_list) -> list[tuple[int, int]]:
    # split the seed list into arrays of two elements
    seeds = []
    for i in range(0, len(seed_list), 2):
        seeds.append((seed_list[i], seed_list[i] + seed_list[i+1]))
    return seeds

def seed_to_map(text):
    seed_list, *block_list = text.split('\n\n')
    seed_list = list(map(int, seed_list.split(': ')[1].split(' ')))
    seed_list = expand_seeds(seed_list)

    for block in block_list:
        source_dest_ranges = []
        for line in block.splitlines()[1:]:
            source, dest, range_len = map(int, line.split())
            source_dest_ranges.append([source, dest, range_len])

        mapped_seeds = []
        while len(seed_list) > 0:
            start, end = seed_list.pop()
            for a, b, c in source_dest_ranges:
                overlap_start = max(start, b)
                overlap_end = min(end, b + c)
                if overlap_start < overlap_end:
                    mapped_seeds.append((overlap_start - b + a, overlap_end  - b + a))
                    if overlap_start > start:
                        seed_list.append((start, overlap_start))
                    if end > overlap_end:
                        seed_list.append((overlap_end, end))
                    break;
            else:
                mapped_seeds.append((start, end))
        seed_list = mapped_seeds
    return seed_list

almanac = parse_file('input.txt')
mapped = seed_to_map(almanac)
print(sorted(mapped)[0][0])

