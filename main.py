from maze import Maze, Cell, Window

def main():
	maze = Maze(0, 0, 10, 10, 10, 10, Window(800, 600))
	maze.solve()

if __name__ == "__main__":
    window = Window(800, 600, "paco")
    maze = Maze(10, 10, 10, 10, 50, 50, window)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visted()
    maze.solve()
    window.wait_for_close()