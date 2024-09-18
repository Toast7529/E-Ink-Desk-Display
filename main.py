from config import loadConfig
from display import Display
from epd import EPD
import time
config = loadConfig('config.toml')
epd = EPD()
def main():
    display = Display("base.png")
    startTime = time.time()
    while True:
        if time.time() - startTime >= 43200:    # refresh e ink every 12 hours
            print("refresh")
            epd.clearDisplay()
            startTime = time.time()
        image = display.displayAll(config['apiKeys']['weatherAPI'], config['apiKeys']['cityName'],'test1.png')
        epd.displayImage(image) # send image to display
        
        time.sleep(config['updateIntervals']['globalTick'])
        # time.sleep(10)

if __name__ == "__main__":
    main()