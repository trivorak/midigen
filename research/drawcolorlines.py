from PIL import Image, ImageDraw

### Take in String and split by char len

## Defaults
scaleSize = 1

## Input Static for example
# a = input("Hex String: ")

with open("input.txt","r") as f:
	a = f.read()

# Remove Carriage Returns
a = a.replace('\n','')

#Convert to string
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

im = Image.new("RGBA",(256*scaleSize,256*scaleSize),(0,0,13,255))

draw = ImageDraw.Draw(im)

print(len(aListInt))

for i in range(0,len(aListInt)-2,5):
	draw.line(xy=(round(aListInt[i]*scaleSize,0),round(aListInt[i+1]*scaleSize,0),round(aListInt[i+5]*scaleSize,0),round(aListInt[i+6]*scaleSize,0)),fill=(aListInt[i+2],aListInt[i+3],aListInt[i+4],255))

im.save("outputColorLines.png")
# Remove Test