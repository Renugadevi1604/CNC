import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)
client.publish("cnc/test", "Hello from CNC!")
print("Message sent!")
client.disconnect()