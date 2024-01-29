try:
    import gpiozero
    LED_PIN = gpiozero.LED(17)
    blink_time = 0.25

    def blink_led():
        LED_PIN.blink(on_time = blink_time, off_time = blink_time)
except:
    is_rpi = False

    def blink_led():
        print("ERROR IN PROGRAM")
