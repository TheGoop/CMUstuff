import string

class Rectangle(object):
	def __init__(self, x, y, length = 80, height = 80,
	 selected = False, color = "White"):
		self.x = x #top left x
		self.y = y # top left y
		self.length = length #length of rectangle
		self.height = height #height of rectangle
		self.color = color
		self.selected = selected #whether or not it is selected

	def draw(self, canvas):
		if not self.selected: #if not selected draws in its own color
			canvas.create_rectangle(self.x, self.y,
				self.x + self.length, self.y + self.height, fill = self.color)
		else: #if it is selected draws in selected color
			canvas.create_rectangle(self.x, self.y,
				self.x + self.length, self.y + self.height, 
				fill = "LightSteelBlue1")

	def select(self): #switches selected state
		if self.selected:
			self.selected = False
		else:
			self.selected = True

class Txt(object):

	def __init__(self, text = "", color = "black", style = "Helvetica", 
		size = 18, bold = False, underlined = False):

		self.text = text
		self.color = color
		self.style = style
		self.size = size
		self.bold = bold
		self.underlined = underlined

	def write(self, canvas, cell, data): #draws the txt instance
		canvas.create_text(cell.x + data.cellWidth//2, cell.y + 
			data.cellHeight//2, text=self.text, fill=self.color, 
			font=self.makeFont())

	def makeFont(self): 
	#combines txt properties to form the font used to draw txt
		bold = ""
		underlined = ""
		if self.bold:
			bold = "bold"
		if self.underlined:
			underlined = "underline"
		return "%s %d %s %s" % (self.style, self.size, bold, underlined)

# Animation Starter Code, Focus on timerFired

from tkinter import *

####################################
# customize these functions
####################################

def loadCells(data): #loads cells with empty rectangles
    for r in range(data.numOfRows):
    	row = []
    	for c in range(data.numOfCols):
    		row.append(Rectangle(data.marginX + data.cellWidth*r, 
    			data.marginY + data.cellHeight*c, data.cellWidth,
    			 data.cellHeight))

    	data.cells.append(row)	

def loadText(data): #loads cells with empty txt
    for r in range(data.numOfRows):
    	row = []
    	for c in range(data.numOfCols):
    		row.append(Txt())
    	data.text.append(row)	

def init(data):
    # load data.xyz as appropriate
    data.marginX = 20 
    data.marginY = 20
    data.selected = [] #where the selected cells will be selected
    data.numOfRows = 10
    data.numOfCols = 10
    data.cellWidth = (data.width-data.marginX)//data.numOfCols
    data.cellHeight = (data.height-data.marginY)//data.numOfRows
    data.cells = []
    loadCells(data)
    data.text = []
    loadText(data)
    
def getSelectedCell(x, y, data): #figures out which cell the coordinates were in
    for r in range(len(data.cells)):
    	for c in range(len(data.cells[r])):
    		endX = data.cells[r][c].x + data.cellWidth
    		if x >= data.cells[r][c].x and x < endX:
    			endY = data.cells[r][c].y + data.cellHeight
    			if y >= data.cells[r][c].y and y < endY:
    				return [r, c]

def clearSelection(data): #unselects all
	for i in data.selected:
	    i.select()
	data.selected = []

def mousePressed(event, data):
    # use event.x and event.y
    #so long as the mouse is pressed within the cells
    if event.x >= data.marginX and event.x < data.width: 
    	if event.y >= data.marginY and event.y < data.height:
		    clearSelection(data) #clears the selection
		    #makes new selection
		    c = getSelectedCell(event.x, event.y, data)
		    data.cells[c[0]][c[1]].select()
		    data.selected.append(data.cells[c[0]][c[1]])
		    data.coords = c

def wrapAround(data):
	if data.coords[0] == 0: #top
		data.coords[0] = data.numOfRows - 1

	if data.coords[0] == data.numOfRows - 1: #bottom
		data.coords[0] = 0

	if data.coords[1] == 0: #left
		data.coords[1] = data.numOfCols -1

	if data.coords[1] == data.numOfCols -1: #right
		data.coords[1] = 0
