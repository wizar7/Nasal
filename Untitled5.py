#!/usr/bin/env python
# coding: utf-8

# In[29]:


#This code is for generate midi files by notes, which you just write them as symbols
#from music21 import stream, note, chord

def generate_melody(notes):
    melody = stream.Stream()

    for note_name in notes:
        if '.' in note_name:  # Handle chords
            chord_notes = note_name.split('.')
            chord_notes_objects = [note.Note(n) for n in chord_notes]
            chord_note = chord.Chord(chord_notes_object)
            melody.append(chord_note)
        else:  # Single note
            new_note = note.Note(note_name)
            melody.append(new_note)

    return melody

notes7 = ['E3' ,'G#3' ,'B3', 'G#3'] # temperature for LILY
notes8 = ['G#3', 'E3', 'G#3', 'E3'] # pressure for LILY
notes9 = ['B3', 'C#3', 'E3', 'C#3'] # humidity for LILY

notes1 = ['Ab', 'Bb', 'C', 'Eb', 'F', 'Ab'] # Ab pentatonic scale for ROSE
notes2 = ['E', 'F#', 'G#', 'B', 'C#', 'E'] # E pentatonic scale for LILY
notes3 = ['C','D', 'E', 'G', 'A', 'C']    # C pentatonic scale for MARGARET

notes4 = ['C4', 'A3', 'G3', 'C4', 'A3', 'D4', 'E4', 'C3']
notes5 = ['E4', 'C#4', 'B3', 'E4', 'C#4', 'F#3', 'G#3', 'E3']
notes6 = ['Ab4', 'F3', 'Eb3', 'Ab4', 'F3', 'Bb3', 'C4', 'Ab']

melody_stream = generate_melody(notes1)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output1.mid')

melody_stream = generate_melody(notes2)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output2.mid')

melody_stream = generate_melody(notes3)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output3.mid')

melody_stream = generate_melody(notes4)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output4.mid')

melody_stream = generate_melody(notes5)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output5.mid')

melody_stream = generate_melody(notes6)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output6.mid')

melody_stream = generate_melody(notes7)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output7.mid')

melody_stream = generate_melody(notes8)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output8.mid')

melody_stream = generate_melody(notes9)
# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output9.mid')


# In[61]:


#You can use this code to play midi file on single defualt channel.
#import pygame

# Initialize pygame
pygame.init()

# Set up the mixer module
pygame.mixer.init()

# Define a list of MIDI files to play
midi_files = ["output1.mid", "output2.mid", "output3.mid", "output4.mid", "output5.mid", "output6.mid"]
#midi_files= ["output7.mid", "output8.mid", "output9.mid",'output5.mid']

# Loop through the MIDI files
for file in midi_files:
    pygame.mixer.music.load(file)  # Load the MIDI file
    pygame.mixer.music.play(0)  # Play the MIDI file

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pass
# Quit pygame
pygame.quit()


# In[9]:


#Check how many channels on your computer
import pygame

# Initialize pygame
pygame.init()

# Set up the mixer module
pygame.mixer.init()

pygame.mixer.get_num_channels()


# In[4]:


# this code is to play wav music files on different channels once.
import pygame

# Initialize pygame
pygame.init()

# Set up the mixer module
pygame.mixer.init()

# Define the number of channels to use
num_channels = 2

# Reserve the specified number of channels
pygame.mixer.set_num_channels(num_channels)

# Define a list of music files to play on different channels
music_files = ["output7.wav", "output8.wav", "output9.wav",'output5.wav']

# Loop through the music files
for i, file in enumerate(music_files):
    channel = pygame.mixer.Channel(i)  # Get the channel corresponding to the index

    # Load and play the music file on the channel
    sound = pygame.mixer.Sound(file)


    channel.play(sound)

# Wait for the music to finish playing
while any(pygame.mixer.Channel(i).get_busy() for i in range(num_channels)):
    pass

# Quit pygame
pygame.quit()



# In[64]:


import sys
print(sys.version)


# In[3]:


#Make a loop to generate all the midi files that we need(num=104)

from music21 import stream, note, chord

def generate_melody(note_name, duration, number):
    melody = stream.Stream()

    if '.' in note_name:  # Handle chords
        chord_notes = note_name.split('.')
        chord_notes_objects = [note.Note(n, type=duration) for n in chord_notes]
        chord_note = chord.Chord(chord_notes_objects)
        melody.append(chord_note)
    else:  # Single note
        new_note_name = note_name + str(number)
        new_note = note.Note(new_note_name, type=duration)
        melody.append(new_note)

    return melody

