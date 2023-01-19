import sys
from PIL import Image, ImageDraw

### Take in String and split by char len

## Defaults
#scaleSize = 1
# arg for scale
if (len(sys.argv) > 1 ):
    scaleSize = float(sys.argv[1])
else:
    scaleSize = 1

# Variables
images = []
animationSteps = 10

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

bg = Image.new("RGB",(int(256*scaleSize),int(256*scaleSize)),(0,0,0))
images.append(bg)
im = Image.new("RGBA",(int(256*scaleSize),int(256*scaleSize)),(0,0,13,0))
print(len(aListInt))

countVar = 1
for i in range(0,len(aListInt)-2,5):
    draw = ImageDraw.Draw(im)
    draw.line(xy=(round(aListInt[i]*scaleSize,0),round(aListInt[i+1]*scaleSize,0),round(aListInt[i+5]*scaleSize,0),round(aListInt[i+6]*scaleSize,0)),fill=(aListInt[i+2],aListInt[i+3],aListInt[i+4],255))

    if (countVar%animationSteps < 1):
        images.append(im)
        im = Image.new("RGBA",(int(256*scaleSize),int(256*scaleSize)),(0,0,13,0))
        print(countVar)

    countVar = countVar + 1

images[0].save('animated.gif', save_all=True, append_images=images[1:], optimize=False, duration=.001, loop=0)
