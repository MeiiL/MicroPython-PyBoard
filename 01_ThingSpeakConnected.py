## test on the uploading process of ThingSpeak ##
##              with Wifi connected            ##

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




host='http://api.thingspeak.com'       
api_key='--ThingSpeakAPIKey--'   

while True:
    url='%s/update?api_key=%s&field1=123 ' %(host, api_key)   # fixed number for testing
    print('heartbeat=', '123', '%')
    r=urequests.get(url)   
    print('response=', r.text)
    time.sleep(16)   