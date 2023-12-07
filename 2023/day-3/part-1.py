digits = "0123456789"
forbidden = digits + "." 

def crawl(col, row, line, matrix, side) -> list:
    result = []
    visited_cols = []
    breaking_point = 0 if side == "left" else len(line) - 1
    start_iter = col - 1 if side == "left" else col + 1
    max_iter = -1 if side == "left" else len(line)
    iter_step = -1 if side == "left" else 1

    if col == breaking_point:
        return result
    for i in range(start_iter, max_iter, iter_step):
        visited = matrix[row][i]["visited"]
        if line[i] in digits and not visited:
            result.append(line[i])
            visited_cols.append(i)
        else:
            break
    for visited in visited_cols:
        matrix[row][visited]["visited"] = True

    if side == "left":
        result.reverse()
        return result

    return result

def crawl_up(col, row, line, matrix):
    visited = matrix[row][col]["visited"]
    if line[col] in digits and not visited:
        matrix[row][col]["visited"] = True
        return crawl(col, row, line, matrix, "left") + [line[col]] + crawl(col, row, line, matrix, "right")
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


            



    
