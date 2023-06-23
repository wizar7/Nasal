# Set up of the sensor
from bme68x import BME68X
import bme68xConstants as cnst
import bsecConstants as bsec
import datetime
from time import sleep

import numpy as np
import matplotlib.pyplot as plt

import RPi.GPIO as GPIO 

import threading
import tkinter as tk
from threading import Thread
from queue import Queue

import pygame 
import random


#shared varaibles among different functions
air=0
rose=0
lily=0
margaret=0
flower_name=''

temperature=0.0
pressure=0.0
humidity =0.0
gas=0.0

previous_value1=0
previous_value2=0
previous_value3=0
previous_value4=0

button_Status=''


# Callback function when button pressed!
def button_callback(channel):
    print("Button pressed!")
    # add your code here
    
    
# Setup the sensor     
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

# Definition of the variables
def read_conf(path: str):
    with open(path, 'rb') as conf_file:
        conf = [int.from_bytes(bytes([b]), 'little') for b in conf_file.read()]
        conf = conf[4:]
    return conf
    

#This is for the evaluate the most possible smell detected.
def Flower():
    global rose, lily, margaret, air
    highest= max(rose, lily, margaret, air)
    if highest==lily:
        name = 'Lily'
    elif highest==margaret:
        name = 'Margaret'
    elif highest==air:
        name = 'Air'
    else:name='Rose'
    return name
        
#This is showing everthing in GUI
def display_data(queue):
    global flower_name
    def update_label():
        # 更新标签的函数
        if not queue.empty():
            data = queue.get()
            text1.delete("1.0",tk.END)
            text1.insert(tk.END,"Temperature is : {} degC".format(data['temp']))
            text2.delete("1.0",tk.END)
            text2.insert(tk.END,"Air pressure is : {} hPa".format(data['pressure']))
            text3.delete("1.0",tk.END)
            text3.insert(tk.END,"Humidity is : {} %".format(data['humidity']))
            text4.delete("1.0",tk.END)
            text4.insert(tk.END,"Gas resistance is : {} kOhm".format(data['gas']))
        
        window.after(10, update_label)

    # 创建GUI窗口
    window = tk.Tk()
    #window.title("Real-time Data Display")
    window.title("Smell detected:    "+flower_name)

    # Extablish text controler and text content
    text1 = tk.Text(window, height=1, width=40)
    text2 = tk.Text(window, height=1, width=40)
    text3 = tk.Text(window, height=1, width=40)
    text4 = tk.Text(window, height=1, width=40)
    
    #Set up controler and content 
    text1.insert(tk.END,"text1")
    text2.insert(tk.END,"text1")
    text3.insert(tk.END,"text1")
    text4.insert(tk.END,"text1")
    
    #Display controler and content 
    text1.pack()
    text2.pack()
    text3.pack()
    text4.pack()

    # 更新标签
    update_label()
    

    # 运行GUI主循环
    window.mainloop()
    
    
def is_increasing(var1,var2,var3,var4):
        global previous_value1,previous_value2,previous_value3,previous_value4
        count=0
        
        if var1>previous_value1:
            count+=1
        elif var1<previous_value1:
            count-=1

        if var2>previous_value2:
            count+=1
        elif var2<previous_value2:
            count-=1
            
        if var3>previous_value3:
            count+=1
        elif var3<previous_value3:
            count-=1
            
        if var4>previous_value4:
            count+=1
        elif var4<previous_value4:
            count-=1
            
        previous_value1=var1
        previous_value2=var2
        previous_value3=var3
        previous_value4=var4
        return count
        
