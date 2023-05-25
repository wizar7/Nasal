# Set up of the sensor
from bme68x import BME68X
import bme68xConstants as cnst
import bsecConstants as bsec
import json
import datetime


            


# Definition of the variables
def read_conf(path: str):
    with open(path, 'rb') as conf_file:
        conf = [int.from_bytes(bytes([b]), 'little') for b in conf_file.read()]
        conf = conf[4:]
    return conf


# Calling the test algorithm
def main():
    s = BME68X(cnst.BME68X_I2C_ADDR_HIGH, 0)
    s.set_sample_rate(bsec.BSEC_SAMPLE_RATE_LP)
    print(bsec.BSEC_SAMPLE_RATE_LP)

    air_coffee = read_conf('/home/nasalimplant/Desktop/python_nasal/AIstudiio/2023_04_22_23_26_unnamed_HP-354_RDC-5-10.config')
    print(f'SET BSEC CONF {s.set_bsec_conf(air_coffee)}')
    print(f'SUBSCRIBE GAS ESTIMATES {s.subscribe_gas_estimates(4)}')
    print(f'INIT BME68X {s.init_bme68x()}')
    print('\n\nSTARTING MEASUREMENT\n')

    # Data measurement
    while (True):
        try:
            data = s.get_digital_nose_data()
        except Exception as e:
            print(e)
            main()
        if data:
            entry = data[-1]
            ct = datetime.datetime.now()
            print()
            Air = "{:.1%}".format(entry["gas_estimate_1"])
            Rose = " {:.1%}".format(entry["gas_estimate_2"])
            Lily = " {:.1%}".format(entry["gas_estimate_3"])
            Margaret = "{:.1%}".format(entry["gas_estimate_4"])
            print(f'Air {Air}\nROSE {Rose}\nLILY {Lily}\nMARGARET {Margaret}\nDATETIME {ct}')
            d = {
                'AIR':  Air ,
                'ROSE': Rose,
                'LILY': Lily,
                'Margaret': Margaret,
            }
            #with open('/home/nasalimplant/Desktop/Data/data.json', 'W') as file:
                #json.dump(d, file)


if __name__ == '__main__':
    main()
