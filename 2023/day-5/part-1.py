def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.read()
    return lines

def seed_to_map(text):
    block_map = [] 
    seed_list, *block_list = text.split('\n\n')
    seed_list = list(map(int, seed_list.split(': ')[1].split(' ')))

    for block in block_list:
        source_dest_ranges = []
        for line in block.splitlines()[1:]:
            source, dest, range_len = map(int, line.split())
            source_dest_ranges.append([source, dest, range_len])

        mapped_seeds = []
        for seed in seed_list:
            for s, d, r in source_dest_ranges:
                if d <= seed < d + r:
                    mapped_seeds.append(seed - d + s)
                    break;
            else:
                mapped_seeds.append(seed)
        seed_list = mapped_seeds
    return seed_list

almanac = parse_file('input.txt')
mapped = seed_to_map(almanac)
print(min(mapped))

