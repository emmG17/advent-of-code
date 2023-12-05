input = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"

def parse_input(input_string: str):
    input_split = input_string.split(":")
    gameId = input_split[0].strip().split(" ")[1]
    cubes = input_split[1].strip()
    cubes = cubes.split(";")
    shown = []
    for cube in cubes:
        cube = cube.split(",")
        shown.append(cube)
    return (parse_cube_list(shown), int(gameId))
    

def parse_cube_list(input: list) -> list:
    result = []
    for showEvent in input:
        current_cubes = {}
        for item in showEvent:
            pair = item.strip().split(" ")
            v = int(pair[0])
            k = pair[1]
            if k not in result:
                current_cubes[k] = v 
            else:
                current_cubes[k] += v 
        
        result.append(current_cubes)
    return result
        
def max_cube_count(cube_list: list) -> dict:
    result = {
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for cubes in cube_list:
        for key, value in cubes.items():
            result[key] = max(result[key], value)

    return result

def is_valid(cube_count: dict) -> bool:
    max_cubes = {
            'red': 12,
            'green': 13,
            'blue': 14
            }
    for key, value in cube_count.items():
        if value > max_cubes[key]:
            return False
    return True

def process_input(input_string: str):
    cube_list, gameId = parse_input(input_string)
    cube_count = max_cube_count(cube_list)
    if is_valid(cube_count):
        return gameId 
    return 0

run_sum = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        run_sum += process_input(line)

print(run_sum)