def key(event, data):
    if event.keysym == "BackSpace":
        data.text[r][c].text = data.text[r][c].text[:-1]

    if event.keysym == "Return":
        clearSelection(data)
    
    #moves selected box in direction
    elif event.keysym in ["Left", "Right", "Up", "Down"]: 
        # wrap around
        if event.keysym == "Left":
            data.coords[0] -= 1

        if event.keysym == "Right":
            data.coords[0] += 1

        if event.keysym == "Up":
            data.coords[1] -= 1

        if event.keysym == "Down":
            data.coords[1] += 1
        #wraps around until I can add scroll feature
        wrapAround(data)
        #changes selection
        clearSelection(data)
        data.cells[data.coords[0]][data.coords[1]].select()
        data.selected.append(data.cells[data.coords[0]][data.coords[1]])


def keyPressed(event, data):
    # use event.char and event.keysym
    if not data.selected == []:
    	r = data.coords[0]
    	c = data.coords[1]
    	normChar = string.ascii_lowercase+string.digits+string.ascii_uppercase
    	if event.char in normChar:
    		data.text[r][c].text += event.char

    	else:
            key(event,data)

def timerFired(data):
    pass

def drawXMargin(canvas, data): #draws column labels
	for i in range(data.numOfCols):
		canvas.create_text(data.marginX + data.cellWidth//2 + 
			(data.cellWidth*i), data.marginY//2,
		 text = chr(i+65), fill = "Black", font="Helvetica 14 bold underline")

def drawYMargin(canvas, data): #draws row labels
	for i in range(data.numOfCols):
		canvas.create_text(data.marginX//2, data.marginY + 
			data.cellHeight//2 + (data.cellHeight*i),
		 text = str(i), fill = "Black", font="Helvetica 14 bold underline")

def redrawAll(canvas, data):
    # draw in canvas
    drawXMargin(canvas,data)
    drawYMargin(canvas,data)

    for r in data.cells: #draws all cells
    	for c in r:
    		if c not in data.selected:
    			c.selected = False
    		else:
    			c.selected = True
    		c.draw(canvas)

    for r in range(len(data.text)): #draws all text
    	for c in range(len(data.text[r])):
    		cell = data.cells[r][c]
    		data.text[r][c].write(canvas, cell, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)


    def testAll(data):
        #test creating txt instance
        t = Txt()
        values = [t.text, t.color, t.style, t.size, t.bold, t.underlined]
        assert (values == ["", "black", "Helvetica", 18, False, False])
        t = Txt("I hate assertions")
        values = [t.text, t.color, t.style, t.size, t.bold, t.underlined]
        shouldBe = ["I hate assertions", "black", "Helvetica", 18, False, False]
        assert (values == shouldBe)
        t = Txt("I hate assertions", "white")
        values = [t.text, t.color, t.style, t.size, t.bold, t.underlined]
        shouldBe = ["I hate assertions", "white", "Helvetica", 18, False, False]
        assert (values == shouldBe)

        loadText(data2)
        loadCells(data2)
        assert(getSelectedCell(50,50,data2) == [0,0])
        assert(getSelectedCell(500,500,data2) == [6,6])
        assert(getSelectedCell(750,500, data2) == [9,6])

        data2.selected.append(Rectangle(500,500))
        clearSelection(data2)
        assert(data2.selected == [])
        data2.selected.append(Rectangle(500,500))
        data2.selected.append(Rectangle(750,800))
        data2.selected.append(Rectangle(190,870))
        clearSelection(data2)
        assert(data2.selected == [])

        print("Passed All Assertions!")



    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data2 = Struct()
    data.width = width 
    data.height = height
    data2.width = width
    data2.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    init(data2)

    testAll(data2)

    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)