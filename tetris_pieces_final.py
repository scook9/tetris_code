import random

# Piece shapes
types = ["I", "J", "L", "O", "S", "T", "Z"]

# dictionary of pieces and their rotations. Key is tile type, value is a list of orientations
pieces = {
    # see IMPORTANT NOTE 2 for a debug / check code to make sure their pieces work
    "I": [
        [[0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        [[0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0]],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0]],
        [[0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0]
         ]
    ],
    "J": [
        [[2, 0, 0],
         [2, 2, 2],
         [0, 0, 0]],
        [[0, 2, 2],
         [0, 2, 0],
         [0, 2, 0]],
        [[0, 0, 0],
         [2, 2, 2],
         [0, 0, 2]],
        [[0, 2, 0],
         [0, 2, 0],
         [2, 2, 0]]
    ],
    "L": [
        [[0, 0, 3],
         [3, 3, 3],
         [0, 0, 0]],
        [[0, 3, 0],
         [0, 3, 0],
         [0, 3, 3]],
        [[0, 0, 0],
         [3, 3, 3],
         [3, 0, 0]],
        [[3, 3, 0],
         [0, 3, 0],
         [0, 3, 0]]
    ],
    "O": [
        [[0, 4, 4, 0],
         [0, 4, 4, 0],
         [0, 0, 0, 0]]
    ],
    "S": [
        [[0, 5, 5],
         [5, 5, 0],
         [0, 0, 0]],
        [[0, 5, 0],
         [0, 5, 5],
         [0, 0, 5]],
        [[0, 0, 0],
         [0, 5, 5],
         [5, 5, 0]],
        [[5, 0, 0],
         [5, 5, 0],
         [0, 5, 0]]
    ],
    "T": [
        [[0, 6, 0],
         [6, 6, 6],
         [0, 0, 0]],
        [[0, 6, 0],
         [0, 6, 6],
         [0, 6, 0]],
        [[0, 0, 0],
         [6, 6, 6],
         [0, 6, 0]],
        [[0, 6, 0],
         [6, 6, 0],
         [0, 6, 0]]
    ],
    "Z": [
        [[7, 7, 0],
         [0, 7, 7],
         [0, 0, 0]],
        [[0, 0, 7],
         [0, 7, 7],
         [0, 7, 0]],
        [[0, 0, 0],
         [7, 7, 0],
         [0, 7, 7]],
        [[0, 7, 0],
         [7, 7, 0],
         [7, 0, 0]]
    ]
}


# Tetrimino class
class Tetrimino:

    def __init__(self):
        self.type = "I"
        self.rotation = 0
        self.x, self.y = (3,18)

        # Set grid_ref manually - if left as none, blocks will fall and ignore the grid.
        self.grid_ref = None

    def reset(self):
        self.type = random.choice(types)
        self.rotation = 0
        self.x, self.y = (3,18)

    # NEW add return false to move
    def move(self, dx, dy):
        destination_x = self.x + dx
        destination_y = self.y + dy
        if not self.collision_check(destination_x, destination_y):
            self.x = destination_x
            self.y = destination_y
            # move succeeded
            return True
        # move failed
        return False


    def rotate(self, dr):
        new_rotation = (self.rotation + dr) % len(pieces[self.type])
        # NEW: Redefined rotation now that we have a collision check
        prev_rotation = self.rotation
        self.rotation = new_rotation
        if not self.collision_check(self.x, self.y):
            # rotate succeeded
            return
        # rotate failed
        self.rotation = prev_rotation

        # define a collision check function
    def collision_check(self, xPos, yPos):
        top_x, top_y = xPos, yPos
        tetrimino = pieces[self.type][self.rotation]
        tetrimino_height = len(tetrimino)
        tetrimino_width = len(tetrimino[0])

        for y in range(tetrimino_height):
            for x in range(tetrimino_width):
                # No need to check blank spaces of the tetrimino for collision.
                if tetrimino[y][x] != 0:
                    # out of bounds (walls or floor)
                    if top_x + x < 0 or top_x + x >= len(self.grid_ref[0]) or top_y + y < 0 or top_y + y >= len(
                            self.grid_ref):
                        return True
                    # Check vs grid
                    if self.grid_ref is not None and self.grid_ref[top_y + y][top_x + x] != 0:
                        return True
        # If you make it out of this loop without returning True, you're in the clear.
        return False
