from tkinter import *
from tkinter import ttk


# window
window = Tk()
window.title('Pleymate Type Speed')
window.config(pady=40, padx=40, bg='#313866')
window.minsize(width=1220, height=720)
window.maxsize(width=1222, height=720)
window.geometry("700x700")
# app icon
window.iconbitmap('icon/pleymate.ico', )

# VARIABLES
WIDTH = 120
DISPLAY_HEIGHT = 10
INPUT_HEIGHT = 8


# ______________ ================================____________

# Display text retrieval
def retrieve_random_text():
    #  can replace with a http text request
    text = ("Clashing color palettes can drive consumers away from your website. The best hues to use are pleasing to "
            "the eyes and easily legible at different screen sizes and formats. A well-designed website would not "
            "pair bright yellow and white together since combining two light hues makes it difficult to read "
            "information. It’s also crucial to take into account the layering and of colors and how they appear next "
            "to each other."

            "\n\nYour website’s color scheme is crucial to your brand image. It shapes how viewers see your site, "
            "develops a sense of "
            "order and hierarchy, and allows important information stand out. Having a cohesive color scheme also "
            "creates a sense of flow and balance amongst different pages. A harmonious color palette truly does more "
            "than provide aesthetics.")
    text_display.delete(0.0, END)
    text_display.insert(0.0, text)


# prevent pasting on text input
def no_pasting(event):
    return "break"


def delete_random_text():
    text_display.delete(0.0, END)


current_words = 0


# input word counter
def input_word_count():
    global current_words
    input_text = text_input.get(1.0, 'end-1c')
    clean_list = [item for item in input_text.split(' ') if item.strip() != ""]  # using list comprehension
    current_words = len(clean_list)
    if input_text == "":
        current_words = 0
    word_count.config(text=f"Word Count: {current_words}")
    window.after(10, input_word_count)


counter_active = False


def check_counter_status():
    if not counter_active:  # execute only if the counter status is False
        seconds_counter()  # start counting
        speed_tracker()  # start tracking the typing speed


def seconds_counter():
    global current_seconds, counter_active
    counter_active = True
    counter.config(text=f"Elapsed seconds: {current_seconds}")
    window.after(1000, seconds_counter)
    current_seconds += 1


def speed_tracker():
    global current_words, current_seconds, current_speed
    time_in_minutes = current_seconds / 60
    current_speed = int(current_words / time_in_minutes)
    words_per_min.config(text=f"Words/min: {current_speed}")
    window.after(1, speed_tracker)


# styling
style = ttk.Style()  # OPTIONAL
style.configure('Rounded.TButton', relief='solid', borderwidth=1, background='#313866')
style.map('Rounded.TButton', foreground=[('active', '#974EC3')])

# ______________ ================================____________
# text display
text_display = Text(window,
                    state=NORMAL,
                    cursor='cross',
                    relief='solid',
                    font=14,
                    foreground='white',
                    pady=20,
                    padx=20,
                    height=DISPLAY_HEIGHT,
                    width=WIDTH,
                    bg='#974EC3',
                    wrap=WORD
                    )
text_display.grid(columnspan=3, row=0)

# text input
text_input = Text(window, cursor='ibeam',
                  state=NORMAL,
                  insertbackground="#FF6AC2",
                  relief='solid',
                  foreground='black',
                  font=14,
                  pady=20,
                  padx=20,
                  height=INPUT_HEIGHT,
                  width=WIDTH,
                  bg='white',
                  wrap=WORD
                  )
text_input.grid(columnspan=3, row=2)
text_input.focus()

# bindings
text_input.bind("<Control-v>", no_pasting)  # disable pasting (Ctrl+V)

# ______________ ================================____________

# buttons
retrieve_display_text_button = Button(window,
                                      text='Retrieve Text',
                                      command=retrieve_random_text,
                                      cursor='hand2',
                                      bg="yellow",
                                      fg="blue",
                                      width=20

                                      )
retrieve_display_text_button.grid(row=1, column=0)

delete_display_text_button = Button(window,
                                    text='Clear Text',
                                    command=delete_random_text,
                                    cursor='hand2',
                                    bg="red",
                                    fg="white",
                                    justify=LEFT,
                                    width=20
                                    )
delete_display_text_button.grid(row=1, column=2)

start_button = Button(window,
                      text='Start Test',
                      command=check_counter_status,
                      cursor='hand2',
                      bg="green",
                      fg="white",
                      width=20
                      )
start_button.grid(row=1, column=1)

# ______________ ================================____________

# word count (label)
word_count = Label(window, text=current_words, width=20)
word_count.grid(row=3, column=0)
input_word_count()

# counter and timer
current_seconds = 0
counter = Label(window, text=f"Elapsed seconds: {current_seconds}", width=20)
counter.grid(row=3, column=1)

# speed label word per minute
current_speed = 0
words_per_min = Label(window, text=f"Words/min: {current_speed}", width=20)
words_per_min.grid(row=3, column=2)

window.mainloop()
