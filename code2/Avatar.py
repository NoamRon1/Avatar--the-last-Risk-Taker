import i2c_lcd
import machine
import neopixel
import time

import network
import time
from umqtt.simple import MQTTClient

class Avatar:
    def __init__(self, neopixel_pin_1, neopixel_pin_2, neopixel_pin_3, neopixel_pin_4, button_pin, sda_pin, scl_pin,
                 em_stop_pin,
                 lcd_address_1=0x27, lcd_address_2=0x26, lcd_size_1=(2, 16), lcd_size_2=(2, 16), neopixel_led_count=12):
        # neopixel
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

        # button
        self.button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.button.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.on_press)

        # lcd
        i2c = machine.SoftI2C(sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin), freq=400000)
        self.lcd1 = i2c_lcd.I2cLcd(i2c, lcd_address_1, *lcd_size_1)
        # self.lcd2 = i2c_lcd.I2cLcd(i2c, lcd_address_2, *lcd_size_2)
        self.lcd1.putstr("LCD Setup completed")
        # self.lcd2.putstr("LCD Setup completed")
        print("LCD Setup completed")
        time.sleep(1)
        self.lcd1.clear()
        # self.lcd2.clear()

        self.emergency_stop = machine.Pin(em_stop_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
 
        # general game
        self.current_player = 0

        # network
        self.WIFI_SSID = "ENTER NETWORK SSID HERE"
        self.WIFI_PASSWORD = "ENTER NETWORK PASSWORD HERE"
        self.AIO_SERVER = "io.adafruit.com"
        self.AIO_USERNAME = "ENTER USERNAME HERE"
        self.AIO_KEY = "ENTER ACSSES KEY HERE"
        self.AIO_FEED = f"{self.AIO_USERNAME}/feeds/ENTER FEED1 NAME"
        self.AIO_PLAYER_NUM = f"{self.AIO_USERNAME}/feeds/ENTER FEED1 NAME"
        self.AIO_PLAYER_SET = f"{self.AIO_USERNAME}/feeds/ENTER FEED1 NAME"
        self.client = None

    def run(self):
        self.connect_wifi()
        self.connect_adafruit()

        self.write_lcd("  Game Running", f"   Player: #{self.current_player + 1}")

        while self.emergency_stop.value() == 0:
            self.client.check_msg()
            self.neopixel_turn(self.current_player)
            self.led_index += 1
            self.update_lcd(self.current_player + 1)
            time.sleep(0.1)

    def neopixel_turn(self, i):
        for j in range(4):
            if j != i:
                self.neopixels[j].fill((255, 0, 0))
            else:
                for led in range(self.neopixel_led_count):
                    self.neopixels[j][led] = self.green_color_list[(self.led_index + led) % self.neopixel_led_count]
            self.neopixels[j].write()

    def on_press(self, msg):
        self.current_player = (self.current_player + 1) % 4
        self.send_msg(self.current_player + 1)
        print(self.current_player)

    def write_lcd(self, text_line_1, text_line_2):
        self.lcd1.clear()
        # self.lcd2.clear()
        self.lcd1.putstr(text_line_1)
        # self.lcd2.putstr(text_line_1)
        self.lcd1.move_to(0, 1)
        # self.lcd2.move_to(0, 1)
        self.lcd1.putstr(text_line_2)
        # self.lcd2.putstr(text_line_2)
        self.lcd1.move_to(0, 0)
        # self.lcd2.move_to(0, 0)

    def update_lcd(self, player_num):
        self.lcd1.move_to(12, 1)
        self.lcd1.putstr(str(player_num))

        # self.lcd2.move_to(12, 1)
        # self.lcd2.putstr(str(player_num))

    def connect_wifi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.WIFI_SSID, self.WIFI_PASSWORD)

        print("Connecting to Wi-Fi...", end="")
        while not wlan.isconnected():
            time.sleep(0.5)
            print(".", end="")

        print("\nConnected! IP:", wlan.ifconfig()[0])

    def connect_adafruit(self):
        self.client = MQTTClient(self.AIO_USERNAME, self.AIO_SERVER, user=self.AIO_USERNAME, password=self.AIO_KEY)
        self.client.set_callback(self.on_message)
        self.client.connect()
        self.client.subscribe(self.AIO_FEED.encode())
        self.client.subscribe(self.AIO_PLAYER_SET.encode())
        print("Connected to Adafruit IO")

    def send_msg(self, msg):
        try:
            self.client.publish(self.AIO_PLAYER_NUM, str(msg))  # Convert speed to string
            print(f"Sent speed to Adafruit IO: {msg}")
        except Exception as e:
            print("Failed to send speed:", e)

    def on_message(self, topic, msg):
        print(f"Message received on topic {topic}: {msg}")
        if topic == b'Noam_Ron/feeds/Set Player - Avatar the last Risk taker':
            self.current_player = int(msg) - 1
            self.update_lcd(self.current_player)
            self.send_msg(int(msg))
        else:
            if msg == b'1':
                self.on_press(1)


def main():
    game = Avatar(18, 19, 5, 14, 13, 16, 17, 2)
    game.run()


if __name__ == "__main__":
    main()