notes = ['Ab', 'Bb', 'C', 'Eb', 'F', 'F#', 'G#', 'B', 'C#', 'E', 'D', 'E', 'G', 'A', 'C']  # Example notes
durations = ['half', 'quarter']  # Example durations
numbers = [5]  # Numbers 1 to 4

num_outputs = len(notes) * len(durations) * len(numbers)  # Calculate the number of outputs

for i in range(num_outputs):
    # Calculate the corresponding note, duration, and number for the current output
    note_index = i // (len(durations) * len(numbers))
    duration_index = (i // len(numbers)) % len(durations)
    number = numbers[i % len(numbers)]

    # Extract the note and duration for the current output
    note_name = notes[note_index]
    duration = durations[duration_index]

    # Generate the melody and save it with a name based on the note, duration, and number
    melody_stream = generate_melody(note_name, duration, number)
    output_name = f'{note_name}{number}-{duration}.mid'
    melody_stream.write('midi', fp=output_name)
    print(f"Melody {i+1} ({note_name}{number}, {duration}) generated and saved as {output_name}")

print(f"Total {num_outputs} outputs generated.")


# In[6]:


#This is for the evaluate the most possible smell detected.
def Flower(rose, lily, margaret, air):
    highest = rose
    name = 'Rose'

    if lily > highest:
        highest = lily
        name = 'Lily'

    if margaret > highest:
        highest = margaret
        name = 'Margaret'

    if air > highest:
        highest = air
        name = 'Air'

    #print("The highest value is:", highest)
    return name, highest


rose1 = 10
lily1 = 20
margaret1 = 15
air1 = 30

# Call the Flower function
flower_name, highest_value = Flower(rose1, lily1, margaret1, air1)

# Access the returned values
print("The highest flower is:", flower_name)
print("The highest value is:", highest_value)


# In[10]:


#This is for the evaluate the most possible smell detected.
def Flower(rose, lily, margaret, air):
    highest = rose
    name = 'Rose'

    if lily > highest:
        highest = lily
        name = 'Lily'

    if margaret > highest:
        highest = margaret
        name = 'Margaret'

    if air > highest:
        highest = air
        name = 'Air'

    print("The highest value is:", highest)
    return name, highest


rose1 = 10
lily1 = 20
margaret1 = 15
air1 = 30

# Call the Flower function
flower_name, highest_value = Flower(rose1, lily1, margaret1, air1)


# In[87]:





# In[11]:


import pygame
import random

list1 = ['E' ,'G#' ,'B', 'G#','E' ,'G#' ] # temperature for LILY
list2 = ['G#', 'E', 'G#', 'E','G#', 'E'] # pressure for LILY
list3 = ['B', 'C#', 'E', 'C#','B', 'C#'] # humidity for LILY

list5 = ['Ab', 'Bb', 'C', 'Eb', 'F']  # Ab pentatonic scale for ROSE
list6 = ['E', 'F#', 'G#', 'B', 'C#']  # E pentatonic scale for LILY
list7 = ['C', 'D', 'E', 'G', 'A']  # C pentatonic scale for MARGARET

def melody(flower, temperature, pressure, humidity, gas):
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Define the number of channels to use
    num_channels = 4

    # Reserve the specified number of channels
    pygame.mixer.set_num_channels(num_channels)

    while True:
        for j in range(4):
            note4 = list6[j]+ str(random.randint(3,4)) + "-quarter.wav"  # for gas
            note1 = list1[j] + str(random.randint(2, 4)) + "-half.wav"
            note2 = list2[j] + str(random.randint(2, 4)) + "-half.wav"
            note3 = list3[j] + str(random.randint(2, 4)) + "-half.wav"
                    
            # Define a list of music files to play on different channels
            music_files = [note1,note2,note3,note4]
            # print(music_files)
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
            pygame.time.wait(random.randint(500,600))  # Adjust the delay time as needed

            # Stop all channels to prepare for the next iteration
            pygame.mixer.stop()

            # Quit pygame
            #pygame.quit()
melody(1, 1, 1, 1, 1)


# In[69]:


import RPi.GPIO as GPIO

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 定义按钮所连接的GPIO引脚
button_pin = 17

# 设置按钮引脚为输入模式，并启用上拉电阻
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 定义按钮按下的回调函数
def button_callback(channel):
    print("Button pressed!")
    # 在这里添加你想要执行的代码，来控制你的程序运行和停止

# 为按钮引脚添加事件检测
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    while True:
        # 在这里可以继续执行其他的程序逻辑
        pass

except KeyboardInterrupt:
    # 清理GPIO设置
    GPIO.cleanup()


# In[30]:


import pygame
import random

list1 = ['E1' ,'G#1' ,'B1', 'G#1','E2' ,'G#2' ,'B2', 'G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4' ] # temperature for LILY
list2 = ['G#1', 'E1', 'G#1', 'E1','G#2', 'E2','G#2', 'E2','G#3', 'E3', 'G#3', 'E3','G#4', 'E4', 'G#4', 'E4'] # pressure for LILY
list3 = ['B1', 'C#1', 'E1', 'C#1','B2', 'C#2','B2', 'C#2', 'E3', 'C#3','B3', 'C#3','B4', 'C#4', 'E4', 'C#4'] # humidity for LILY

list5 = ['Ab', 'Bb', 'C', 'Eb', 'F']  # Ab pentatonic scale for ROSE
list6 = ['E1', 'F#1', 'G#1', 'B1', 'C#2','E2', 'F#2', 'G#2', 'B3', 'C#3','E3', 'F#3', 'G#4', 'B4', 'C#4','E4']  # E pentatonic scale for LILY
list7 = ['C', 'D', 'E', 'G', 'A']  # C pentatonic scale for MARGARET

def melody(flower, temperature, pressure, humidity, gas):
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Define the number of channels to use
    num_channels = 4

    # Reserve the specified number of channels
    pygame.mixer.set_num_channels(num_channels)

    while True:
        for j in range(16):
            note4 = list6[j]+ "-quarter.wav"  # for gas
            note1 = list1[j]+ "-half.wav"
            note2 = list2[j]+ "-half.wav"
            note3 = list3[j]+ "-half.wav"
                    
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
            pygame.time.wait(random.randint(500,600))  # Adjust the delay time as needed

            # Stop all channels to prepare for the next iteration
            pygame.mixer.stop()

            # Quit pygame
            #pygame.quit()
melody(1, 1, 1, 1, 1)


# In[66]:


#current situation 20230530
import pygame 
import random

list1 = ['G#1','E2' ,'G#2' ,'B2', 'G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4' ] # temperature for LILY
list2 = [ 'E1','G#2', 'E2','G#2', 'E2','G#3', 'E3', 'G#3', 'E3','G#4', 'E4', 'G#4', 'E4'] # pressure for LILY
list3 = [ 'C#1','B2', 'C#2','B2', 'C#2', 'E3', 'C#3','B3', 'C#3','B4', 'C#4', 'E4', 'C#4'] # humidity for LILY


list5 = ['Ab', 'Bb', 'C', 'Eb', 'F']  # Ab pentatonic scale for ROSE
list6 = [ 'B1', 'C#2','E2', 'F#2', 'G#2', 'B3', 'C#3','E3', 'F#3', 'G#4', 'B4', 'C#4','E4']  # E pentatonic scale for LILY
list7 = ['C', 'D', 'E', 'G', 'A']  # C pentatonic scale for MARGARET


previous_value1=0
previous_value2=0
previous_value3=0
previous_value4=0
j=9
h=10
i=6
k=8

def is_increasing(current_value,parameter):
    global previous_value1
    global previous_value2
    global previous_value3
    global previous_value4
    if(parameter=='humidity'):
        if previous_value1 is not None and current_value > previous_value1:
            previous_value1=current_value
            return 1
        elif previous_value1 > current_value:
            previous_value1=current_value
            return -1
        else:
            previous_value1=current_value
            return 0
    if(parameter=='temperature'):
        if previous_value2 is not None and current_value > previous_value2:
            previous_value2=current_value
            return 1
        elif previous_value2 > current_value:
            previous_value2=current_value
            return -1
        else:
            previous_value2=current_value
            return 0
    if(parameter=='pressure'):
        if previous_value3 is not None and current_value > previous_value3:
            previous_value3=current_value
            return 1
        elif previous_value3 > current_value:
            previous_value3=current_value
            return -1
        else:
            previous_value3=current_value
            return 0
    if(parameter=='gas'):
        if previous_value4 is not None and current_value > previous_value4:
            previous_value4=current_value
            return 1
        elif previous_value4 > current_value:
            previous_value4=current_value
            return -1
        else:
            previous_value4=current_value
            return 0


def melody(flower, temperature, pressure, humidity, gas):
    global h,i,j,k
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Define the number of channels to use
    num_channels = 4

    # Reserve the specified number of channels
    pygame.mixer.set_num_channels(num_channels)

    while True:
            temperature=random.uniform(20,30)
            humidity=random.uniform(20,30)
            pressure=random.uniform(20,30)
            gas=random.uniform(20,30)
            
            h+=is_increasing(humidity,'humidity')
            i+=is_increasing(pressure,'pressure')
            j+=is_increasing(temperature,'temperature')
            k+=is_increasing(gas,'gas')
            
            if(k>12 or k<0):
                k=9
            if(h>12 or h<0):
                h=9
            if(j>12 or j<0):
                j=9
            if(i>12 or i<0):
                i=9
                
            note4 = list6[k]+ "-quarter.wav"  # for gas
            note1 = list1[i]+ "-half.wav"
            note2 = list2[j]+ "-half.wav"
            note3 = list3[h]+ "-half.wav"
                    
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
melody(1, 1, 1, 1, 1)


# In[9]:


--previous_value=0
def is_increasing(current_value):
    global previous_value
    if previous_value is not None and current_value > previous_value:
        previous_value=current_value
        return 1
    elif previous_value > current_value:
        previous_value=current_value
        return -1
    else:
        previous_value=current_value
        return 0

while(1):
    temperature=random.uniform(20,35)
    print(is_increasing(temperature))


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

plt.style.use('ggplot')
subjects=['Rose','Lily','Margaret','Air']
flower=[60,40,68,94]

angles=np.linspace(0,2*np.pi,len(subjects), endpoint=False)
print(angles)

angles=np.concatenate((angles,[angles[0]]))
print(angles)

subjects.append(subjects[0])
flower.append(flower[0])

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
#basic plot
ax.plot(angles,flower, 'o--', color='g', label='Flower')
#fill plot
ax.fill(angles, flower, alpha=0.25, color='g')
#Add labels
ax.set_thetagrids(angles * 180/np.pi, subjects)
plt.figtext(1, 1, 'rose', fontsize=14, ha='center')

plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

window=tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")


# In[5]:


#current situation 20230619
#version description: same column
#comments:too dull

import pygame 
import random
    
def melody(flower, temperature, pressure, humidity, gas):
        global position
        position=6
        # Initialize pygame
        pygame.init()
        pygame.mixer.init()

        # Define the number of channels to use
        num_channels = 4

        # Reserve the specified number of channels
        pygame.mixer.set_num_channels(num_channels)

        while True:
                temperature=random.uniform(20,30)
                humidity=random.uniform(20,30)
                pressure=random.uniform(20,30)
                gas=random.uniform(20,30)
            
                position+=1
            
                if(position>12 or position<0):
                    position=6
                
                if flower == 'Lily':
                    list1 = ['G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4','E5' ,'G#5' ,'B5', 'G#5' ] # temperature for LILY
                    list2 = [ 'E2','G#3', 'E3','G#3', 'E3','G#4', 'E4', 'G#4', 'E4','G#5', 'E5', 'G#5', 'E5'] # pressure for LILY
                    list3 = [ 'C#2','B3', 'C#3','B3', 'C#3', 'E4', 'C#4','B4', 'C#4','B5', 'C#5', 'E5', 'C#5'] # humidity for LILY
                    list4 = [ 'B2', 'C#3','E3', 'F#3', 'G#3', 'B4', 'C#4','E4', 'F#4', 'G#5', 'B5', 'C#5','E5']  # E pentatonic scale for LILY
                elif flower == 'Margaret':
                    list1 = ['C4','A3','C4','A3','E4','C5','A4','G4','C4','D4','E4','C4','G3' ] # temperature for Margaret
                    list2 = ['E4','D4','G3','D3','A4','G4','E4','D4','E3','A3','D3','G3','C3'] # pressure for Margaret
                    list3 = ['G4','A4','E3','C4','G3','D4','C4','G3','G4','C5','G3','E3','C4'] # humidity for Margaret
                    list4 = ['A2','C3','D3', 'E3', 'G3', 'A3', 'C4', 'D4', 'E4', 'G4', 'A4','C5','D5']  # C pentatonic scale for Margaretprevious_value1=0
                elif flower == 'Rose':
                    list1 = ['Ab3','Bb3' ,'Bb4' ,'Ab4', 'Eb4','C3' ,'Eb3' ,'C4', 'Eb4','C4' ,'Eb3' ,'C3', 'F4' ] # temperature for ROSE
                    list2 = ['F3', 'Eb4', 'F4', 'Eb4', 'C4', 'Ab3', 'Bb3', 'F3', 'Bb3', 'F4', 'C4', 'Ab3', 'F3'] # pressure for ROSE
                    list3 = [ 'C4','F3','C4','F4','Bb3','C4','C3','Ab3','F3','Ab3','Bb3','Eb3','Ab4'] # humidity for ROSE
                    list4 = ['F2','Ab3', 'Bb3', 'C3',  'Eb3', 'F3', 'Ab4', 'Bb4', 'C4', 'Eb4', 'F4', 'Ab5','Bb5']  # Ab pentatonic scale for ROSE
                    
                '''if flower == 'Lily':
                    list1 = ['G#1','E2' ,'G#2' ,'B2', 'G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4' ] # temperature for LILY
                    list2 = [ 'E1','G#2', 'E2','G#2', 'E2','G#3', 'E3', 'G#3', 'E3','G#4', 'E4', 'G#4', 'E4'] # pressure for LILY
                    list3 = [ 'C#1','B2', 'C#2','B2', 'C#2', 'E3', 'C#3','B3', 'C#3','B4', 'C#4', 'E4', 'C#4'] # humidity for LILY
                   
                elif flower == 'Margaret':
                    list1 = ['C3','A2','C3','A2','E3','C4','A3','G3','C3','D3','E3','C3','G2' ] # temperature for Margaret
                    list2 = ['E3','D3','G2','D2','A3','G3','E3','D3','E2','A2','D2','G2','C2'] # pressure for Margaret
                    list3 = ['G3','A3','E2','C3','G2','D3','C3','G2','G3','C4','G2','E2','C3'] # humidity for Margaret
                elif flower == 'Rose':   
                    list1 = ['Ab2','Bb2' ,'Bb3' ,'Ab3', 'Eb3','C2' ,'Eb2' ,'C3', 'Eb3','C3' ,'Eb2' ,'C2', 'F3' ] # temperature for ROSE
                    list2 = ['F2', 'Eb3', 'F3', 'Eb3', 'C3', 'Ab2', 'Bb2', 'F2', 'Bb2', 'F3', 'C3', 'Ab2', 'F2'] # pressure for ROSE
                    list3 = [ 'C3','F2','C3','F3','Bb2','C3','C2','Ab2','F2','Ab2','Bb2','Eb2','Ab3'] # humidity for ROSE
                    '''    
                
                note1 = list1[position]+ "-half.wav"
                note2 = list2[position]+ "-half.wav"
                note3 = list3[position]+ "-half.wav"
                    
                # Define a list of music files to play on different channels
                music_files = [note1,note2,note3]
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

                # Delay before starting the next iteration
                pygame.time.wait(500)  # Adjust the delay time as needed

                # Stop all channels to prepare for the next iteration
                pygame.mixer.stop()

                # Quit pygame
                #pygame.quit()

name = 'Lily'
print(name+':\nonly 3 channels,playing the same column')
melody(name,1,1,1,1)
#melody(name, random.randint(0,100), random.randint(0,100), random.randint(0,100),random.randint(0,100))


# In[17]:


#current situation 20230619
#Random picking notes from each list
#comments: 

import pygame 
import random
    
def melody(flower, temperature, pressure, humidity, gas):
        global h,i,j,k
        # Initialize pygame
        pygame.init()
        pygame.mixer.init()

        # Define the number of channels to use
        num_channels = 4

        # Reserve the specified number of channels
        pygame.mixer.set_num_channels(num_channels)

        while True:
                temperature=random.uniform(20,30)
                humidity=random.uniform(20,30)
                pressure=random.uniform(20,30)
                gas=random.uniform(20,30)
            
                h=random.randint(0,14)
                i=random.randint(0,14)
                j=random.randint(0,14)
                k=random.randint(0,14)
            
                if flower == 'Lily':
                    list1 = ['G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4','E5' ,'G#5' ,'B5', 'G#5' ] # temperature for LILY
                    list2 = [ 'E2','G#3', 'E3','G#3', 'E3','G#4', 'E4', 'G#4', 'E4','G#5', 'E5', 'G#5', 'E5'] # pressure for LILY
                    list3 = [ 'C#2','B3', 'C#3','B3', 'C#3', 'E4', 'C#4','B4', 'C#4','B5', 'C#5', 'E5', 'C#5'] # humidity for LILY
                    list4 = [ 'B2', 'C#3','E3', 'F#3', 'G#3', 'B4', 'C#4','E4', 'F#4', 'G#5', 'B5', 'C#5','E5']  # E pentatonic scale for LILY
                elif flower == 'Margaret':
                    list1 = ['C4','A3','C4','A3','E4','C5','A4','G4','C4','D4','E4','C4','G3' ] # temperature for Margaret
                    list2 = ['E4','D4','G3','D3','A4','G4','E4','D4','E3','A3','D3','G3','C3'] # pressure for Margaret
                    list3 = ['G4','A4','E3','C4','G3','D4','C4','G3','G4','C5','G3','E3','C4'] # humidity for Margaret
                    list4 = ['A2','C3','D3', 'E3', 'G3', 'A3', 'C4', 'D4', 'E4', 'G4', 'A4','C5','D5']  # C pentatonic scale for Margaretprevious_value1=0
                elif flower == 'Rose':
                    list1 = ['Ab3','Bb3' ,'Bb4' ,'Ab4', 'Eb4','C3' ,'Eb3' ,'C4', 'Eb4','C4' ,'Eb3' ,'C3', 'F4' ] # temperature for ROSE
                    list2 = ['F3', 'Eb4', 'F4', 'Eb4', 'C4', 'Ab3', 'Bb3', 'F3', 'Bb3', 'F4', 'C4', 'Ab3', 'F3'] # pressure for ROSE
                    list3 = [ 'C4','F3','C4','F4','Bb3','C4','C3','Ab3','F3','Ab3','Bb3','Eb3','Ab4'] # humidity for ROSE
                    list4 = ['F2','Ab3', 'Bb3', 'C3',  'Eb3', 'F3', 'Ab4', 'Bb4', 'C4', 'Eb4', 'F4', 'Ab5','Bb5']  # Ab pentatonic scale for ROSE
                    
                '''if flower == 'Lily':
                    list1 = ['G#1','E2' ,'G#2' ,'B2', 'G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4' ] # temperature for LILY
                    list4 = [ 'B1', 'C#2','E2', 'F#2', 'G#2', 'B3', 'C#3','E3', 'F#3', 'G#4', 'B4', 'C#4','E4']  # E pentatonic scale for LILY
                elif flower == 'Margaret':
                    list1 = ['C3','A2','C3','A2','E3','C4','A3','G3','C3','D3','E3','C3','G2' ] # temperature for Margaret
                    list4 = ['A1','C2','D2', 'E2', 'G2', 'A2', 'C3', 'D3', 'E3', 'G3', 'A3','C4','D4']  # C pentatonic scale for Margaretprevious_value1=0
                elif flower == 'Rose':
                    list1 = ['Ab2','Bb2','C2','EB2', 'F2', 'Ab3', 'Bb3', 'C3', 'Eb3', 'F3', 'Ab4', 'Bb4', 'C4',  'EB4', 'F4' ] # temperature for ROSE
                    list4 = ['Ab2','Bb2','C2','EB2', 'F2', 'Ab3', 'Bb3', 'C3', 'Eb3', 'F3', 'Ab4', 'Bb4', 'C4',  'EB4', 'F4' ]  # Ab pentatonic scale for ROSE
                '''
                note4 = list4[k]+ "-quarter.wav"  # for gas
                note1 = list1[i]+ "-half.wav"
                note2 = list1[j]+ "-half.wav"
                note3 = list1[h]+ "-half.wav"
                    
                # Define a list of music files to play on different channels
                music_files = [note1,note2,note3]
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
            
                #channel = pygame.mixer.Channel(3)  # Get the channel corresponding to the index
                # Load and play the music file on the channel
                #sound = pygame.mixer.Sound(music_files[3])
                #channel.play(sound)

                # Delay before starting the next iteration
                pygame.time.wait(500)  # Adjust the delay time as needed

                # Stop all channels to prepare for the next iteration
                pygame.mixer.stop()

                # Quit pygame
                #pygame.quit()

name = 'Rose'
print(name +':\n4 channels,random picking note from the list')
melody(name,1,1,1,1)


# In[10]:


#current situation 20230619
#Random start with moving by one step
import pygame 
import random

def is_increasing(current_value,parameter):
        global previous_value1
        global previous_value2
        global previous_value3
        global previous_value4
        if(parameter=='humidity'):
            if previous_value1 is not None and current_value > previous_value1:
                previous_value1=current_value
                return 1
            elif previous_value1 > current_value:
                previous_value1=current_value
                return -1
            else:
                previous_value1=current_value
                return 0
        if(parameter=='temperature'):
            if previous_value2 is not None and current_value > previous_value2:
                previous_value2=current_value
                return 1
            elif previous_value2 > current_value:
                previous_value2=current_value
                return -1
            else:
                previous_value2=current_value
                return 0
        if(parameter=='pressure'):
            if previous_value3 is not None and current_value > previous_value3:
                previous_value3=current_value
                return 1
            elif previous_value3 > current_value:
                previous_value3=current_value
                return -1
            else:
                previous_value3=current_value
                return 0
        if(parameter=='gas'):
            if previous_value4 is not None and current_value > previous_value4:
                previous_value4=current_value
                return 1
            elif previous_value4 > current_value:
                previous_value4=current_value
                return -1
            else:
                previous_value4=current_value
                return 0

    
    
def melody(flower, temperature, pressure, humidity, gas):
        global h,i,j,k
        j=6
        h=6
        i=6
        k=6
        # Initialize pygame
        pygame.init()
        pygame.mixer.init()

        # Define the number of channels to use
        num_channels = 4

        # Reserve the specified number of channels
        pygame.mixer.set_num_channels(num_channels)

        while True:
                temperature=random.uniform(0,100)
                humidity=random.uniform(0,100)
                pressure=random.uniform(0,100)
                gas=random.uniform(0,100)
            
                h+=is_increasing(humidity,'humidity')
                i+=is_increasing(pressure,'pressure')
                j+=is_increasing(temperature,'temperature')
                k+=is_increasing(gas,'gas')
            
            
                if(k>12 or k<0):
                    k=6
                if(h>12 or h<0):
                    h=6
                if(j>12 or j<0):
                    j=6
                if(i>12 or i<0):
                    i=6
                    
                if flower == 'Lily':
                    list1 = ['G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4','E5' ,'G#5' ,'B5', 'G#5' ] # temperature for LILY
                    list2 = [ 'E2','G#3', 'E3','G#3', 'E3','G#4', 'E4', 'G#4', 'E4','G#5', 'E5', 'G#5', 'E5'] # pressure for LILY
                    list3 = [ 'C#2','B3', 'C#3','B3', 'C#3', 'E4', 'C#4','B4', 'C#4','B5', 'C#5', 'E5', 'C#5'] # humidity for LILY
                    list4 = [ 'B2', 'C#3','E3', 'F#3', 'G#3', 'B4', 'C#4','E4', 'F#4', 'G#5', 'B5', 'C#5','E5']  # E pentatonic scale for LILY
                elif flower == 'Margaret':
                    list1 = ['C4','A3','C4','A3','E4','C5','A4','G4','C4','D4','E4','C4','G3' ] # temperature for Margaret
                    list2 = ['E4','D4','G3','D3','A4','G4','E4','D4','E3','A3','D3','G3','C3'] # pressure for Margaret
                    list3 = ['G4','A4','E3','C4','G3','D4','C4','G3','G4','C5','G3','E3','C4'] # humidity for Margaret
                    list4 = ['A2','C3','D3', 'E3', 'G3', 'A3', 'C4', 'D4', 'E4', 'G4', 'A4','C5','D5']  # C pentatonic scale for Margaretprevious_value1=0
                elif flower == 'Rose':
                    list1 = ['Ab3','Bb3' ,'Bb4' ,'Ab4', 'Eb4','C3' ,'Eb3' ,'C4', 'Eb4','C4' ,'Eb3' ,'C3', 'F4' ] # temperature for ROSE
                    list2 = ['F3', 'Eb4', 'F4', 'Eb4', 'C4', 'Ab3', 'Bb3', 'F3', 'Bb3', 'F4', 'C4', 'Ab3', 'F3'] # pressure for ROSE
                    list3 = [ 'C4','F3','C4','F4','Bb3','C4','C3','Ab3','F3','Ab3','Bb3','Eb3','Ab4'] # humidity for ROSE
                    list4 = ['F2','Ab3', 'Bb3', 'C3',  'Eb3', 'F3', 'Ab4', 'Bb4', 'C4', 'Eb4', 'F4', 'Ab5','Bb5']  # Ab pentatonic scale for ROSE
                
                note4 = list4[k]+ "-quarter.wav"  # for gas
                note1 = list1[i]+ "-half.wav"
                note2 = list2[j]+ "-half.wav"
                note3 = list3[h]+ "-half.wav"
                    
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
previous_value1=0
previous_value2=0
previous_value3=0
previous_value4=0
name = 'Margaret'
print(name+ ": \n 4 channels, moving one step at a time")
melody(name,1,1,1,1)


# In[13]:


list4 = ['Ab2','Bb2','C2','EB2', 'F2', 'Ab3', 'Bb3', 'C3', 'Eb3', 'F3', 'Ab4', 'Bb4', 'C4',  'EB4', 'F4' ] 
len(list4)


# In[7]:





# In[ ]:

import random
def extract_array(arr, start, m):
    if m == 0:
        # 只取出 start 这一位的数
        extracted = [arr[start]]
    else:
        # 计算起始位置和结束位置
        end = start + m

        # 如果结束位置超过数组长度，调整为数组末尾的索引
        if end > len(arr):
            end = end % len(arr)

        # 如果 m 是负数，向前取绝对值为 m 的元素个数
        if m < 0:
            extracted = arr[end:start]
        else:
            # 提取部分数组
            if end > start:
                extracted = arr[start:end]
            else:
                extracted = arr[start:] + arr[:end]

    return extracted

# 示例数组
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# 起始位置和要取的元素个数
start = 7
i=0
while (i<10):
    m = random.randint(-4,4)
    i+=1
    # 调用函数提取数组
    extracted_array = extract_array(array, start, m)
    start+=m
    print(str(m)+str(extracted_array))




if flower == 'Lily':
                    list1 = ['G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4','E5' ,'G#5' ,'B5', 'G#5' ] # temperature for LILY
                    list2 = [ 'E2','G#3', 'E3','G#3', 'E3','G#4', 'E4', 'G#4', 'E4','G#5', 'E5', 'G#5', 'E5'] # pressure for LILY
                    list3 = [ 'C#2','B3', 'C#3','B3', 'C#3', 'E4', 'C#4','B4', 'C#4','B5', 'C#5', 'E5', 'C#5'] # humidity for LILY
                    list4 = [ 'B2', 'C#3','E3', 'F#3', 'G#3', 'B4', 'C#4','E4', 'F#4', 'G#5', 'B5', 'C#5','E5']  # E pentatonic scale for LILY
                elif flower == 'Margaret':
                    list1 = ['C4','A3','C4','A3','E4','C5','A4','G4','C4','D4','E4','C4','G3' ] # temperature for Margaret
                    list2 = ['E4','D4','G3','D3','A4','G4','E4','D4','E3','A3','D3','G3','C3'] # pressure for Margaret
                    list3 = ['G4','A4','E3','C4','G3','D4','C4','G3','G4','C5','G3','E3','C4'] # humidity for Margaret
                    list4 = ['A2','C3','D3', 'E3', 'G3', 'A3', 'C4', 'D4', 'E4', 'G4', 'A4','C5','D5']  # C pentatonic scale for Margaretprevious_value1=0
                elif flower == 'Rose':
                    list1 = ['Ab3','Bb3' ,'Bb4' ,'Ab4', 'Eb4','C3' ,'Eb3' ,'C4', 'Eb4','C4' ,'Eb3' ,'C3', 'F4' ] # temperature for ROSE
                    list2 = ['F3', 'Eb4', 'F4', 'Eb4', 'C4', 'Ab3', 'Bb3', 'F3', 'Bb3', 'F4', 'C4', 'Ab3', 'F3'] # pressure for ROSE
                    list3 = [ 'C4','F3','C4','F4','Bb3','C4','C3','Ab3','F3','Ab3','Bb3','Eb3','Ab4'] # humidity for ROSE
                    list4 = ['F2','Ab3', 'Bb3', 'C3',  'Eb3', 'F3', 'Ab4', 'Bb4', 'C4', 'Eb4', 'F4', 'Ab5','Bb5']  # Ab pe