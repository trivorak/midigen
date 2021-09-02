from PIL import Image, ImageDraw

### Take in String and split by char len

## Defaults
scaleSize = 1

## Input Static for example
# a = input("Hex String: ")

with open("input.txt","r") as f:
	a = f.readlines()

#Convert to sring
a = str(a)

# Remove the [' & '] from string
a = a[2:(len(a)-2)]

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
for i in range(0,2-len(aListInt)%2):
	aListInt.append(0)

for element in aListInt:
	aWorkingList.append(round(element*scaleSize,0))

aListInt = aWorkingList

im = Image.new("RGB",(256*scaleSize,256*scaleSize),(255,255,255))

draw = ImageDraw.Draw(im)

draw.polygon(xy=aListInt,outline=(0,0,0))

im.save("output.png")

