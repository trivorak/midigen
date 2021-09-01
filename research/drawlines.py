from PIL import Image, ImageDraw

### Take in String and split by char len

# Input Static for example
a = input("Hex String: ")

# Create blank list
aList = []
aListInt = []

# Split by every 2 characters and append to "blank list"
for i in range(0,len(a),2):
	aList.append(a[i:i+2])

# Loop hex to int into new list 
for element in aList:
	aListInt.append(int(element,16))


im = Image.new("RGB",(255,255),(255,255,255))

draw = ImageDraw.Draw(im)

draw.polygon(xy=aListInt,outline=(0,0,0))

im.save("output.png")

