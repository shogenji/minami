# HCSR04 障害物・停止

from microbit import *
import machine

pin2.read_digital()

while True:
    pin1.write_digital(1)
    sleep(1)
    pin1.write_digital(0)

    t = machine.time_pulse_us(pin2, 1)
    d = int(t * 340 / 20000)
    if d < 10:
        i2c.write(16, bytes([0, 0, 0]))
        i2c.write(16, bytes([2, 0, 0]))
        sleep(100)
    else:
        i2c.write(16, bytes([0, 0, 50]))
        i2c.write(16, bytes([2, 0, 50]))