# Playing the music
def play_music(queue):
        global flower_name, temperature, pressure, humidity, gas
        # Initialize pygame
        pygame.init()
        pygame.mixer.init()

        # Define the number of channels to use
        num_channels = 4

        # Reserve the specified number of channels
        pygame.mixer.set_num_channels(num_channels)

        while True:
                if not queue.empty():
                    data = queue.get()
                    print(data)
                    count=is_increasing(float(data['humidity']),float(data['pressure']),float(data['temp']),float(data['gas']))
                    if(count>12 or count<0):
                        count=6

                    if flower_name == 'Lily':
                        list1 = ['G#1','E2' ,'G#2' ,'B2', 'G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4' ] # temperature for LILY
                        list2 = [ 'E1','G#2', 'E2','G#2', 'E2','G#3', 'E3', 'G#3', 'E3','G#4', 'E4', 'G#4', 'E4'] # pressure for LILY
                        list3 = [ 'C#1','B2', 'C#2','B2', 'C#2', 'E3', 'C#3','B3', 'C#3','B4', 'C#4', 'E4', 'C#4'] # humidity for LILY
                        list4 = [ 'B1', 'C#2','E2', 'F#2', 'G#2', 'B3', 'C#3','E3', 'F#3', 'G#4', 'B4', 'C#4','E4']  # E pentatonic scale for LILY
                    elif flower_name == 'Margaret':
                        list1 = ['C3','A2','C3','A2','E3','C4','A3','G3','C3','D3','E3','C3','G2' ] # temperature for Margaret
                        list2 = ['E3','D3','G2','D2','A3','G3','E3','D3','E2','A2','D2','G2','C2'] # pressure for Margaret
                        list3 = ['G3','A3','E2','C3','G2','D3','C3','G2','G3','C4','G2','E2','C3'] # humidity for Margaret
                        list4 = ['A1','C2','D2', 'E2', 'G2', 'A2', 'C3', 'D3', 'E3', 'G3', 'A3','C4','D4']  # C pentatonic scale for Margaretprevious_value1=0
                    elif flower_name == 'Rose':
                        list1 = ['Ab2','Bb2' ,'Bb3' ,'Ab3', 'Eb3','C2' ,'Eb2' ,'C3', 'Eb3','C3' ,'Eb2' ,'C2', 'F3' ] # temperature for ROSE
                        list2 = ['F2', 'Eb3', 'F3', 'Eb3', 'C3', 'Ab2', 'Bb2', 'F2', 'Bb2', 'F3', 'C3', 'Ab2', 'F2'] # pressure for ROSE
                        list3 = [ 'C3','F2','C3','F3','Bb2','C3','C2','Ab2','F2','Ab2','Bb2','Eb2','Ab3'] # humidity for ROSE
                        list4 = ['F1','Ab2', 'Bb2', 'C2',  'Eb2', 'F2', 'Ab3', 'Bb3', 'C3', 'Eb3', 'F3', 'Ab4','Bb4']  # Ab pentatonic scale for ROSE
                    elif flower_name=='Air':
                        list1 = ['C1','C1' ,'C1' ,'C1', 'C2','C2' ,'C2' ,'C2', 'C3','C3' ,'C3' ,'C4', 'C4' ] # temperature for Air
                        list2 = ['C1','C1' ,'C1' ,'C1', 'C2','C2' ,'C2' ,'C2', 'C3','C3' ,'C3' ,'C4', 'C4' ] # temperature for Air
                        list3 = ['C1','C1' ,'C1' ,'C1', 'C2','C2' ,'C2' ,'C2', 'C3','C3' ,'C3' ,'C4', 'C4' ] # temperature for Air
                        list4 = ['C1','C1' ,'C1' ,'C1', 'C2','C2' ,'C2' ,'C2', 'C3','C3' ,'C3' ,'C4', 'C4' ] # temperature for Air
                        

                    note4 = list4[count]+ "-quarter.wav"  # for gas
                    note1 = list1[count]+ "-half.wav"
                    note2 = list2[count]+ "-half.wav"
                    note3 = list3[count]+ "-half.wav"

                    # Define a list of music files to play on different channels
                    music_files = [note1,note2,note3,note4]
                    print(music_files)
                    # Loop through the music files

                    channel = pygame.mixer.Channel(0)  # Get the channel corresponding to the index
                    # Load and play the music file on the channel
                    sound = pygame.mixer.Sound(music_files[0])
                    channel.play(sound)

                    channel = pygame.mixer.Channel(1)  # Get the channel corresponding to the index
                    # Load and play the music file on the channel
                    sound = pygame.mixer.Sound(music_files[1])
                    channel.play(sound)

                    channel = pygame.mixer.Channel(2)  # Get the channel corresponding to the index
                    # Load and play the music file on the channel
                    sound = pygame.mixer.Sound(music_files[2])
                    channel.play(sound)

                    channel = pygame.mixer.Channel(3)  # Get the channel corresponding to the index
                    # Load and play the music file on the channel
                    sound = pygame.mixer.Sound(music_files[3])
                    channel.play(sound)

                    # Delay before starting the next iteration
                    pygame.time.wait(500)  # Adjust the delay time as needed

                    # Stop all channels to prepare for the next iteration
                    pygame.mixer.stop()

                    # Quit pygame
                    #pygame.quit()
