import time
from collections import deque
import heapq

def is_safe(state, col):
    row = len(state)
    for r, c in enumerate(state):
        
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def get_successors(state):
    return [state + (c,) for c in range(8) if is_safe(state, c)]

def run_bfs():
    start_time = time.time()
    queue = deque([((), 0)])
    expanded = 0

    while queue:
        state, cost = queue.popleft()
        expanded += 1

        if len(state) == 8:
            return state, expanded, time.time() - start_time
        
        for succ in get_successors(state):
            queue.append((succ, cost + 1))
    return None, expanded, time.time() - start_time

def run_dfs():
    start_time = time.time()
    stack = [((), 0)]
    expanded = 0

    while stack:
        state, cost = stack.pop()
        expanded += 1

        if len(state) == 8:
            return state, expanded, time.time() - start_time

        for succ in get_successors(state):
            stack.append((succ, cost + 1))
    return None, expanded, time.time() - start_time

def run_ucs():
    start_time = time.time()
    pq = [(0, ())]
    expanded = 0

    while pq:
        cost, state = heapq.heappop(pq)
        expanded += 1
        if len(state) == 8:
            return state, expanded, time.time() - start_time

        for succ in get_successors(state):
            heapq.heappush(pq, (cost + 1, succ))
    return None, expanded, time.time() - start_time

def run_dls(limit):
    start_time = time.time()
    stack = [((), 0)]
    expanded = 0
    while stack:
        state, depth = stack.pop()
        expanded += 1
        if len(state) == 8:
            return state, expanded, time.time() - start_time
        if depth < limit:
            for succ in get_successors(state):
                stack.append((succ, depth + 1))
    return None, expanded, time.time() - start_time

def run_iddfs():
    start_time = time.time()
    total_expanded = 0
    for depth in range(9):
        stack = [((), 0)]
        while stack:
            state, d = stack.pop()
            total_expanded += 1

            if len(state) == 8:
                return state, total_expanded, time.time() - start_time

            if d < depth:
                for succ in get_successors(state):
                    stack.append((succ, d + 1))

    return None, total_expanded, time.time() - start_time

def compare():
    results = []
    results.append(("BFS", *run_bfs()[1:]))
    results.append(("DFS", *run_dfs()[1:]))
    results.append(("UCS", *run_ucs()[1:]))
    results.append(("DLS (Limit=8)", *run_dls(8)[1:]))
    results.append(("IDDFS", *run_iddfs()[1:]))
    
    print(f"{'Algorithm':<15} | {'Nodes Expanded':<15} | {'Time (Seconds)'}")
    print("-" * 50)

    for name, nodes, t in results:
        print(f"{name:<15} | {nodes:<15} | {t:.6f}")

if __name__ == "__main__":
    compare()