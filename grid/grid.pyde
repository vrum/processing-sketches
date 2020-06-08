# Number of columns and rows in the grid
window_width = 1280
window_height = 800
rect_size = 60
nCols = (window_width-2*rect_size)/rect_size
nRows = (window_height-2*rect_size)/rect_size
sizes = [[1,1],[1,2],[2,1],[2,2]]
rects = []

def setup():
    global nCols, nRows, grid, sizes
    size(1280, 800)
    grid = makeGrid()
    for i in xrange(nRows):
        for j in xrange(nCols):
            # Initialize each object
            grid[i][j] = 0
    old_index = -1
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if free(grid, row_index, col_index):
                size_index = -1
                siz = sizes[0]         
                while True:
                    size_index = get_size()
                    siz = sizes[size_index]
                    if row_index+siz[0] <= len(grid) and col_index+siz[1] <= len(row):
                        if free_grid(grid, row_index, col_index, siz[0], siz[1]):
                            break
                    # print('adi', size_index, old_index)
                    if old_index >= 1 and old_index == size_index:
                        continue
                    old_index = size_index
                # print(row_index, col_index, siz)
                fill_grid(grid, row_index, col_index, siz[0], siz[1])
                r = Rect(rect_size, row_index, col_index, siz[1], siz[0], True, False)
                rects.append(r)
                rr = Rect(rect_size, row_index, col_index, siz[1], siz[0], False, True)
                rects.append(rr)
                # print(r)

def get_size():
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
            if grid[row+i][col+j] != 0:
                return False
    return True

def free(grid, row, col):
    return grid[row][col] == 0

def fill_grid(grid, row, col, dr, dc):
    for i in range(dr):
        for j in range(dc):
            # print(row+i, col+j)
            if grid[row+i][col+j] != 0:
                print('nope')
            grid[row+i][col+j] = 1

def makeGrid():
    global nCols, nRows
    grid = []
    for i in xrange(nRows):
        grid.append([])
        for j in xrange(nCols):
            grid[i].append(0)
    return grid

class Rect():    
    def __init__(self, siz, row, col, w, h, dofill, dostroke):
        # self.color = ()
        outer_margin = rect_size
        inner_margin = rect_size//8
        tolerance = inner_margin//2+1
        self.siz = siz
        
        x1 = outer_margin+col*siz+inner_margin
        y1 = outer_margin+row*siz+inner_margin
        x2 = outer_margin+(col+w)*siz-inner_margin
        y2 = outer_margin+(row+h)*siz-inner_margin

        x3 = x2+int(random(tolerance*2)-tolerance)
        y3 = y1+int(random(tolerance*2)-tolerance)
        x4 = x1+int(random(tolerance*2)-tolerance)
        y4 = y2+int(random(tolerance*2)-tolerance)

        x1 = x1+int(random(tolerance*2)-tolerance)
        y1 = y1+int(random(tolerance*2)-tolerance)
        x2 = x2+int(random(tolerance*2)-tolerance)
        y2 = y2+int(random(tolerance*2)-tolerance)

        self.s = createShape()
        self.s.beginShape()
        if dostroke:
            self.s.setStroke(True)
            self.s.strokeWeight(rect_size//16)
        else:
            self.s.noStroke()

        if dofill:
            self.s.fill(int(random(128)+128),int(random(196)+64),int(random(196)+64))
        else:
            self.s.noFill()    
        self.s.vertex(x1, y1)
        self.s.vertex(x3, y3)
        self.s.vertex(x2, y2)
        self.s.vertex(x4, y4)
        self.s.endShape(CLOSE)
    
    def __str__(self):
        return '{} {} - {} {}'.format(self.x, self.y, self.dx, self.dy) 
    
    def draw(self):
        noStroke()
        # stroke(3)
        # rect(self.x, self.y, self.dx, self.dy)
        shape(self.s, 0, 0)

    
def draw():
    global rects
    background(255)
    # The counter variables i and j are also the column and row numbers and 
    # are used as arguments to the constructor for each object in the grid.  
    for r in rects:
        r.draw()
