from PIL import Image, ImageDraw

im = Image.new("RGB",(100,100),(255,255,255))

draw = ImageDraw.Draw(im)

draw.polygon(xy=(1,50,25,50,10,14,8,30,5,60),outline=(0,0,0))

im.save("output.png")

