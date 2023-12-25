import pandas as pd

def create_isomorphic_keyboard(start_note, rows, cols, upper_increase = 5):
    # Define the notes and semitones
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_to_semitone = {note: i for i, note in enumerate(notes)}

    # Calculate the starting semitone index
    start_note_name, start_octave = start_note[:-1], int(start_note[-1])
    start_semitone_index = note_to_semitone[start_note_name] + start_octave * 12

    # Create the keyboard layout
    keyboard_layout = []
    for row in range(rows):
        keyboard_row = []
        for col in range(cols):
            # Calculate the semitone index for this key
            semitone_index = start_semitone_index + col - row * upper_increase
            octave, note_index = divmod(semitone_index, 12)
            note_name = notes[note_index]
            # Append the note with octave
            keyboard_row.append(f"{note_name}{octave}")
        keyboard_layout.append(keyboard_row)

    return pd.DataFrame(keyboard_layout)

keyboard_layout = create_isomorphic_keyboard("C2", 16, 16, 5)

# Display the layout
keyboard_layout = keyboard_layout.iloc[::-1]
print(keyboard_layout)
keyboard_layout.to_csv("keyboard_layout.csv", index=False)