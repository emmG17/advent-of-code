def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.read()
    return lines

def seed_to_map(text):
    maps_dict = {}
    block_list = text.split('\n\n')
    for i in range(len(block_list)):
        if i == 0:
            seed_list = block_list[i].split(': ')
            title = seed_list[0].strip()
            contents = [int(seed.strip()) for seed in seed_list[1].strip().split(' ')]
            maps_dict[title] = contents
        else:
            title = block_list[i].replace(':', '').split(' ')[0].strip()
            map_values = block_list[i].strip().split('\n')[1:]
            contents = []
            for line in map_values:
                contents.append([ int(i) for i in line.split(' ')])
            maps_dict[title] = contents

    return maps_dict

    

text = parse_file('test.txt')
print(seed_to_map(text))

