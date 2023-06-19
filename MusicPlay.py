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
