from PIL import Image
import math
import normal

#Init Variable
colorList = []

#Import Image
im = Image.open('output.png')

#Convert to RGB to
im = im.convert("RGB")

#Get all Colors
for y in range(0,im.height):
	for x in range(0,im.width):
		colorValue = im.getpixel((x,y))
		colorList.append(colorValue)

## Print for Debugging Only
#print(colorList)

#Create a new image
nim = Image.new("RGB",(im.width,im.height),(0,0,0))
pixels = nim.load()
index = 0

#Main Loop
for element in colorList:
	pixels[index%im.width,math.floor(index/im.width)] = (element[2],element[0],element[1])
	index = index + 1

#Output Image
nim.save('nimoutput.png')	
