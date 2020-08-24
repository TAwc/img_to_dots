#higher scale = larger files/images and better quality
img_scale = 40

from PIL import Image, ImageDraw

# get pixel data
im = Image.open('test.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())

# create new image to draw on
blank = Image.new('P', (width*img_scale, height*img_scale), 255)
draw = ImageDraw.Draw(blank)

# draw a circle
def create_circle(x, y, r): #center coordinates, radius
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(0,0,0,255))

print ("start")
perc = 0
# for every pixel get the index and rgb value
for index, values in enumerate(pixel_values):
    # skip every other line
    if (index%width) % 2 == 0 or int(index/width) % 2 == 0:
        continue

    # calculacte gray value (inverted)
    gray_value = (values[0] * 0.3) + (values[1] * 0.59) + (0.11 * values[2]) # (max(values) + min(values)) / 2 #
    
    # get x and y pos
    y, x = (index/width), (index%width)

    # draw circle at correct positions and add invert gray scale (to non inverted)
    create_circle(x * img_scale, y * img_scale, (1 - gray_value/255) * img_scale)

    #loading ani
    if (int(index/len(pixel_values) * 100) > perc):
        perc = (int(index/len(pixel_values) * 100))
        print(str(perc) + "%")

# show the img
blank.show()

#save the img
blank.save('output.png')