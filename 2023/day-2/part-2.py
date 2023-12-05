input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
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

def powered_cube_count(cube_count: dict) -> int:
    result = 1
    for value in cube_count.values():
        result *= value
    return result

def process_input(input_string: str) -> int:
    cube_list, _ = parse_input(input_string)
    cube_count = max_cube_count(cube_list)
    return powered_cube_count(cube_count)

run_sum = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        run_sum += process_input(line)

print(run_sum)


