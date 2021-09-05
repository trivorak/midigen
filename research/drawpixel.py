import math

# Input Ratio 16:9 for example
width = 16
height = 9

totalPixels = 3861837

# Functions
def getHeight(pixels,rWidth,rHeight):
	return math.ceil(math.sqrt((pixels*rHeight/rWidth)))

def getWidth(pixels,rWidth,rHeight):
	return math.ceil(rWidth*getHeight(pixels,rWidth,rHeight)/rHeight)