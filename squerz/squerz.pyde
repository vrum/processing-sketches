# Number of columns and rows in the grid
window_width = 1024
window_height = 768
rect_size = 256
nCols = (window_width - 0 * rect_size / 2) / rect_size
nRows = (window_height - 0 * rect_size / 2) / rect_size
sizes = [[1, 1], [1, 2], [2, 1], [2, 2]]
rects = []
# COLORS = [[230, 64, 64], [230, 166, 41], [32, 140, 134], [196, 188, 167]]
COLORS = [[237, 118, 112], [167, 219, 216], [127, 199, 175], [218, 216, 167]]
# COLORS = [[179, 216, 216], [236, 195, 188], [232, 217, 198], [185, 187, 201]]
pressed = False


def setup():
    # global nCols, nRows, grid, sizes
    global window_height, window_width
    size(window_width, window_height)
    setup_grid()


def setup_grid():
    global window_height, window_width, nCols, nRows, grid, sizes, rects, rect_size, COLORS
    rects = []
    background(255)
    for x in range(nCols):
        for y in range(nRows):
            left = x * rect_size
            right = left + rect_size
            top = y * rect_size
            bottom = top + rect_size
            print(left, top, right, bottom)
            setup_rects(0, rect_size, left, right, top, bottom)


def setup_rects(step, squer_size, left, right, top, bottom):
    global nCols, nRows, grid, sizes, rects, rect_size, COLORS
    split = False

    switch = {
        0 : int(random(100)) > 5,
        1 : int(random(100)) > 20,
        2 : int(random(100)) > 30,
        3 : int(random(100)) > 40,
        4 : int(random(100)) > 50,
    }
    split = switch.get(step, False)

    if split:
        hmiddle = left + (right - left) / 2
        vmiddle = top + (bottom - top) / 2
        setup_rects(step + 1, squer_size / 2, left, hmiddle, top, vmiddle)
        setup_rects(step + 1, squer_size / 2, hmiddle, right, top, vmiddle)
        setup_rects(step + 1, squer_size / 2, left, hmiddle, vmiddle, bottom)
        setup_rects(step + 1, squer_size / 2, hmiddle, right, vmiddle, bottom)
        print("nope", squer_size, step)
    else:
        color_index = get_color_index()
        r = Rect(
            squer_size, left, top, squer_size, squer_size, color_index, True, False
        )
        # print(step, left, right, top, bottom, squer_size, color_index)
        rects.append(r)
        # print('yep', squer_size, step, color_index)


def get_color_index():
    number = random(100)
    if number > 90:
        return 3
    if number > 70:
        return 2
    if number > 50:
        return 1
    return 0


def free_grid(grid, row, col, dr, dc):
    # print(row, col, dr, dc)
    for i in range(dr):
        for j in range(dc):
            if grid[row + i][col + j] != 0:
                return False
    return True


def free(grid, row, col):
    return grid[row][col] == 0


def fill_grid(grid, row, col, dr, dc):
    for i in range(dr):
        for j in range(dc):
            # print(row+i, col+j)
            if grid[row + i][col + j] != 0:
                print("nope")
            grid[row + i][col + j] = 1


def makeGrid():
    global nCols, nRows
    grid = []
    for i in xrange(nRows):
        grid.append([])
        for j in xrange(nCols):
            grid[i].append(0)
    return grid


class Rect:
    def __init__(self, siz, left, top, w, h, color_index, dofill, dostroke):
        # self.color = ()
        global COLORS
        outer_margin = 0
        inner_margin = 2
        tolerance = 0

        x1 = outer_margin + left + inner_margin
        y1 = outer_margin + top + inner_margin
        x2 = outer_margin + left + w - inner_margin
        y2 = outer_margin + top + h - inner_margin

        x3 = x2 + int(random(tolerance * 2) - tolerance)
        y3 = y1 + int(random(tolerance * 2) - tolerance)
        x4 = x1 + int(random(tolerance * 2) - tolerance)
        y4 = y2 + int(random(tolerance * 2) - tolerance)

        x1 = x1 + int(random(tolerance * 2) - tolerance)
        y1 = y1 + int(random(tolerance * 2) - tolerance)
        x2 = x2 + int(random(tolerance * 2) - tolerance)
        y2 = y2 + int(random(tolerance * 2) - tolerance)
        self.s = createShape()
        self.s.beginShape()
        if dostroke:
            self.s.setStroke(True)
            self.s.stroke(0)
            self.s.strokeWeight(rect_size // 16)
        else:
            self.s.noStroke()

        if dofill:
            # self.s.fill(int(random(128)+128),int(random(196)+64),int(random(196)+64))
            index = int(random(4))
            self.s.fill(COLORS[index][0], COLORS[index][1], COLORS[index][2])
        else:
            self.s.noFill()
        # print(x1, y1, x3, y3, x2, y2, x4, y4)
        self.s.vertex(x1, y1)
        self.s.vertex(x3, y3)
        self.s.vertex(x2, y2)
        self.s.vertex(x4, y4)
        self.s.endShape(CLOSE)

    def __str__(self):
        # return '{} {} - {} {}'.format(self.x1, self.y1, self.x2, self.y2)
        return "{}".format(self.s)

    def draw(self):
        noStroke()
        # stroke(3)
        # rect(self.x, self.y, self.dx, self.dy)
        shape(self.s, 0, 0)


def draw():
    global rects, pressed
    background(255)
    if keyPressed:
        if not pressed:
            setup_grid()
            pressed = True
        else:
            pressed = False
    # The counter variables i and j are also the column and row numbers and
    # are used as arguments to the constructor for each object in the grid.
    for r in rects:
        r.draw()
