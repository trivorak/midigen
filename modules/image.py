from PIL import Image
from . import normal

# TO-DO Use this file pull in image and parse out the color
# Try to use PIL/Pillow to do all the image conversion

im = Image.open('output.png');
width, height = im.size;

print("Height = " + str(height));
print("Width = " + str(width))

# Get Color Function
def getColor(w,h):
    return im.getpixel((w,h))

