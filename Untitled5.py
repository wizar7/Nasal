#!/usr/bin/env python
# coding: utf-8

# In[31]:


from music21 import stream, note, chord

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


# In[1]:


import pygame

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


import pygame

# Initialize pygame
pygame.init()

# Set up the mixer module
pygame.mixer.init()

pygame.mixer.get_num_channels()


# In[6]:



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



# In[5]:


import sys
print(sys.version)


# In[21]:


##间隔演奏，超级难听
import pygame
import random
    
list1 = ['Ab', 'Bb', 'C', 'Eb', 'F', 'Ab'] # Ab pentatonic scale for ROSE
list2 = ['E', 'F#', 'G#', 'B', 'C#', 'E'] # E pentatonic scale for LILY
list3 = ['C','D', 'E', 'G', 'A', 'C']    # C pentatonic scale for MARGARET
flower=1

def melody(flower,temperature,pressure,humidity,gas):
    while(1):
        for i in list1:
            note1=random.choice(list1)+str(random.randint(1,2))+"-half.wav"
            note2=random.choice(list2)+str(random.randint(1,2))+"-half.wav"
            note3=random.choice(list3)+str(random.randint(1,2))+"-half.wav"
            #note1="output7.wav"
            #note2="output8.wav"
            #note3="output9.wav"
            note4=random.choice(list1)+str(random.randint(1,2))+"-quarter.wav" #for gas


            # Initialize pygame
            pygame.init()

            # Set up the mixer module
            pygame.mixer.init()

            # Define the number of channels to use
            num_channels = 4

            # Reserve the specified number of channels
            pygame.mixer.set_num_channels(num_channels)

            # Define a list of music files to play on different channels

            if num % 2 == 0:
                    music_files = [note4]
                    num+=1
            else:
                    music_files = [note1,note2,note3,note4] 
                    num+=1
            print(music_files )

            # Loop through the music files
            for i, file in enumerate(music_files):
                channel = pygame.mixer.Channel(i)  # Get the channel corresponding to the index

                # Load and play the music file on the channel
                sound = pygame.mixer.Sound(file)


                channel.play(sound)


            # Wait for the music to finish playing
            for i in range(num_channels):
                while pygame.mixer.Channel(i).get_busy(): 
                    pass

            # Quit pygame
            pygame.quit()
melody(1,1,1,1,1)


# In[27]:


##间隔演奏，超级难听
import pygame
import random
    
list1 = ['Ab', 'Bb', 'C', 'Eb', 'F', 'Ab'] # Ab pentatonic scale for ROSE
list2 = ['E', 'F#', 'G#', 'B', 'C#', 'E'] # E pentatonic scale for LILY
list3 = ['C','D', 'E', 'G', 'A', 'C']    # C pentatonic scale for MARGARET
flower=1

def melody(flower,temperature,pressure,humidity,gas):
    while(1):
        note1=random.choice(list1)+str(random.randint(1,2))+"-half.wav"
        note2=random.choice(list2)+str(random.randint(1,2))+"-half.wav"
        note3=random.choice(list3)+str(random.randint(1,2))+"-half.wav"
        #note1="output7.wav"
        #note2="output8.wav"
        #note3="output9.wav"
        note4=random.choice(list1)+str(random.randint(1,2))+"-quarter.wav" #for gas


        # Initialize pygame
        pygame.init()

        # Set up the mixer module
        pygame.mixer.init()

        # Define the number of channels to use
        num_channels = 4

        # Reserve the specified number of channels
        pygame.mixer.set_num_channels(num_channels)

        # Define a list of music files to play on different channels
        music_files = [note1,note2,note3,note4]    
        print(music_files )

        # Loop through the music files
        for i, file in enumerate(music_files):
            channel = pygame.mixer.Channel(i)  # Get the channel corresponding to the index

            # Load and play the music file on the channel
            sound = pygame.mixer.Sound(file)
            
    
            channel.play(sound)


        # Wait for the music to finish playing
        for i in range(num_channels):
            while pygame.mixer.Channel(i).get_busy(): 
                pass

        # Quit pygame
        pygame.quit()
melody(1,1,1,1,1)


# In[23]:


-
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
numbers = [1, 2, 3, 4]  # Numbers 1 to 4

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


# In[12]:


#This is for the evaluate the most possible smeell detected.
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


# In[78]:


import pygame
import random

list1 = ['E' ,'G#' ,'B', 'G#'] # temperature for LILY
list2 = ['G#', 'E', 'G#', 'E'] # pressure for LILY
list3 = ['B', 'C#', 'E', 'C#'] # humidity for LILY

notes1 = ['Ab', 'Bb', 'C', 'Eb', 'F', 'Ab'] # Ab pentatonic scale for ROSE
notes2 = ['E', 'F#', 'G#', 'B', 'C#', 'E'] # E pentatonic scale for LILY
notes3 = ['C','D', 'E', 'G', 'A', 'C']    # C pentatonic scale for MARGARET

list4 = ['C', 'A', 'G', 'C', 'A', 'D', 'E', 'C']
notes5 = ['E', 'C#', 'B', 'E', 'C#', 'F#', 'G#', 'E']
notes6 = ['Ab', 'F', 'Eb', 'Ab', 'F', 'Bb', 'C', 'A']

list5 = ['Ab', 'Bb', 'C', 'Eb', 'F', 'Ab']  # Ab pentatonic scale for ROSE
list6 = ['E', 'F#', 'G#', 'B', 'C#', 'E']  # E pentatonic scale for LILY
list7 = ['C', 'D', 'E', 'G', 'A', 'C']  # C pentatonic scale for MARGARET

def melody(flower, temperature, pressure, humidity, gas):
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Define the number of channels to use
    num_channels = 4

    # Reserve the specified number of channels
    pygame.mixer.set_num_channels(num_channels)

    while True:
        for j in range(8):
            for i,note in enumerate(list1) :
                note1 = list1[i] + str(random.randint(2, 4)) + "-half.wav"
                note2 = list2[i] + str(random.randint(3, 4)) + "-half.wav"
                note3 = list3[i] + str(random.randint(3, 4)) + "-half.wav"
            note4 = list4[j]+ str(random.randint(1,4)) + "-quarter.wav"  # for gas

            # Define a list of music files to play on different channels
            music_files = [note1,note1,note4]
            print(music_files)

            # Loop through the music files
            for i, file in enumerate(music_files):
                channel = pygame.mixer.Channel(i)  # Get the channel corresponding to the index

                # Load and play the music file on the channel
                sound = pygame.mixer.Sound(file)
                channel.play(sound)

            # Delay before starting the next iteration
            pygame.time.wait(500)  # Adjust the delay time as needed

            # Stop all channels to prepare for the next iteration
            pygame.mixer.stop()

            # Quit pygame
                #pygame.quit()
melody(1, 1, 1, 1, 1)


# In[ ]:


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


# In[ ]:




