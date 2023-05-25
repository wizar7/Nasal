#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

