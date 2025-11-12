from machine import Pin, ADC, PWM
import time

led = PWM(Pin(15))
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
buzzer = PWM(Pin(16))
pot = ADC(Pin(28))

led.freq(1000)
buzzer.freq(1000)
led_state = False

while True:
    if button.value() == 1:
        led_state = not led_state
        time.sleep(0.3)
    
    if led_state:
        pot_value = pot.read_u16() / 65535
        led.duty_u16(int(pot_value * 65535))
        if pot_value > 0.8:
            buzzer.duty_u16(40000)
        else:
            buzzer.duty_u16(0)
    else:
        led.duty_u16(0)
        buzzer.duty_u16(0)
