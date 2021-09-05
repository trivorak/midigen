import math
from PIL import Image

# Input Hex from local text file
with open("input.txt","r") as f:
	a = f.readlines()

# Convert input into a string
a = str(a)

#Remove the [' & '] from string
a = a[2:(len(a)-2)]

# Create blank variables
aList = []
aListInt = []
aWorkingList = []

# Split by every 2 characters and append to "blank list"
for i in range(0,len(a),2):
	aList.append(a[i:i+2])

# Loop hex to int into new list 
for element in aList:
	aListInt.append(int(element,16))

	# Append so list is in groups of 3
for i in range(0,3-len(aListInt)%3):
	aListInt.append(0)

# Input Ratio 16:9 for example
width = 16
height = 9

totalPixels = aListInt

# Functions
def getHeight(pixels,rWidth,rHeight):
	return math.ceil(math.sqrt((pixels*rHeight/rWidth)))

def getWidth(pixels,rWidth,rHeight):
	return math.ceil(rWidth*getHeight(pixels,rWidth,rHeight)/rHeight)  