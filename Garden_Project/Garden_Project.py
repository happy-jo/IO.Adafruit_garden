import sys
import time
import math
# import RPi.GPIO as GPIO
from Adafruit_IO import MQTTClient
import sht31

# IO.Adafruit account info, go to io.adafruit.com to setup your account
ADAFRUIT_IO_KEY      = 'enter your key here'
ADAFRUIT_IO_USERNAME = 'enter your username here'

# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print 'Connected to Adafruit IO!  Listening for DemoFeed changes...'
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe('Temperture')
    client.subscribe('Humidity')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print 'Disconnected from Adafruit IO!'
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print 'Feed {0} received new value: {1}'.format(feed_id, payload)

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Client loop function
client.loop_background()

print 'Publishing a new message every 10 seconds (press Ctrl-C to quit)...'

with sht31.SHT31(1) as sht31:
    while True:
        temperature, humidity = sht31.get_temp_and_humidity()
        print 'publishing {0} to Temperature Feed'.format(round(temperature * 9/5 +32), 1)
        print 'Publishing {0} to Humidity Feed'.format(round(humidity), 1)
        client.publish('Temperature', temperature)
        client.publish('Humidity', humidity)
        time.sleep (10)
