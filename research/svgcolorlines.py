from PIL import Image, ImageDraw
import drawsvg as draw

## Input Static for example
# a = input("Hex String: ")

# Define helper functions
def getHexString(input):
	return str(hex(input))

def clipHexHeader(input):
	return input[2:]

def checkStringLength(input):
	if len(input)<2:
		return "0"+input
	else:
		return input

def makeHexString(color1,color2,color3):
	return "#"+color1+color2+color3

def getHexFunction(color1,color2,color3):
	return makeHexString(checkStringLength(clipHexHeader(getHexString(color1))),checkStringLength(clipHexHeader(getHexString(color2))),checkStringLength(clipHexHeader(getHexString(color3))))

with open("input.txt","r") as f:
	a = f.read()

# Remove Carriage Returns
a = a.replace('\n','')

#Convert to sring
a = str(a)

# Create blank list
aList = []
aListInt = []
aWorkingList = []

# Split by every 2 characters and append to "blank list"
for i in range(0,len(a),2):
	aList.append(a[i:i+2])

# Loop hex to int into new list
for element in aList:
	aListInt.append(int(element,16))

# Append so list is in grounps (fix coordinate errors)
for i in range(0,5-len(aListInt)%5):
	aListInt.append(0)

aListInt.append(0)
aListInt.append(0)

print(aListInt)

d = draw.Drawing(256, 256, origin=(0,0),displayInline=False)

for i in range(0,len(aListInt)-2,5):
	d.append(draw.Line(aListInt[i], 256-aListInt[i+1], aListInt[i+5], 256-aListInt[i+6],stroke=getHexFunction(aListInt[i+2],aListInt[i+3],aListInt[i+4]), stroke_width=0.2))

d.save_svg('test.svg')
