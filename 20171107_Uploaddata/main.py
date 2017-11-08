#20171106 working


import time
import urequests 
import network
sta = network.WLAN(network.STA_IF)
    
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    sta.connect('20-6','0952399999')
    while not sta.isconnected():
        pass
print('network config:', sta.ifconfig())




host='http://api.thingspeak.com'       
api_key='76O41MDRQC7GPHFO'   

while True:
    url='%s/update?api_key=%s&field1="123" ' %(host, api_key)   
    print('heartbeat=', '123', '%')
    r=urequests.get(url)   
    print('response=', r.text)
    time.sleep(16)   