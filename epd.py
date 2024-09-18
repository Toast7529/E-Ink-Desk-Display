from waveshare_epd import epd2in13_V4
import time
class EPD:
    def __init__(self):
        self._epd = epd2in13_V4.EPD()
        self._epd.init()
        self._epd.Clear(0xFF)   # clear e-ink with white

    def displayImage(self, image):
        self._epd.init()
        self._epd.display(self._epd.getbuffer(image))
        time.sleep(2)
        self._epd.sleep()

    def clearDisplay(self):
        self._epd.Clear(0xFF)
        time.sleep(2)
        self._epd.sleep()