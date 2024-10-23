



GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
def goal(state):
    return state == GOAL

def blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def move(state):
    neighbors = []
    i, j = blank(state)
    moves = {
        'Up': (i - 1, j),
        'Down': (i + 1, j),
        'Left': (i, j - 1),
        'Right': (i, j + 1)
    }

    for direction, (new_i, new_j) in moves.items():
        if 0 <= new_i < 3 and 0 <= new_j < 3:  
            
            new_state = list(map(list, state))  
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append((tuple(map(tuple, new_state)), direction))  
    return neighbors

def iddfs(start_s):
    def dls(state, depth, path, visited, moves_l):
        if goal(state):
            return path, moves_l
        if depth == 0:
            return None, None
        visited.add(state)
        for neighbor, move_direction in move(state):
            if neighbor not in visited:
                result, moves_result = dls(neighbor, depth - 1, path + [neighbor], visited, moves_l + [move_direction])
                if result is not None:
                    return result, moves_result
        visited.remove(state)
        return None, None

    depth = 0
    while True:
        visited = set()
        result, moves_result = dls(start_state, depth, [start_s], visited, [])
        if result is not None:
            return result, moves_result, depth
        depth += 1


def print_moves(sol, moves):
    print("moves:", len(moves))
    print(" total Moves:", moves)
    for i, state in enumerate(sol):
        print(f"Step {i}:")
        for row in state:
            print(row)
        print()


start_state = ((1, 2, 3), (4,6,0), (7, 5, 8))


solution_path, moves, max_depth = iddfs(start_state)
print_moves(solution_path, moves)
