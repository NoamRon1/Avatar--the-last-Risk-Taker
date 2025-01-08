"""
Avatar the last Risk taker
By Noam Ron

In the project:
x4 - 20 Leds NeoPixel
x2 - 20x4 LCD I2C screens
x4 - Normal Push Buttons 
"""

from time import sleep, time
import machine
from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
import neopixel
import random


class Avatar:

    def __init__(self, s1_adr: int, s2_adr: int, s1_s: tuple, s2_s: tuple, b_p: int, n_p1_p=14, n_p2_p=15, n_p3_p=16,
                 n_p4_p=17):
        # p1_p = neopixel player 1 pin
        # p2_p = neopixel player 2 pin
        # p3_p = neopixel player 3 pin
        # p4_p = neopixel player 4 pin
        # s1_adr = lcd screen 1 address
        # s2_adr = lcd screen 2 address
        # s1_s = lcd screen 1 size
        # s2_s = lcd screen 2 size
        # b_p = button pin

        self.current_player = 1  # Player Turn changes by buttons.

        self.game_state = True  # checks if the game is currently on.

        # NeoPixel Pins:
        self.neopixel_player1_pin = n_p1_p
        self.neopixel_player2_pin = n_p2_p
        self.neopixel_player3_pin = n_p3_p
        self.neopixel_player4_pin = n_p4_p

        # Neopixel objects. will be assigned in NeoPixelSetup.
        self.neopixel_1 = None
        self.neopixel_2 = None
        self.neopixel_3 = None
        self.neopixel_4 = None

        self.neopixel_led_count = 12  # Number of leds on the neopixel module.

        # LCD addresses and sizes:
        self.screen1_address = s1_adr
        self.screen2_address = s2_adr

        self.screen1_size = s1_s
        self.screen2_size = s2_s

        self.lcd1 = None
        self.lcd2 = None

        self.button_pin = b_p  # Button pin.

        self.button = None  # Button object. will be assigned in ButtonsSetup.

        # Dictionary setup
        self.player_dict = {self.neopixel_1: "Player 1", self.neopixel_2: "Player 2", self.neopixel_3: "Player 3",
                            self.neopixel_4: "Player 4"}  # Used for lcdPrint function.

    def neo_pixel_setup(self):
        # Initialize the neopixel objects.
        np1 = neopixel.NeoPixel(machine.Pin(self.neopixel_player1_pin), self.neopixel_led_count)
        np2 = neopixel.NeoPixel(machine.Pin(self.neopixel_player2_pin), self.neopixel_led_count)
        np3 = neopixel.NeoPixel(machine.Pin(self.neopixel_player3_pin), self.neopixel_led_count)
        np4 = neopixel.NeoPixel(machine.Pin(self.neopixel_player4_pin), self.neopixel_led_count)

        self.neopixel_1, self.neopixel_2, self.neopixel_3, self.neopixel_4 = np1, np2, np3, np4

        print("NeoPixel Setup completed")
        self.player_dict = {self.neopixel_1: "Player 1", self.neopixel_2: "Player 2", self.neopixel_3: "Player 3",
                            self.neopixel_4: "Player 4"}  # Reload the dictionary with the new objects.
        print("Dictionary setup finally complete")

    def lcd_setup(self):
        i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=400000)

        # Initialize the lcd objects.
        self.lcd1 = I2cLcd(i2c, self.screen1_address, *self.screen1_size)
        self.lcd2 = I2cLcd(i2c, self.screen1_address, *self.screen2_size)

        self.lcd1.putstr("LCD Setup completed")
        self.lcd2.putstr("LCD Setup completed")
        print("LCD Setup completed")

        sleep(1)
        self.lcd1.clear()
        self.lcd2.clear()

    def buttons_setup(self):
        self.button = Pin(self.button_pin, Pin.IN, Pin.PULL_DOWN)
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.ButtonChange)

    # Turn the neopixels to red except the current player.
    def neo_pixel_red(self):
        for neopixel_i in [self.neopixel_1, self.neopixel_2, self.neopixel_3, self.neopixel_4].pop(
                self.current_player - 1):
            neopixel_i.fill((255, 0, 0))
            neopixel_i.write()

    def neo_pixel_on(self):
        for i in range(self.neopixel_led_count):
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            P1[i] = (a, b, c)
            P1.write()

    def ButtonChange(self, pin):

        B1_value = self.button.value()
        if self.button_state == B1_value:
            return
        # if not self.button_counter:
        # self.button_counter = True
        # return
        self.button_counter = False
        print("Next Player")
        if self.current_player == 4:
            self.current_player = 1
        else:
            self.current_player += 1
        print(self.current_player)
        sleep(.3)
        self.button_state = B1_value

    def lcdPrint(self, P1, message):
        if not message:
            print("hi")
            self.lcd1.clear()
            self.lcd1.putstr(self.player_dict.get(P1))
            print(self.player_dict.get(P1))
            self.lcd1.move_to(0, 1)
            self.lcd1.putstr("Turn")

        # self.lcd2.clear()
        #  self.lcd2.putstr(self._PD.get(P1))
        # self.lcd2.move_to(0, 1)
        # self.lcd2.putstr("Turn")
        else:
            self.lcd1.clear()
            self.lcd1.putstr(message)

        # self.lcd2.clear()
        # self.lcd2.putstr(message)

    def begin(self):
        self.neo_pixel_setup()
        self.lcd_setup()
        self.buttons_setup()

        print("Begin Func Successfully Completed.")
        self.lcdPrint(None, "Begin Completed")

    def run(self):
        while self.game_state:
            sleep(0.2)
            print(self.button.value())
            if self.current_player == 1:
                print("yes")
                self.neo_pixel_on(self.neopixel_1, self._P12N)
                self.neo_pixel_red(self.neopixel_2, self.neopixel_3, self.neopixel_4)
                self.lcdPrint(self.neopixel_1, None)

            elif self.current_player == 2:
                self.neo_pixel_on(self.neopixel_2, self._P12N)
                self.neo_pixel_red(self.neopixel_1, self.neopixel_3, self.neopixel_4)
                self.lcdPrint(self.neopixel_2, None)

            elif self.current_player == 3:
                self.neo_pixel_on(self.neopixel_3, self.neopixel_led_count)
                self.neo_pixel_red(self.neopixel_1, self.neopixel_2, self.neopixel_4)
                self.lcdPrint(self.neopixel_3, None)

            elif self.current_player == 4:
                self.neo_pixel_on(self.neopixel_4, self.neopixel_led_count)
                self.neo_pixel_red(self.neopixel_1, self.neopixel_2, self.neopixel_3)
                self.lcdPrint(self.neopixel_4, None)

            else:
                print(self.current_player)
                print("break LLL")
                break
