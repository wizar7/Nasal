#current situation 20230619
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
        j=9
        h=10
        i=6
        k=8
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
                    
                if flower == 'Lily':
                    list1 = ['G#1','E2' ,'G#2' ,'B2', 'G#2','E3' ,'G#3' ,'B3', 'G#3','E4' ,'G#4' ,'B4', 'G#4' ] # temperature for LILY
                    list2 = [ 'E1','G#2', 'E2','G#2', 'E2','G#3', 'E3', 'G#3', 'E3','G#4', 'E4', 'G#4', 'E4'] # pressure for LILY
                    list3 = [ 'C#1','B2', 'C#2','B2', 'C#2', 'E3', 'C#3','B3', 'C#3','B4', 'C#4', 'E4', 'C#4'] # humidity for LILY
                    list4 = [ 'B1', 'C#2','E2', 'F#2', 'G#2', 'B3', 'C#3','E3', 'F#3', 'G#4', 'B4', 'C#4','E4']  # E pentatonic scale for LILY
                elif flower == 'Margaret':
                    list1 = ['C3','A2','C3','A2','E3','C4','A3','G3','C3','D3','E3','C3','G2' ] # temperature for Margaret
                    list2 = ['E3','D3','G2','D2','A3','G3','E3','D3','E2','A2','D2','G2','C2'] # pressure for Margaret
                    list3 = ['G3','A3','E2','C3','G2','D3','C3','G2','G3','C4','G2','E2','C3'] # humidity for Margaret
                    list4 = ['A1','C2','D2', 'E2', 'G2', 'A2', 'C3', 'D3', 'E3', 'G3', 'A3','C4','D4']  # C pentatonic scale for Margaretprevious_value1=0
                elif flower == 'Rose':
                    list1 = ['Ab2','Bb2' ,'Bb3' ,'Ab3', 'Eb3','C2' ,'Eb2' ,'C3', 'Eb3','C3' ,'Eb2' ,'C2', 'F3' ] # temperature for ROSE
                    list2 = ['F2', 'Eb3', 'F3', 'Eb3', 'C3', 'Ab2', 'Bb2', 'F2', 'Bb2', 'F3', 'C3', 'Ab2', 'F2'] # pressure for ROSE
                    list3 = [ 'C3','F2','C3','F3','Bb2','C3','C2','Ab2','F2','Ab2','Bb2','Eb2','Ab3'] # humidity for ROSE
                    list4 = ['F1','Ab2', 'Bb2', 'C2',  'Eb2', 'F2', 'Ab3', 'Bb3', 'C3', 'Eb3', 'F3', 'Ab4','Bb4']  # Ab pentatonic scale for ROSE
                
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
melody(name, random.randint(0,100), random.randint(0,100), random.randint(0,100),random.randint(0,100))