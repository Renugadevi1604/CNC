import paho.mqtt.client as mqtt
import json
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB connection
TOKEN = "RMnkSi94zEvmnP1xFEBImgCqnmi2R2nWSU7NA1PkYNYEQ-vsOCDkHR_8LHJQRjN32hLjJ4S4CgqlR4NK8mWc-g=="
ORG = "cnc_org"
BUCKET = "cnc_data"
URL = "http://localhost:8086"

client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

def on_connect(client_mqtt, userdata, flags, rc, properties=None):
    print("Connected to MQTT!")
    client_mqtt.subscribe("cnc/vibration")

def on_message(client_mqtt, userdata, msg):
    data = json.loads(msg.payload.decode())
    point = Point("vibration")\
        .field("x", data['x'])\
        .field("y", data['y'])\
        .field("z", data['z'])
    write_api.write(bucket=BUCKET, org=ORG, record=point)
    print(f"Written to InfluxDB: {data}")

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("test.mosquitto.org", 1883, 60)
mqtt_client.loop_forever()