from PIL import Image, ImageDraw, ImageFont
import psutil
import requests
from datetime import datetime
import random
class Display:
    def __init__(self, imagePath):
        self._imagePath = imagePath
        self._image = Image.open(imagePath).convert('RGBA')
        self._draw = ImageDraw.Draw(self._image)
        self.faces = ["Awakening","Bored","Cool","Demotivated","Happy","Intense","Lonely","Sleeping"]

    def displayMemory(self):
        memory = psutil.virtual_memory()
        currentMemory = memory.used / (1024**3)  # fetch sys info
        maxMemory = memory.total / (1024**3)
        # get memory usage and percentage
        self._draw.text((55,195), f"{int(currentMemory/maxMemory*100)}%  {round(currentMemory,1)}GiB", fill=(0,0,0))
        barWidth = int(currentMemory/maxMemory*110) + 3 # 113 is bar width
        self._draw.line((8,212,barWidth,212), fill=(0,0,0), width=3)

    def displayCPU(self):
        cpuInfo = psutil.cpu_freq()
        print(cpuInfo)
        temp = -1 
        # fetch cpu temperature
        try:
            temp = psutil.sensors_temperatures()['cpu_thermal'][0][1]
        except:
            print("Couldn't retrieve CPU temps")
        currentSpeed = cpuInfo.current    # fetch sys info
        maxSpeed = cpuInfo.max
        # display CPU percentage and temp
        self._draw.text((55,163), f"{int(currentSpeed/maxSpeed*100)}%  {temp}°C ", fill=(0,0,0))

        barWidth = int(currentSpeed/maxSpeed*110) + 3 # 113 is bar width
        self._draw.line((8,180,barWidth,180), fill=(0,0,0), width=3)

    def displayWeather(self, cityName, apiKey):
        res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units=metric")
        if (res.status_code != 200):
            print("OpenWeatherAPI error")
            return
        data = res.json()
        temp = data['main']['temp']

        font = ImageFont.truetype("./Fonts/arial.ttf", 20)
        self._draw.text((10,120), f"{round(float(temp),1)}°C", fill=(0,0,0), font=font)
        iconID = data["weather"][0]["icon"].replace("n","d")
        iconImage = Image.open(f"Assets/WeatherIcons/{iconID}.png").convert('RGBA')
        self._image.paste(iconImage, (80,115), iconImage)


    def displayTime(self):
        now = datetime.now()
        time = now.strftime("%I:%M%p")
        date = now.strftime("%A, %b %d")
        font = ImageFont.truetype("./Fonts/consola.ttf", 25)
        self._draw.text((10,20), time, fill=(0,0,0), font=font)

        self._draw.text((10,45), date, fill=(0,0,0))

    def displayFace(self):
        currentFace = random.choice(self.faces)
        faceImage = Image.open(f"Assets/Faces/{currentFace}.png").convert('RGBA')
        self._image.paste(faceImage, (0,75), faceImage)

    def show(self):
        self._image.show()
    
    def save(self, fileName):
        self._image.save(fileName)
        
    def clear(self):
        self._image = Image.open(self._imagePath).convert('RGBA')
        self._draw = ImageDraw.Draw(self._image)

    def displayAll(self, apiKey, cityName, fileName):
        self.displayWeather(cityName, apiKey)
        self.displayFace()
        self.displayTime()
        self.displayCPU()
        self.displayMemory()
        temp = self._image
        self.save(fileName)
        self.clear()
        return temp

if __name__ == "__main__":
    display = Display("base.png")
    display.displayAll(1,1, "test.png")