import math
from PIL import Image

# Create blank variables
aList = []
aListInt = []
aWorkingList = []

# Defaults
width = 16
height = 9

# Define Functions
def getHeight(pixels,rWidth,rHeight):
	return math.ceil(math.sqrt((pixels*rHeight/rWidth)))

def getWidth(pixels,rWidth,rHeight):
	return math.ceil(rWidth*getHeight(pixels,rWidth,rHeight)/rHeight)  

# Input Hex from local text file
with open("input.txt","r") as f:
	a = f.readlines()

# Convert input into a string
a = str(a)

#Remove the [' & '] from string - Windows endline
a = a[2:(len(a)-2)]

# Split by every 2 characters and append to "blank list"
for i in range(0,len(a),2):
	aList.append(a[i:i+2])

# Loop hex to int into new list 
for element in aList:
	aListInt.append(int(element,16))

	# Append so list is in groups of 3
for i in range(0,3-len(aListInt)%3):
	aListInt.append(0)


totalPixels = aListInt

#DBG
print(len(totalPixels))

# Create a new File to draw pixels
im = Image.new("RGB",(getWidth(len(totalPixels)/3,width,height),getHeight(len(totalPixels)/3,width,height)),(0,0,0))
pixels = im.load()
index = 0

# Drawing Loop
for i in range(0,len(totalPixels),3):
	pixels[index%im.width,math.floor(index/im.width)] = (totalPixels[i],totalPixels[i+1],totalPixels[i+2])
	index = index + 1

im.save("outputPixels.png")