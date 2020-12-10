import datetime
import paho.mqtt.client as mqtt
import random
import time
def get_line_protocol(sensor, reading, value):
        line = "{} {}={}"
        timestamp = str(int(datetime.datetime.now().timestamp() * 1000))
        return line.format(sensor, reading, value)

#Client(client_id="pi", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
#val=get_line_protocol("s1", "value", random.random())
#print(get_line_protocol("s1", "value", 23))
#print(val)
client =mqtt.Client(client_id="pi", clean_session=True, userdata=None, transport="tcp")
client.connect("192.168.1.106", port=1883, keepalive=60, bind_address="")

while(1):
 val=get_line_protocol("s1", "value", random.randint(0,20))
 print(val)
