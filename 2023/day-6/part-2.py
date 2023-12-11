import math

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def data_table(filename):
    time, distance = parse_file(filename) 
    time = int(time.split(':')[1].replace(' ', ''))
    distance = int(distance.split(':')[1].replace(' ', ''))
    return time, distance

def chicharronera(a, b, c) -> tuple[float, float]:
    # This is the general formula for a quadratic equation, it is adjusted to pick discrete values
    big_sqrt = math.sqrt(b**2 - 4*a*c)
    first = math.ceil((-b + big_sqrt)/(2*a))
    second = math.floor((-b - big_sqrt)/(2*a))
    return first, second

# 'tis but a parable
def parable_intersect(time, distance):
    # the parable formula is -x^2 + tx where t is the max time and x is the time ellapsed
    a = -1
    b = time
    c = -(distance + 1)
    first, last = sorted(chicharronera(a, b, c))
    return (last - first) + 1

t, d= data_table('input.txt')
multiplication = parable_intersect(t, d)
print(multiplication)
