from PIL import Image, ImageDraw, ImageFont
im = Image.open("base.png")

def displayMemory():
    currentMemory = 3138    # fetch sys info
    maxMemory = 4000
    draw = ImageDraw.Draw(im)
    draw.text((55,195), f"{int(currentMemory/maxMemory*100)}%  {round(currentMemory/1000,1)}GiB", fill=(255,0,0))
    # bar is 105 long, 3 tall
    # draw bar
    barWidth = int(currentMemory/maxMemory*113) + 8 #113 is bar width
    draw.line((8,212,barWidth,212), fill=(255,0,0), width=3)

def displayCPU():
    temp = 42.0
    currentSpeed = 1.2    # fetch sys info
    maxSpeed = 3
    draw = ImageDraw.Draw(im)
    draw.text((55,163), f"{int(currentSpeed/maxSpeed*100)}%  {temp}°C ", fill=(255,0,0))
    # bar is 105 long, 3 tall
    # draw bar
    barWidth = int(currentSpeed/maxSpeed*113) + 8 #113 is bar width
    draw.line((8,180,barWidth,180), fill=(255,0,0), width=3)

if __name__ == "__main__":
    print(im.format)
    displayCPU()
    displayMemory()
    im.show()