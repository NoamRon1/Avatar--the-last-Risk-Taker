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

class avatar:
    
    def __init__(self, PTurn, P1P, P2P, P3P, P4P, S1Adr, S2Adr, S1S, S2S, B1P, B2P, B3P, B4P):

        self._PTurn = PTurn #Player Turn changes by buttons.
        #NeoPixel Pins:
        self._P1P = P1P
        self._P2P = P2P
        self._P3P = P3P
        self._P4P = P4P

        self._NP1 = 0
        self._NP2 = 0
        self._NP3 = 0
        self._NP4 = 0


        self._P12N = 20
        self._P34N = 16

        #LCD addresses and scales:
        self._S1Adr = S1Adr
        self._S2Adr = S2Adr

        self._S1S = S1S
        self._S2S = S2S

        self._lcd_1 = 0
        self._lcd_2 = 0

        #buttons pins:
        self._B1P = B1P
        self._B2P = B2P
        self._B3P = B3P
        self._B4P = B4P

        self._last_stat = False
        self._stat = False

        #Dictionary setup
        self._PD = {self._P1P: "Player 1", self._P2P: "Player 2", self._P3P: "Player 3", self._P4P: "Player 4"}

    def NeoPixelSetup(self):
        NP1 = neopixel.Neopixel(machine.Pin(self._P1P), self._P12N)
        NP2 = neopixel.Neopixel(machine.Pin(self._P2P), self._P12N)
        NP3 = neopixel.Neopixel(machine.Pin(self._P3P), self._P34N)
        NP4 = neopixel.Neopixel(machine.Pin(self._P4P), self._P34N)

        self._NP1, self._NP2, self._NP3, self._NP4 = NP1, NP2, NP3, NP4

        print("NeoPixel Setup completed")
    
    def LcdSetup(self):
        i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=400000)

        lcd_1 = I2cLcd(i2c, self._S1Adr, self._S1S[0], self._S1S[1])
        lcd_2 = I2cLcd(i2c, self._S2Adr, self._S2S[0], self._S2S[1])

        lcd_1.putstr("LCD Setup completed")
        lcd_2.putstr("LCD Setup completed")
        print("LCD Setup completed")

        sleep(1)
        lcd_1.clear()
        lcd_2.clear()

        self._lcd_1 = lcd_1
        self._lcd_2 = lcd_2

    def NeoPixelNot(self, P1, P2, P3):
        P1.fill((255, 0, 0))
        P2.fill((255, 0, 0))
        P3.fill((255, 0, 0))

    def NeoPixelYes(self, P1, PN):
        for i in range(PN):
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            P1[i] = (a, b, c)
            P1.write()

    def ButtonCheck(self):
        pass

    def lcdPrint(self, P1, message):
        if message == None:
            self._lcd_1.clear()
            self._lcd_1.putstr(self._PD.get(P1))
            self._lcd_1.move_to(0, 1)
            self._lcd_1.putstr("Turn")

            self._lcd_2.clear()
            self._lcd_2.putstr(self._PD.get(P1))
            self._lcd_2.move_to(0, 1)
            self._lcd_2.putstr("Turn")
        else:
            self._lcd_1.clear()
            self._lcd_1.putstr(message)

            self._lcd_2.clear()
            self._lcd_2.putstr(message)


    def begin(self):
        self.NeoPixelSetup()
        self.LcdSetup()
        print("Begin Func Successfully Completed.")
        self.lcdPrint(None, "Begin Completed")

    def run(self):
        pass
