# import i2c_lcd
import machine
import neopixel
import time


class Avatar:
    def __init__(self, neopixel_pin_1, neopixel_pin_2, neopixel_pin_3, neopixel_pin_4, neopixel_led_count=12):
        self.neopixel_1 = neopixel.NeoPixel(machine.Pin(neopixel_pin_1), neopixel_led_count)
        self.neopixel_2 = neopixel.NeoPixel(machine.Pin(neopixel_pin_2), neopixel_led_count)
        self.neopixel_3 = neopixel.NeoPixel(machine.Pin(neopixel_pin_3), neopixel_led_count)
        self.neopixel_4 = neopixel.NeoPixel(machine.Pin(neopixel_pin_4), neopixel_led_count)
        self.neopixel_led_count = neopixel_led_count
        self.neopixels = [self.neopixel_1, self.neopixel_2, self.neopixel_3, self.neopixel_4]
        self.green_color_list = [
            (0, 102, 0),
            (3, 115, 6),
            (6, 128, 14),
            (10, 141, 22),
            (13, 154, 29),
            (15, 168, 37),
            (16, 182, 45),
            (17, 196, 52),
            (16, 211, 60),
            (14, 225, 68),
            (9, 240, 77),
            (0, 255, 85)
        ]
        self.led_index = 0

    def run(self):
        while True:
            self.neopixel_turn(1)
            self.led_index += 1
            time.sleep(0.1)

    def neopixel_turn(self, i):
        for j in range(4):
            if j != i:
                self.neopixels[j].fill((255, 0, 0))
            else:
                for led in range(self.neopixel_led_count):
                    self.neopixels[j][led] = self.green_color_list[(self.led_index + led) % self.neopixel_led_count]
            self.neopixels[j].write()
