

import heapq

class PuzzleNode:
    def __init__(self, state, parent, move, g_cost, h_cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

    # Add comparison method for heapq to work
    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def generate_children(self, goal_state):
        children = []
        empty_index = self.state.index(0)
        x, y = empty_index // 3, empty_index % 3
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for dx, dy in moves:
            if 0 <= dx < 3 and 0 <= dy < 3:
                new_state = self.state[:]
                new_index = dx * 3 + dy
                new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
                h_cost = self.manhattan_distance(new_state, goal_state)
                children.append(PuzzleNode(new_state, self, (x, y, dx, dy), self.g_cost + 1, h_cost))
        return children

    def manhattan_distance(self, state, goal_state):
        distance = 0
        for i in range(1, 9):
            x1, y1 = divmod(state.index(i), 3)
            x2, y2 = divmod(goal_state.index(i), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
        return distance

class AStarSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def solve(self):
        if not self.is_solvable(self.start_state):
            return None
        open_list = []
        heapq.heappush(open_list, (0, PuzzleNode(self.start_state, None, None, 0, 0)))
        closed_list = set()

        while open_list:
            current_node = heapq.heappop(open_list)[1]
            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            closed_list.add(tuple(current_node.state))
            for child in current_node.generate_children(self.goal_state):
                if tuple(child.state) in closed_list:
                    continue
                heapq.heappush(open_list, (child.f_cost, child))
        return None

    def trace_solution(self, node):
        path = []
        while node.parent:
            path.append(node.move)
            node = node.parent
        return path[::-1]

    def is_solvable(self, state):
        inv_count = 0
        flat_state = [tile for tile in state if tile != 0]
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inv_count += 1
        return inv_count % 2 == 0

start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
solver = AStarSolver(start_state, goal_state)
solution = solver.solve()
print(solution)
