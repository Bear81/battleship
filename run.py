import random


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


def print_grid(grid):
    """
    Print the grid
    """
    for row in grid:
        print(" ".join(row))
    print()


# Create abd print an empty 10x10 grid
grid_size = 10
grid = build_grid(grid_size)


# Functions to place ships.
# Where to place them and check if they can be placed.

def can_place_ship(grid, row, col, length, orientation):
    """Check if a ship can be placed on the grid."""
    if orientation == 'H':  # Horizontal
        if col + length > len(grid):  # Check if ship goes off grid
            return False
        for i in range(length):
            if grid[row][col + i] != '~':  # Check if cell is already occupied
                return False
    else:  # Vertical
        if row + length > len(grid):  # Check if ship goes off grid
            return False
        for i in range(length):
            if grid[row + i][col] != '~':  # Check if cell is already occupied
                return False
    return True


def place_ship(grid, length):
    """Place a ship of given length on the grid."""
    placed = False
    while not placed:
        row = random.randint(0, len(grid) - 1)
        col = random.randint(0, len(grid) - 1)
        orientation = random.choice(
            ['H', 'V'])  # 'H' for horizontal, 'V' for vertical

        if can_place_ship(grid, row, col, length, orientation):
            # Place the ship
            for i in range(length):
                if orientation == 'H':
                    grid[row][col + i] = 'S'
                else:
                    grid[row + i][col] = 'S'
            placed = True


# Place battleships of lengths 3, 4, 5, and 6
ship_lengths = [3, 4, 5, 6]
for length in ship_lengths:
    place_ship(grid, length)

# Print the grid with ships
print_grid(grid)
