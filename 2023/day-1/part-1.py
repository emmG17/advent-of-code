numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
text = "treb7uchet"
running_sum = 0

# Find first number
def first_num(text):
    for c in text:
        if c in numbers:
            return c
    return "0"

# Find second number
def last_num(text):
    # Reverse search
    for i in range(len(text) - 1, -1, -1):
        if text[i] in numbers:
            return text[i]
    return "0"

# Concat & convert numbers
def two_digits_from_line(line):
    two_digits = first_num(line) + last_num(line)
    return int(two_digits)

# Read lines
with open("./input.txt", "r") as f:
    for line in f.readlines():
        running_sum += two_digits_from_line(line)


# Out result
print(running_sum)
