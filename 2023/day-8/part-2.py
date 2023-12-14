from math import gcd

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

def node_ends_with_z(node: str) -> bool:
    return node[-1] == "Z"

instruction, network = parse_map("input.txt")

starting_nodes = [node for node in network.keys() if node[-1] == "A"]
arrived_at = []
for node in starting_nodes:
    step_count = 0
    current = node
    while (True):
        if current[-1] == "Z":
            break;

        direction = travel_direction(step_count, instruction)
        current = network[current][direction]
        step_count += 1
    arrived_at.append(step_count)

total_steps = arrived_at.pop()

for count in arrived_at:
    total_steps = total_steps * count // gcd(total_steps, count)

print(total_steps)


    

