from machine import Pin, PWM, ADC import time
- Pin setup
led = PWM(Pin(15))
# LED connected to GP15
button = Pin(14, Pin.IN, Pin.PULL_UP) # Button on GP14 (active LOW)
buzzer = PWM(Pin(13))
# Buzzer on GP13
pot = ADC(26)
# Potentiometer on GP26 (ADCO)
led. freq (1000)
mode = "blink"
def beep():
buzzer.freq (1000)
buzzer.duty_u16(30000)
time.sleep(0.2)
buzzer.duty_u16(0)
while True:
pot_val = pot. read_u16()
led_brightness = pot_val
# Read potentiometer (0-65535)
# Use directly for LED brightness
led.duty_u16(led_brightness)
# —- Button logic
if button.value() = 0:
press
_time = time.ticks_ms()
while button.value() =
0:
time.sleep(0.01)
hold = time.ticks_diff(time.ticks_ms(), press_time)
if hold > 800:
beep ()
else:
mode = "steady" if mode = "blink" else "blink"
print ("Mode switched to:", mode)
if mode = "blink":
led.duty_u16(led_brightness)
time.sleep (0.3) led.duty_u16(0) time.sleep(0.3)
else:
led.duty_u16(led_brightness)
time.sleep (0.05)
