from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start = None
        litter_positions = []

        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == 'S':
                    start = (i, j)
                elif c == 'L':
                    litter_positions.append((i, j))

        L = len(litter_positions)
        if L == 0:
            return 0

        litter_index = {pos: idx for idx, pos in enumerate(litter_positions)}
        full_mask = (1 << L) - 1

        sr, sc = start
        # best_energy[r][c][mask] = highest energy with which this
        # (position, mask) combo has been reached so far. Because BFS
        # processes states in non-decreasing step order, a new arrival
        # here with energy <= what's recorded is dominated (same-or-worse
        # steps AND same-or-worse energy) -> safe to prune.
        best_energy = [[[-1] * (1 << L) for _ in range(n)] for _ in range(m)]
        best_energy[sr][sc][0] = energy

        queue = deque([(sr, sc, energy, 0, 0)])  # r, c, energy_left, mask, steps
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, e, mask, steps = queue.popleft()

            if mask == full_mask:
                return steps  # BFS -> first time hitting full_mask is optimal

            if e == 0:
                continue  # stuck, and not on R (R would've refilled on arrival)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    ne = energy if cell == 'R' else e - 1
                    nmask = mask
                    if cell == 'L':
                        idx = litter_index.get((nr, nc))
                        if idx is not None:
                            nmask = mask | (1 << idx)

                    # Only explore if this beats the best energy already
                    # recorded for this (position, mask) — collapses the
                    # energy dimension instead of tracking every value of e
                    if ne > best_energy[nr][nc][nmask]:
                        best_energy[nr][nc][nmask] = ne
                        queue.append((nr, nc, ne, nmask, steps + 1))

        return -1