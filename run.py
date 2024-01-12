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

def can_place_ship(ships, row, col, length, orientation, grid_size):
    """Check if a ship can be placed on the grid."""
    if orientation == 'H':  # Horizontal
        if col + length > grid_size:  # Check if ship goes off grid
            return False
        for i in range(length):
            if (row, col + i) in ships:  # Check if cell is already occupied
                return False
    else:  # Vertical
        if row + length > grid_size:  # Check if ship goes off grid
            return False
        for i in range(length):
            if (row + i, col) in ships:  # Check if cell is already occupied
                return False
    return True


ships = []


def place_ship(ships, length, grid_size):
    """
    Place a ship of given length on the grid,
    storing its coordinates in ships list.
    """
    placed = False
    while not placed:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        # 'H' for horizontal, 'V' for vertical
        orientation = random.choice(['H', 'V'])

        ship_coords = []  # Temporary list to hold ship coordinates
        if can_place_ship(ships, row, col, length, orientation, grid_size):
            # Add ship coordinates
            for i in range(length):
                if orientation == 'H':
                    ship_coords.append((row, col + i))
                else:
                    ship_coords.append((row + i, col))
            placed = True
        if placed:
            # Add the ship coordinates to the main list
            ships.extend(ship_coords)


# Place battleships of lengths 3, 4, 5, and 6
ship_lengths = [3, 4, 5, 6]
for length in ship_lengths:
    place_ship(ships, length, grid_size)

# Print the grid with ships
print_grid(grid)
