import randon


def build_grid(size):
    """
    Create a size x size grid, initialised with a water symbol
    """
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append("~")
        grid.append(row)
    return grid


def print_grid():
    """
    Print the grid
    """
    for row in grid:
        print(" ".join(row))
    print()


# Create abd print an empty 10x10 grid
grid_size = 10
grid = build_grid(grid_size)
print_grid(grid)
