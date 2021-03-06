from itertools import count, product


class Puzzle2:
    directions = ['top', 'left', 'bottom', 'right']

    def __init__(self, y, x, grid, data_location):
        self.data_location = data_location
        self.map = grid
        self.y = y
        self.x = x
        self.direction = 'top'
        self.ring_level = 1

    def set_next_direction(self):
        direction_index = self.directions.index(self.direction)
        self.direction = self.directions[(direction_index + 1) % 4]
        if self.direction == 'top':
            self.x += 1
            self.set_case()

    def set_next_coord(self):
        next_moves = (
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        )
        direction_index = self.directions.index(self.direction)
        move_y, move_x = next_moves[direction_index]
        self.y += move_y
        self.x += move_x
        self.set_case()

    def set_case(self):
        sum_of_adjacent_squares = 0
        # Get a list of the 8 directions around the current position.
        # The current position is also given, but since his value is 0 it's not a problem.
        for dir_y, dir_x in product([1, 0, -1], repeat=2):
            adjacent_square = self.map[self.y + dir_y][self.x + dir_x]
            sum_of_adjacent_squares += adjacent_square

        if sum_of_adjacent_squares > self.data_location:
            print(f"Puzzle 2: {sum_of_adjacent_squares}")
            exit()
        self.map[self.y][self.x] = sum_of_adjacent_squares

    def loop(self):
        side = 3
        while True:
            lower = (side - 2) ** 2
            upper = side ** 2
            i = self.ring_level

            for val in range(lower + 1, upper + 1):
                if i % (side - 1) == 0:
                    self.set_next_direction()
                self.set_next_coord()
                i += 1

            side += 2
            self.ring_level += 1


def get_square_level_and_side_len(data: int) -> (int, int):
    for index, value in enumerate(count(start=1, step=2)):
        if value ** 2 > data:
            return index, value


def get_value_axis(data_location: int, side_len: int) -> int:
    start_value = (side_len - 2)**2 + 1
    end_value = side_len ** 2
    square = [end_value] + list(range(start_value, end_value + 1))
    position_on_side = square.index(data_location) % (side_len - 1)
    axis = abs(position_on_side - side_len // 2)
    return axis


def puzzle_1(data_location: int) -> int:
    square_level, square_side_len = get_square_level_and_side_len(data_location)
    alignment = get_value_axis(data_location, square_side_len)
    return square_level + alignment


def puzzle_2(data_location: int):
    grid = [[0] * 20 for _ in range(20)]
    grid[10][10] = 1
    grid[10][11] = 1
    coord = Puzzle2(10, 11, grid, data_location)

    coord.loop()


if __name__ == "__main__":
    puzzle_input = 368078

    result_1 = puzzle_1(puzzle_input)
    print(f"Puzzle 1: {result_1}")

    puzzle_2(puzzle_input)
