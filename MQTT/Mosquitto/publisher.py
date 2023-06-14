import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish("topic/test", "Hello MQTT")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)

client.loop_forever()
