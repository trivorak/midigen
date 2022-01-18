from PIL import Image
import modules.normal as normal
import modules.scale as scale
import modules.image as image

# Define Blank Array/List
a=[ ]

# Debug / Test Functions
# print(scale.generateScaleArray(scale.randomRootNote(),scale.generateRandomScale(),a))
# print(image.getColor(1,2))

im = Image.open('output.png')
print(image.getColor(100,100,im))