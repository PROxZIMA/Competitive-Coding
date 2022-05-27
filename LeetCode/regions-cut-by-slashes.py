from collection import defaultdict


class Cell:
    def __init__(self, ur, dl, ul, dr):
        self.ur = ur
        self.dl = dl
        self.ul = ul
        self.dr = dr

    def get_directions(self):
        return [self.ur, self.dl, self.ul, self.dr]

    def __repr__(self):
        return f'ur {self.ur} dl {self.dl} ul {self.ul} dr {self.dr}'

directions = {
    ' ' : (1, 1, 1, 1),
    '/' : (0, 0, 1, 1),
    '\\': (1, 1, 0, 0)
}

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        cell_map = {}
        visited = defaultdict(lambda : 0)
        n = len(grid)

        def get_region(i, j, cell_map, visited, entry=None):
            if not (0 <= i < n and 0 <= j < n):
                return 0

            if abs(visited[(i, j)]) == 1:
                return 1

            cell = cell_map[(i, j)]
            direction = cell.get_directions()

            if all(direction): # empty space
                visited[(i, j)] = 1
                return  get_region(i - 1, j, cell_map, visited, 2) ||
                        get_region(i + 1, j, cell_map, visited, 0) ||
                        get_region(i, j - 1, cell_map, visited, 1) ||
                        get_region(i, j + 1, cell_map, visited, 3)
            if direction[2]: # /
                if visited[(i, j)] == 0.5: # upper triangle visited
                    if entry == 0 or entry == 3: # comming in from top or left
                        return 0
                    visited[(i, j)] = 1
                    if entry == 1: # comming in from right
                        return get_region(i + 1, j, cell_map, visited, 0)
                    if entry == 2: # comming in from bottom
                        return get_region(i, j + 1, cell_map, visited, 3)
                    # comming in from right or bootom or main loop
                    return  get_region(i + 1, j, cell_map, visited, 0) |
                            get_region(i, j + 1, cell_map, visited, 3)
                if visited[(i, j)] == -0.5: # lower triangle visited
                    if entry == 1 or entry == 2: # comming in from top or left
                        return 0
                    visited[(i, j)] = -1
                    if entry == 3: # comming in from left
                        return get_region(i - 1, j, cell_map, visited, 2)
                    if entry == 0: # comming in from top
                        return get_region(i, j - 1, cell_map, visited, 1)
                    # comming in from left or top or main loop
                    return  get_region(i - 1, j, cell_map, visited, 2) |
                            get_region(i, j - 1, cell_map, visited, 1)
            if direction[0]: # \
                if visited[(i, j)] == 0.5: # upper triangle visited
                    if entry == 0 or entry == 3: # comming in from top or left
                        return 0
                    if entry == 1: # comming in from right
                        return get_region(i + 1, j, cell_map, visited, 0)
                    if entry == 2: # comming in from bottom
                        return get_region(i, j + 1, cell_map, visited, 3)
                    # comming in from right or bootom or main loop
                    return  get_region(i + 1, j, cell_map, visited, 0) |
                            get_region(i, j + 1, cell_map, visited, 3)
                if visited[(i, j)] == -0.5: # lower triangle visited
                    if entry == 1 or entry == 2: # comming in from top or left
                        return 0
                    if entry == 3: # comming in from left
                        return get_region(i - 1, j, cell_map, visited, 2)
                    if entry == 0: # comming in from top
                        return get_region(i, j - 1, cell_map, visited, 1)
                    # comming in from left or top or main loop
                    return  get_region(i - 1, j, cell_map, visited, 2) |
                            get_region(i, j - 1, cell_map, visited, 1)

        for i in range(n):
            for j in range(n):
                cell_map[(i, j)] = Cell(*directions[grid[i][j]])
        counter = 0
        for i in range(n):
            for j in range(n):
                if visited[(i, j)] == 1:
                    continue
                cell = cell_map[(i, j)]
                if grid[i][j] =:
                else:
