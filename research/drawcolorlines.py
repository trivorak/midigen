from PIL import Image, ImageDraw

### Take in String and split by char len

## Defaults
#scaleSize = 1

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
for i in range(0,5-len(aListInt)%5):
	aListInt.append(0)

aListInt.append(0)
aListInt.append(0)

#for element in aListInt:
#	aWorkingList.append(round(element*scaleSize,0))

#aListInt = aWorkingList

im = Image.new("RGB",(256,256),(255,255,255))

draw = ImageDraw.Draw(im)

print(len(aListInt))

for i in range(0,len(aListInt)-2,5):
	draw.line(xy=(aListInt[i],aListInt[i+1],aListInt[i+5],aListInt[i+6]),fill=(aListInt[i+2],aListInt[i+3],aListInt[i+4]))

im.save("output.png")