# Use AI model to predict the smell detected. It would be air or one of flowers.
# And returns the percent
def flowerDetecting():
    global air,rose,lily,margaret,flower_name
    s = BME68X(cnst.BME68X_I2C_ADDR_HIGH, 0)
    s.set_sample_rate(bsec.BSEC_SAMPLE_RATE_LP)
    air_coffee = read_conf('/home/nasalimplant/Desktop/python_nasal/AIstudiio/2023_04_22_23_26_unnamed_HP-354_RDC-5-10.config')
    # print(air_coffee)
    print(f'SET BSEC CONF {s.set_bsec_conf(air_coffee)}')
    print(f'SUBSCRIBE GAS ESTIMATES {s.subscribe_gas_estimates(4)}')
    print(f'INIT BME68X {s.init_bme68x()}')
    print('\n\nSTARTING MEASUREMENT\n')
    while (True):
            # Flower Recognise
            try:
                data = s.get_digital_nose_data()
                #print(data)
            except Exception as e:
                print(e)
            if data:
                entry = data[-1]
                ct = datetime.datetime.now()
                air= "{:.1%}".format(entry["gas_estimate_1"])
                rose = " {:.1%}".format(entry["gas_estimate_2"])
                lily = " {:.1%}".format(entry["gas_estimate_3"])
                margaret = "{:.1%}".format(entry["gas_estimate_4"])
                print(f'Air {air}\nROSE {rose}\nLILY {lily}\nMARGARET {margaret}')
                break
    return Flower()

# Use BME sensor to measure the parameters of environment
# Attention: It needs reflush the setup of sensor, so obsorb the process of flower detecting.
def dataMeasurement(queue):
    global temperature, pressure, humidity, gas
    #Parameters detection
    s = BME68X(cnst.BME68X_I2C_ADDR_HIGH, 0)
    s.set_sample_rate(bsec.BSEC_SAMPLE_RATE_LP)
    while(True):
        bsec_data = get_data(s)
        #print(bsec_data)
        while bsec_data == None:
            bsec_data = get_data(s)
        ct = datetime.datetime.now()
        #print(f'temperature={bsec_data["temperature"]}' + ' '  + f'pressure={bsec_data["raw_pressure"]}'+ ' '  + f'humidity={bsec_data["humidity"]}'+ ' '  + f'gas={bsec_data["raw_gas"]}',' '  + f'time={ct}')
        temperature = "{:.01f}".format(bsec_data["raw_temperature"])
        pressure= " {:.1f}".format(bsec_data["raw_pressure"])
        humidity = " {:.01f}".format(bsec_data["humidity"])
        gas = "{:.1f}".format(bsec_data["raw_gas"])
        print(f'Temperature {temperature}degC\nAir Pressure {pressure}hPa\nHumidity {humidity}%\nGas {gas}kOhm\nDATETIME {ct}\n\n')
        data= {'temp':temperature,'pressure':pressure,'humidity':humidity,'gas':gas,}
        queue.put(data)
    
# Calling the test algorithm
def main():
    global flower_name
    flower_name=flowerDetecting()
    
    # 创建并启动线程
    queue = Queue()

    # 创建读取数据的线程
    read_thread1 = Thread(target=dataMeasurement, args=(queue,))
    read_thread1.start()
    
    
    
    # 创建显示数据的GUI程序
    display_data(queue)
    play_music(queue)

    # 等待读取数据的线程结束
    read_thread.join()



            

            
if __name__ == '__main__':
    
    main()
