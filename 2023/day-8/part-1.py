def parse_map(filename: str):
    with open(filename, "r") as f:
        instruction, node_list = f.read().strip().split("\n\n")
        node_list = node_list.split("\n")
        node_list = [node.split(" = ") for node in node_list]
        network = {}
        for node_key, node_to in node_list:
            l, r = node_to.replace(")", "").replace("(", "").split(", ")
            network[node_key] = { "L": l, "R": r }

        return instruction, network




def travel_direction(step: int, instruction: str) -> str:
    idx = step % len(instruction)
    return instruction[idx]

instruction, network = parse_map("input.txt")

step_count = 0
node = "AAA" 
while (True):
    if node == "ZZZ":
        print(step_count)
        break;

    direction = travel_direction(step_count, instruction)
    node = network[node][direction]
    step_count += 1
