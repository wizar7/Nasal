from bme68x import BME68X
import bme68xConstants as cnst
import bsecConstants as bsec
from time import sleep
import json
import datetime

bme = BME68X(cnst.BME68X_I2C_ADDR_HIGH, 0)       # I2C address of the BME68X sensor (execute <i2cdetect -y 1> in terminal to look up the i2c address, either 0x76 or 0x77)
bme.set_sample_rate(bsec.BSEC_SAMPLE_RATE_LP)    # LP is for interactive displays and has a drain of <1 mA and an update rate of 3 sec

def get_data(sensor):
    data = {}
    try:
        data = sensor.get_bsec_data()
    except Exception as e:
        print(e)
        return None
    if data == None or data == {}:
        sleep(0.1)
        return None
    else:
        sleep(3)
        return data
        
while(True):
    bsec_data = get_data(bme)
    #print(bsec_data)
    while bsec_data == None:
        bsec_data = get_data(bme)
    ct = datetime.datetime.now()
    print(f'temperature={bsec_data["temperature"]}' + ' '  + f'pressure={bsec_data["raw_pressure"]}'+ ' '  + f'humidity={bsec_data["humidity"]}'+ ' '  + f'gas={bsec_data["raw_gas"]}',' '  + f'time={ct}\n')
    
    
    temp = "{:.1%}".format(bsec_data["raw_temperature"])
    pressure = " {:.1%}".format(bsec_data["raw_pressure"])
    humidity = " {:.1%}".format(bsec_data["humidity"])
    gas = "{:.1%}".format(bsec_data["raw_gas"])
    d= {
    'temperature': temp,
    'raw_pressure': pressure,
    'humidity': humidity,
    'gas': gas}
    
    with open('data.json', 'w') as file:json.dump(d,file)
