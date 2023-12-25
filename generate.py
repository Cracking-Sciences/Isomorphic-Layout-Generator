import pandas as pd
import argparse

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
            semitone_index = start_semitone_index + col + row * upper_increase
            octave, note_index = divmod(semitone_index, 12)
            note_name = notes[note_index]
            # Append the note with octave
            keyboard_row.append(f"{note_name}{octave}")
        keyboard_layout.append(keyboard_row)

    return pd.DataFrame(keyboard_layout)

def highlight_c_notes(val):
    """
    Function to apply HTML styling to cells with C notes.
    """
    color = 'red' if ('C' in val and 'C#' not in val)else 'black'
    return f'<span style="color: {color}">{val}</span>'



if __name__ == "__main__":
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description="Create an Isomorphic Keyboard Layout")
    parser.add_argument("--start-note", type=str, help="Starting note, e.g., 'C2'")
    parser.add_argument("--rows", type=int, help="Number of rows in the keyboard layout")
    parser.add_argument("--cols", type=int, help="Number of columns in the keyboard layout")
    parser.add_argument("--upper-increase", type=int, help="Number of semitones to increase per row")
    
    args = parser.parse_args()
    
    keyboard_layout = create_isomorphic_keyboard(args.start_note, args.rows, args.cols, args.upper_increase)
    keyboard_layout = keyboard_layout.iloc[::-1]
    # Display the layout
    print(keyboard_layout)
    
    base_filename = f"keyboard_layout_{args.start_note}_{args.rows}x{args.cols}_increase{args.upper_increase}"
    csv_filename = base_filename + ".csv"
    html_filename = base_filename + ".html"

    keyboard_layout.to_csv(csv_filename, index=False)
    html_keyboard = keyboard_layout.to_html(escape=False, formatters=[highlight_c_notes]*keyboard_layout.shape[1])
    with open(html_filename, 'w') as file:
        file.write(html_keyboard)

    print(f"Files generated: {csv_filename}, {html_filename}")

# python .\generate.py --start-note C2 --rows 16 --cols 16 --upper-increase 5