import smbus2 as smbus
from flask import Flask

app = Flask(__name__)

I2CADDR = 0x08
REGISTER = 0x00
bus = smbus.SMBus(1)
name = "weather"
sensortype  = "resistance"
sensor = "raindrop1"

@app.route('/')
def rawval():
    return (getval())

@app.route('/inline/')
def inlineval():
    return (sensortype + ",sensor=" + sensor + " value=" + getval())

def getval():
    reading = bus.read_byte(I2CADDR)
    return (str(reading))
    


if __name__ == '__main__':
    app.run()






