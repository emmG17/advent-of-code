spelled_nums = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

def find_first_spelled_num(line):
  first = [len(line), "0"]
  for k, v in spelled_nums.items():
    found_idx = line.find(k)
    if found_idx != -1 and first[0] >= found_idx:
      first[0] = found_idx
      first[1] = v
  return first

def find_last_spelled_num(line):
  first = [len(line), "0"]
  reversed_line = "".join(reversed(line))
  for k, v in spelled_nums.items():
    reversed_key = "".join(reversed(k))
    found_idx = reversed_line.find(reversed_key)
    if found_idx != -1 and first[0] >= found_idx:
      first[0] = found_idx
      first[1] = v
  first[0] = (len(line) - 1) - first[0]
  return first

def first_num(text):
  for i in range(len(text)):
      if text[i] in spelled_nums.values():
          return [i, text[i]]
  return [-1, "0"]

# Find second number
def last_num(text):
  # Reverse search
  for i in range(len(text) - 1, -1, -1):
      if text[i] in spelled_nums.values():
          return [i, text[i]]
  return [-1, "0"]

def find_num(line):
  nums = [find_first_spelled_num(line), \
   find_last_spelled_num(line), \
   first_num(line), \
   last_num(line) ]
  nums.sort(key=lambda x: x[0])
  valid_nums = [i for i in filter(lambda x: x[1] != "0", nums)]
  return int(valid_nums[0][1] + valid_nums[-1][1])

running_sum = 0
with open("./input.txt", "r") as f:
  for line in f.readlines():
    num = find_num(line)
    running_sum += num

print(running_sum)

