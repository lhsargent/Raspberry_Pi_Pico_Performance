import machine
import utime
scope = machine.Pin(0, machine.Pin.OUT)
while True:
 scope.value(1)
 scope.value(0)
 utime.sleep(1)
#9.00us