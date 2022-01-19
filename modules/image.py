from PIL import Image
from . import normal

# TO-DO Use this file pull in image and parse out the color
# Try to use PIL/Pillow to do all the image conversion


# Get Color Function
def getColor(w,h,image):
    return image.getpixel((w,h))

def getImageSize(image):
    width,height = im.size
    return(width,height)

def getImageBWArray(image):
    a = [ ]
    for y in range(0,image.height):
        for x in range(0,image.width):
            a.append(getColor(x,y,image))
    return a

def convertToMonochrome(image):
    return image.convert(mode='1')