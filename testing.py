from PIL import Image
import sys
import modules.normal as normal
import modules.scale as scale
import modules.image as img

# Define Blank Array/List
a=[ ]

# Import Image
if (len(sys.argv) > 1 ): 
  im = Image.open(sys.argv[1])
else:
  im = Image.open('output.png')

# Debug print color at pixel 100x100
print(img.getColor(100,100,im))
# Debug Return Array of image color normalized 0 - 1 see modules 
# a = normal.process(img.getImageBWArray(img.convertToMonochrome(im)))
# Debug Print Normal List
# print(a)

