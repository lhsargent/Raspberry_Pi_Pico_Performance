import machine
import utime
scope = machine.Pin(0, machine.Pin.OUT)
potentiometer = machine.ADC(26)
pot2 = machine.ADC(27)
pot3 = machine.ADC(28)
while True:
 scope.value(1)
 if potentiometer.read_u16() >= 50000 and pot2.read_u16()>= 1 and pot3.read_u16()>= 1:
     scope.value(0)
 utime.sleep(1)
 #51.28us