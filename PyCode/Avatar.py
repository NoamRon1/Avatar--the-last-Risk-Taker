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
    
    def __init__(self, P1P, P2P, P3P, P4P, S1Adr, S2Adr, S1S, S2S, BP):

        self._PTurn = 1 #Player Turn changes by buttons.

        self._game = True #checks if the game is currently on.
        #NeoPixel Pins:
        self._P1P = P1P
        self._P2P = P2P
        self._P3P = P3P
        self._P4P = P4P

        self._NP1 = None
        self._NP2 = None
        self._NP3 = None
        self._NP4 = None


        self._P12N = 20
        self._P34N = 16

        #LCD addresses and scales:
        self._S1Adr = S1Adr
        self._S2Adr = S2Adr

        self._S1S = S1S
        self._S2S = S2S

        self._lcd_1 = None
        # self._lcd_2 = None

        #buttons pins:
        self._BP = BP

        self._B1 = None

        #Dictionary setup
        self._PD = {self._NP1: "Player 1", self._NP2: "Player 2", self._NP3: "Player 3", self._NP4: "Player 4"}

        self.button_state = False
        self.button_counter = False

    def NeoPixelSetup(self):
        NP1 = neopixel.NeoPixel(machine.Pin(self._P1P), self._P12N)
        NP2 = neopixel.NeoPixel(machine.Pin(self._P2P), self._P12N)
        NP3 = neopixel.NeoPixel(machine.Pin(self._P3P), self._P34N)
        NP4 = neopixel.NeoPixel(machine.Pin(self._P4P), self._P34N)

        self._NP1, self._NP2, self._NP3, self._NP4 = NP1, NP2, NP3, NP4

        print("NeoPixel Setup completed")
        self._PD = {self._NP1: "Player 1", self._NP2: "Player 2", self._NP3: "Player 3", self._NP4: "Player 4"}
        print("Dictionary setup finally complete")

    def LcdSetup(self):
        i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=400000)

        self._lcd_1 = I2cLcd(i2c, self._S1Adr, self._S1S[0], self._S1S[1])
        # self._lcd_2 = I2cLcd(i2c, self._S2Adr, self._S2S[0], self._S2S[1])

        self._lcd_1.putstr("LCD Setup completed")
        # self._lcd_2.putstr("LCD Setup completed")
        print("LCD Setup completed")

        sleep(1)
        self._lcd_1.clear()
        # self._lcd_2.clear()

    def ButtonsSetup(self):
        self._B1 = Pin(self._BP, Pin.IN, Pin.PULL_DOWN)
        self._B1.irq(trigger=Pin.IRQ_FALLING, handler=self.ButtonChange)

    def NeoPixelNot(self, P1, P2, P3):
        P1.fill((255, 255, 255))
        P2.fill((255, 0, 0))
        P3.fill((255, 0, 0))
        P1.write()
        P2.write()
        P3.write()

    def NeoPixelYes(self, P1, PN):
        for i in range(PN):
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            P1[i] = (a, b, c)
            P1.write()

    def ButtonChange(self, pin):

        B1_value = self._B1.value()
        if self.button_state == B1_value:
            return
        #if not self.button_counter:
            #self.button_counter = True
            #return
        self.button_counter = False
        print("Next Player")
        if self._PTurn == 4:
            self._PTurn = 1
        else:
            self._PTurn += 1
        print(self._PTurn)
        sleep(.3)
        self.button_state = B1_value



    def lcdPrint(self, P1, message):
        if not message:
            print("hi")
            self._lcd_1.clear()
            self._lcd_1.putstr(self._PD.get(P1))
            print(self._PD.get(P1))
            self._lcd_1.move_to(0, 1)
            self._lcd_1.putstr("Turn")

           # self._lcd_2.clear()
          #  self._lcd_2.putstr(self._PD.get(P1))
           # self._lcd_2.move_to(0, 1)
            #self._lcd_2.putstr("Turn")
        else:
            self._lcd_1.clear()
            self._lcd_1.putstr(message)

           # self._lcd_2.clear()
            #self._lcd_2.putstr(message)


    def begin(self):
        self.NeoPixelSetup()
        self.LcdSetup()
        self.ButtonsSetup()

        print("Begin Func Successfully Completed.")
        self.lcdPrint(None, "Begin Completed")

    def run(self):
        while self._game:
            sleep(0.2)
            print(self._B1.value())
            if self._PTurn == 1:
                print("yes")
                self.NeoPixelYes(self._NP1, self._P12N)
                self.NeoPixelNot(self._NP2, self._NP3, self._NP4)
                self.lcdPrint(self._NP1, None)

            elif self._PTurn == 2:
                self.NeoPixelYes(self._NP2, self._P12N)
                self.NeoPixelNot(self._NP1, self._NP3, self._NP4)
                self.lcdPrint(self._NP2, None)

            elif self._PTurn == 3:
                self.NeoPixelYes(self._NP3, self._P34N)
                self.NeoPixelNot(self._NP1, self._NP2, self._NP4)
                self.lcdPrint(self._NP3, None)

            elif self._PTurn == 4:
                self.NeoPixelYes(self._NP4, self._P34N)
                self.NeoPixelNot(self._NP1, self._NP2, self._NP3)
                self.lcdPrint(self._NP4, None)

            else:
                print(self._PTurn)
                print("break LLL")
                break
