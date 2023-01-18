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
counterVar = 1
animationSteps = 1

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

bg = Image.new("RGB",(int(256*scaleSize),int(256*scaleSize)),(0,0,13))
images.append(bg)
im = Image.new("RGBA",(int(256*scaleSize),int(256*scaleSize)),(0,0,13,255))
print(len(aListInt))

countVar = 1
for i in range(0,len(aList)):
    draw = ImageDraw.Draw(im)
    draw.text((10,10),str(aList[i]))

    if (countVar%animationSteps < 1):
        images.append(im)
        im = Image.new("RGBA",(int(256*scaleSize),int(256*scaleSize)),(0,0,13,255))
        print(countVar)

    countVar = countVar + 1

images[0].save('animated.gif', save_all=True, append_images=images[1:], optimize=False, duration=.001, loop=0)
