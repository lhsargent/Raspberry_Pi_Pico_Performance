import machine
import utime
scope = machine.Pin(0, machine.Pin.OUT)
decrease = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)
while True:
 scope.value(1)
 if decrease.value() == 1:
     scope.value(0)
 utime.sleep(1)
#19.38us
