from PIL import Image, ImageDraw, ImageFont
import requests
from datetime import datetime
import random
im = Image.open("base.png").convert('RGBA')
faces = ["Awakening","Bored","Cool","Demotivated","Happy","Intense","Lonely","Sleeping"]
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

def displayWeather(cityName, apiKey):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units=metric")

    if (res.status_code != 200):
        return None
    data = res.json()
    temp = data['main']['temp']

    font = ImageFont.truetype("arial.ttf", 20)
    draw = ImageDraw.Draw(im)
    draw.text((10,120), f"{round(temp,1)}°C", fill=(255,0,0), font=font)

    # Need to design some icons to use instead of theirs, specifically for black and white
    iconID = data["weather"][0]["icon"].replace("n","d")
    iconImage = Image.open(f"Assets/WeatherIcons/{iconID}.png").convert('RGBA')
    im.paste(iconImage, (80,115), iconImage)
    # urllib.request.urlretrieve(f"https://openweathermap.org/img/wn/{iconID}@2x.png","weatherIcon.png") 
    # iconImg = Image.open("weatherIcon.png").resize((15,15))
    # print(f"https://openweathermap.org/img/wn/{iconID}@2x.png")
    # im.paste(iconImg, (85,120))

def displayTime():
    now = datetime.now()
    time = now.strftime("%I:%M%p")
    date = now.strftime("%A, %b %d")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("consola.ttf", 25)
    draw.text((10,20), time, fill=(255,0,0), font=font)

    draw.text((10,45), date, fill=(255,0,0))

def displayFace():
    currentFace = random.choice(faces)
    faceImage = Image.open(f"Assets/Faces/{currentFace}.png").convert('RGBA')
    im.paste(faceImage, (0,75), faceImage)
    print(currentFace)

if __name__ == "__main__":
    displayWeather(1,1)
    displayFace()
    displayTime()
    displayCPU()
    displayMemory()
    im.show()
    im.save("test.png")