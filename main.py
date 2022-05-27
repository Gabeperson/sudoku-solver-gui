import eel
import json

eel.init("web")

solved_grid = None
solved = False


def possible(y, x, n, grid):
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for ii in range(0, 3):
            if grid[y0+i][x0+ii] == n:
                return False
    return True


def solve(grid):
    global solved
    global solved_grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y, x, n, grid):
                        grid[y][x] = n
                        solve(grid)
                        if solved:
                            return
                        grid[y][x] = 0
                return
    solved_grid = grid
    solved = True


@eel.expose
def solve_grid(grid_string):
    global solved
    solved = False
    grid = json.loads(grid_string)
    solve(grid)
    return json.dumps(solved_grid)


eel.start("index.html", size=(540, 620))
