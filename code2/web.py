    from time import sleep
    from machine import Pin
    import _thread

    import network
    import time
    from umqtt.simple import MQTTClient

    # Wi-Fi and Adafruit IO Credentials
    # AIO_CONTROL_FEED = f"{AIO_USERNAME}/feeds/diorama"
    # diorama_run = "0"  # Default state (off)
    client = None
    # neobreak = False


    # Connect to Wi-Fi
    def connect_wifi():
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        print("Connecting to Wi-Fi...", end="")
        while not wlan.isconnected():
            time.sleep(0.5)
            print(".", end="")

        print("\nConnected! IP:", wlan.ifconfig()[0])


    # Connect to Adafruit IO
    def connect_adafruit():
        global client
        client = MQTTClient(AIO_USERNAME, AIO_SERVER, user=AIO_USERNAME, password=AIO_KEY)
        client.set_callback(subscribe_callback)
        client.connect()
        client.subscribe(AIO_FEED.encode())
        print("Connected to Adafruit IO")


    # Callback function to handle incoming feed data
    def subscribe_callback(topic, msg):
        diorama_run = msg.decode("utf-8")  # Convert byte response to string

        # if diorama_run == "1":
        #     neobreak = False  # Enable LEDs
        # else:
        #     neobreak = True  # Disable LEDs

        print(f"Feed updated: {diorama_run}")


    # Function to send speed data
    def send_speed(msg):
        try:
            self.client.publish(AIO_SPEED_FEED, str(msg))  # Convert speed to string
            print(f"Sent speed to Adafruit IO: {msg}")
        except Exception as e:
            print("Failed to send speed:", e)


    # Create a Diorama instance with motors configuration
    # diorama = Diorama(
    #     button1_pin=25,
    #     button2_pin=26,
    #     speedup_pin=33,
    #     speeddown_pin=32,
    #     neo_pin=5,
    #     num_pix=62,
    #     encoder1_pin=12,
    #     encoder2_pin=14,
    #     in1b_pin=16,  # base
    #     in2b_pin=17,
    #     in1d_pin=0,  # disk
    #     in2d_pin=4,
    #     wheel_size=65
    # )


    # LED control task (Core 0)
    # def neotask():
    #     global neobreak
    #     while True:
    #         if neobreak:
    #             diorama.rainbow()  # LED active state
    #         else:
    #             diorama.heartbeat()  # Standby mode
    #         time.sleep(0.5)  # Reduce CPU load


    # Motor control and button handling (Core 1)
    def main_task():
        connect_wifi()
        connect_adafruit()
        while True:
            client.check_msg()
            sleep(0.1)
            # if diorama_run == "1" or diorama.get_button1_state():
            #     speed = diorama.run()  # Set motor speed
            #     neobreak = True
            #     diorama.motgo(speed)
            # else:
            #     speed = 0  # Stop motor
            #     neobreak = False
            #     diorama.motgo(0)

            # Send speed to Adafruit IO
            # try:
            #     client.publish(AIO_SPEED_FEED, str(speed))
            #     print(f"Sent speed to Adafruit: {speed}")
            # except Exception as e:
            #     print("MQTT publish failed:", e)

            time.sleep(5)


    # Start the LED task on Core 0
    # _thread.start_new_thread(neotask, ())

    # Run motor control on Core 1
    main_task()
