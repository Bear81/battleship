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
    Print the grid with row labels and column headers
    """
    column_headers = " " + " ".join(str(i + 1) for i in range(len(grid)))
    print(column_headers)

    for i, row in enumerate(grid):
        row_label = chr(ord("A") + i)
        print(f"{row_label} {' '.join(row)}")
    print()


# Create and print an empty 10x10 grid
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


def get_player_guess():
    """
    Ask the user for their guess, validate the input and row and column number
    """
    while True:
        guess = input("Enter your guess (e.g., A1, B4 etc.): ").upper()
        if len(guess) < 2 or not guess[0].isalpha or not guess[1].isdigit():
            print("Invalid Input. Please enter a letter followed by a number.")
            continue
        row, col = ord(guess[0]) - ord("A"), int(guess[1]) - 1
        if row < 0 or row >= grid_size or col < 0 or col >= grid_size:
            print("Invalid input. Please enter a guess within the grid")
            continue

        return row, col

get_player_guess()


remaining_guesses = 30


def run_player_guess():
    """
    Process the players guess.
    - if it's a hit, mark the grid with an 'X'
    - If it's a miss, mark the grid with 'O'
    -if the cell has already been guessed, inform the player
    Returns True if its a hit, False otherwise
    """
    if grid[row][col] in ["X", "O"]:
        print("you've already guessed this spot, try again. ")
        return False, remaining_guesses
    
    if(row,col) in ships:
        print("HIT!")
        grid[row][col] = "X"
        remaining_guesses -= 1
        return True, remaining_guesses
    else:
        print("Miss!")
        grid[row][col] = "O"
        remaining_guesses -= 1
        return False, remaining_guesses