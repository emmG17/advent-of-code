test_lines = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split('\n')

digits = "0123456789"
forbidden = digits + "." 

def crawl_left(col, row, line, matrix):
    left = []
    if col == 0:
        return left
    visited_cols = []
    for i in range(col - 1, -1, -1):
        visited = matrix[row][i]["visited"]
        if line[i] in digits and not visited:
            left.append(line[i])
            visited_cols.append(i)
        else:
            break

    for vistited in visited_cols:
        matrix[row][vistited]["visited"] = True
    left.reverse()
    return left

def crawl_right(col, row, line, matrix):
    right = []
    if col == len(line) - 1:
        return right
    visited_cols = []
    for i in range(col + 1, len(line)):
        visited = matrix[row][i]["visited"]
        if line[i] in digits and not visited:
            right.append(line[i])
            visited_cols.append(i)
        else:
            break
    for vistited in visited_cols:
        matrix[row][vistited]["visited"] = True
    return right

def crawl_up(col, row, line, matrix):
    visited = matrix[row][col]["visited"]
    if line[col] in digits and not visited:
        matrix[row][col]["visited"] = True
        return crawl_left(col, row, line, matrix) + [line[col]] + crawl_right(col, row, line, matrix)
    return

def find_neighbors(node, lines):
    i, j = node
    rows = len(lines)
    cols = len(lines[i])
    neighbors = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            i_new = i + di
            j_new = j + dj
            if i_new < 0 or i_new >= rows or j_new < 0 or j_new >= cols:
                continue
            neighbors.append( { "node": (i_new, j_new) } )
    return neighbors

def adjacency_matrix(lines):
    matrix = []
    for i in range(len(lines)):
        row = []
        for j in range(len(lines[i])):
            row.append( { "neighbors": find_neighbors( (i, j), lines), "visited": False } ) 
        matrix.append(row)
    return matrix

def find_symbols(lines, matrix):
    symbol_nodes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if lines[i][j] not in forbidden:
                symbol_nodes.append(matrix[i][j])
    return symbol_nodes


seen_numbers = [] 
with open("input.txt", "r") as f:
    raw_lines = f.readlines()
    test_lines = [line.strip() for line in raw_lines]
    matrix = adjacency_matrix(test_lines)
    symbol_nodes = find_symbols(test_lines, matrix)
    for node in symbol_nodes:
        for neighbor in node["neighbors"]:
            i, j = neighbor["node"]
            if not matrix[i][j]["visited"]:
                crawled_num = crawl_up(j, i, test_lines[i], matrix)
                res_num = -1
                if crawled_num:
                    res_num = int("".join(crawled_num))
                if res_num > 0:
                    seen_numbers.append(res_num)

print(sum(seen_numbers))
print(seen_numbers)


            



    
