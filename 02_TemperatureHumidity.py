## test on the uploading process of ThingSpeak ##
##              with Wifi connected            ##
##   use DHT11 temperature & humidity sensor   ##

from machine import Pin
import dht   
import time
import urequests 

import network
sta = network.WLAN(network.STA_IF)
    
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    sta.connect('--APRouterName--','--WifiPassword--')
    while not sta.isconnected():
        pass
print('network config:', sta.ifconfig())




p2=Pin(2, Pin.IN)
d=dht.DHT11(p2)
host='http://api.thingspeak.com'       
api_key='--ThingSpeakAPIKey--'   

while True:
    d.measure()                 
    t=d.temperature()       
    h=d.humidity()
    url='%s/update?api_key=%s&field1=%s&field2=%s'%(host, api_key,t,h)   
    print('temperature=', t, ' ' ,'humidity=', h, ' ')   
    r=urequests.get(url)   
    print('response=', r.text)
    time.sleep(16)   