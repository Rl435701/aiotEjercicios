from machine import Pin, PWM, SoftI2C
from time import sleep
import ssd1306

redpin = Pin(4)
bluepin = Pin(18)
greenpin = Pin(5)

red = PWM(redpin)
blue = PWM(bluepin)
green = PWM(greenpin)

red.freq(500)
blue.freq(500)
green.freq(500)

i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    for val in range(256):
        red.duty_u16(int(val * 65535 // 255))
        blue.duty_u16(int(max(0, min(65535, 65535 - val * 256))))
        green.duty_u16(int(max(0, min(65535, 65535 - (val - 128) * 512))))

        display.fill(0)
        display.text("R: {}".format(val), 0, 0, 1)
        display.text("G: {}".format(max(0, min(255, int(255 - (val - 128) * 2)))), 0, 16, 1)
        display.text("B: {}".format(max(0, min(255, int(val * 2)))), 0, 32, 1)
        display.show()

        sleep(0.001)

    for val in range(255, 0, -1):
        red.duty_u16(int(val * 65535 // 255))
        blue.duty_u16(int(max(0, min(65535, 65535 - val * 512))))
        green.duty_u16(int(max(0, min(65535, 65535 - (val - 128) * 256))))

        display.fill(0)
        display.text("R: {}".format(val), 0, 0, 1)
        display.text("G: {}".format(max(0, min(255, int(255 - (val - 128) * 2)))), 0, 16, 1)
        display.text("B: {}".format(max(0, min(255, int(val * 2)))), 0, 32, 1)
        display.show()

        sleep(0.001)
