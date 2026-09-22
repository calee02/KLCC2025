from collections import deque

def king_escape(grid, N):
    # Fix: Check starting cell (0, 0)
    if grid[0][0] == '#' or grid[0][0] == 'T':
        return 0 if grid[0][0] == 'T' else "TRAPPED"
        
    queue = deque([(0, 0, 0)])  # Stores (row, col, distance)
    visited = {(0, 0)}
    # 8 possible directions (Up, Down, Left, Right & 4 Diagonals)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if grid[r][c] == 'T':
            return dist
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                if grid[nr][nc] != '#':
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
                    
    return "TRAPPED"

# --- Driver Code to read input and see the output ---
if __name__ == "__main__":
    N = int(input().strip())
    grid = [input().strip() for _ in range(N)]
    
    result = king_escape(grid, N)
    print(result)

## NEED TO CHECK AGAIN
# Sample output 1: 3
# Sample output 2: TRAPPED
# Output 1: 18
# Output 2: 28
# Output 3: 200