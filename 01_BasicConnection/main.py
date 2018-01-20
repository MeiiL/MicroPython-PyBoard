from machine import Pin
import network
import time


p2 = Pin(2,Pin.OUT)
p2.value(0)


wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
wlan.isconnected()      # check if the station is connected to an AP
wlan.connect('--APRouterName--', '--AP-Pin--') # connect to an AP
wlan.config('192.168.199.254')      # get the interface's MAC adddress
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses
print('connect success')
print('network config:', wlan.ifconfig())
if wlan.isconnected():
    for i in range(1,10):
        p2.low()
        time.sleep(2)
        p2.high()
        time.sleep(2)