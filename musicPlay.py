from music21 import stream, note, chord
def generate_melody(notes):
    melody = stream.Stream()

    for note_name in notes:
        if '.' in note_name:  # Handle chords
            chord_notes = note_name.split('.')
            chord_notes_objects = [note.Note(n) for n in chord_notes]
            chord_note = chord.Chord(chord_notes_objects)
            melody.append(chord_note)
        else:  # Single note
            new_note = note.Note(note_name)
            melody.append(new_note)

    return melody
notes = ['C4', 'A3', 'G3', 'C4', 'A3', 'D4', 'E4', 'C3']
#Ab, Bb, C, Eb, F, Ab

melody_stream = generate_melody(notes)

# Optionally, you can write the generated melody to a MIDI file
melody_stream.write('midi', fp='output.mid')

import pygame

pygame.init()
pygame.mixer.music.load('output.mid')
pygame.mixer.music.play()

# Set the number of times the MIDI file should repeat (-1 means continuous loop)
pygame.mixer.music.play(-1)

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    continue