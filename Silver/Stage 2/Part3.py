# 📌 Part 3 – Maze Escape with Teleportation Portals (Grid BFS)

"""
Task:
Navigate N * M grid maze from top-left (0, 0) to bottom-right (N-1, M-1) in the minimum number of moves
. = Safe path
x = Wall / Obstacle
* = Teleportation Portal
Portal Teleportation Rule: Stepping onto ANY portal * allows you to instantly jump to ANY other portal * on the board in 1 move.

Rule: 
1. Standard BFS Queue stores (row, col, distance)
2. Move in 2 directions (Down, Right) onto . or * tiles
3. Warp feature: If step on * portal, can jump to all other * portals on the board instantly

Explanation:
You are trapped in a grid maze!
. = Normal Floor (takes 1 step)
x = Wall (cannot walk here)
* = Teleporter Pad!
Magic Rule: The moment you step on ANY * teleporter pad, you can instantly warp to ALL OTHER * teleporter pads on the map in just 1 step!
"""

# Replace with different inputs 
# Here is input 1 from KLCC 2025 Silver Stage 2 Part 3 Input 1
raw_input = """
..*.......
.xx.xx.xx.
..xx....x.
.x..xx....
.xxxxx..x.
....xx..x.
.*....x...
.....x....
"""

grid = [line.strip() for line in raw_input.strip().splitlines() if line.strip()]

from collections import deque

def escape_portal_maze(grid, N, M):
    # 1. Locate all teleportation portals '*'
    portals = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] == '*':
                portals.append((r,c))
    
    queue = deque([(0,0,0)]) # row, column, steps
    visited = {(0,0)}
    used_portals = False

    while queue:
        r, c, dist = queue.popleft()

        # Reached the exit (bottom-right corner)
        if r == N - 1 and c == M - 1:
            return dist

        # Standard movement (Down, Right)
        for dr, dc in [(1,0), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 'x':
                if (nr,nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr,nc,dist+1))

        # Teleport Logic
        if grid[r][c] == '*' and not used_portals:
            used_portals = True # Warp to all portals at once
            for pr, pc in portals:
                    visited.add((pr,pc))
                    queue.appendleft((pr,pc,dist)) # Append left will move this queue to the first queue (by default it will be the last queue)

    return -1 # Escape blocked


# Example
print(escape_portal_maze([".xx", "..*", ".xx", ".*."], 4, 3))
# Ans: 4

# Input 1
print(escape_portal_maze(grid, 8, 10))
# Ans: 16

# Input 2
print(escape_portal_maze(grid, 25, 25))
# Ans: 47

# Input 3
print(escape_portal_maze(grid, 50, 50))
# Ans: 97