from collections import deque
def king_escape(grid, N):
# BFS implementation checking 8 directions
# and avoiding '#' cells
   if grid == '#' or grid == 'T':
        return 0 if grid == 'T' else "TRAPPED"
        
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}
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

    # NOT YET CHECK IF THIS CORRECT
    



