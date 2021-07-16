import tkinter as tk
import math
import random

# --------------------- CONSTANTS ----------------------#
WORD_BANK = ['green', 'yellow', 'gorilla', 'cheese', 'virtue', 'avatar', 'photo', 'zoo', 'there', 'you', 'are', 'code', 'python', 'love', 'type', 'hope', 'tree', 'sleep', 'rabbit', 'cartoon', 'big', 'stuff', 'ruler', 'everything', 'clock', 'fish', 'war', 'star', 'hive', 'mind', 'force']
FONT = ('Arial', 13)
words_count = 0
current_word = None

# --------------------- FUNCTIONS ----------------------#

def start():
    get_word()
    window.after(60000, end_game)

def check_word(event):
    global current_word
    global words_count
    entered_word = word_entry.get()[:-1]
    if entered_word == current_word:
        words_count += 1
        word_entry.delete(0, 'end')
        get_word()
    else:
        print(f"Incorrect:{current_word}!={entered_word}")
        word_entry.delete(0, 'end')

def get_word():
    global current_word
    current_word = random.choice(WORD_BANK)
    word_label.config(text=f'{current_word}')

def end_game():
    subtitle_label.config(text=f"Your typing speed is {words_count} words per minute.")


# --------------------- UI ----------------------#

window = tk.Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)

# Labels
title_label = tk.Label(text='Typing Speed Tester', font=('Arial', 20))
title_label.grid(column=1, row=0)

subtitle_label = tk.Label(text='Click start to begin, then type the words that appear. Once 60 seconds are up, you will be given your score.', font=FONT)
subtitle_label.grid(column=1, row=1)

type_label = tk.Label(text='Type this word:', font=FONT)
type_label.grid(column=0, row=2)

word_label = tk.Label(text='', font=FONT)
word_label.grid(column=1, row=2)

# Entry
word_entry = tk.Entry(font=FONT)
word_entry.grid(column=1, row=3)

# Button
start_button = tk.Button(text='Start', font=FONT, command=start)
start_button.grid(column=1, row=4)

window.bind("<space>", check_word)

window.mainloop()