import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected!")
    client.subscribe("cnc/vibration")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"Received: {data}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()