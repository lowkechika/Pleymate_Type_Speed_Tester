from tkinter import *

# window
window = Tk()
window.title('Pleymate Type Speed')
window.config(pady=40, padx=40, bg='#313866')
window.minsize(width=1220, height=720)
window.maxsize(width=1222, height=720)
window.geometry("700x700")
# app icon
window.iconbitmap('D:/Dev/Python Dev/My_Speed_Test_App_Version/pleymate.ico', )

# VARIABLES
WIDTH = 100
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
# noinspection PyUnusedLocal
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


counter_active = True
task_paused = False
reset = False


def check_counter_status():
    global reset, task_paused
    reset = False
    task_paused = False
    if counter_active:  # execute only if the counter status is True
        start_button.config(text="TASK ACTIVE")
        seconds_counter()  # start counting
        speed_tracker()  # start tracking the typing speed
    else:
        track_end_task()


def seconds_counter():
    global current_seconds, counter_active, task_paused
    if counter_active and not reset:
        start_button.config(state=DISABLED)
        pause_button.config(state=ACTIVE)
        counter.config(text=f"Elapsed seconds: {current_seconds}")
        window.after(1000, seconds_counter)
        current_seconds += 1
    elif reset:
        current_seconds = 0
        start_button.config(state=ACTIVE, text="START")
        pause_button.config(state=DISABLED, text="PAUSE TASK")
        counter.config(text=f"Elapsed seconds: {current_seconds}")

    elif reset and task_paused:
        current_seconds = 0
        start_button.config(state=ACTIVE, text="START")
        pause_button.config(state=DISABLED, text="PAUSE TASK")
        counter.config(text=f"Elapsed seconds: {current_seconds}")


def speed_tracker():
    global current_words, current_seconds, current_speed
    time_in_minutes = current_seconds / 60
    try:
        current_speed = int(current_words / time_in_minutes)
    except ZeroDivisionError:
        pass
    words_per_min.config(text=f"Words/min: {current_speed}")
    window.after(1, speed_tracker)


def track_end_task():
    global counter_active
    if not task_paused and not counter_active:
        counter_active = True
        pause_button.config(state=ACTIVE, text="PAUSE TASK")
        start_button.config(state=DISABLED)
        print('here!')
        check_counter_status()


def pause_task():
    global counter_active, task_paused
    start_button.config(state=ACTIVE, text="UNPAUSE")
    pause_button.config(state=DISABLED, text="TASK PAUSED")
    counter_active = False
    task_paused = True


def reset_task():
    global current_seconds, current_speed, reset
    reset = True
    current_speed = 0
    text_input.delete(0.0, END)
    check_pause_status()


def check_pause_status():
    if task_paused:
        seconds_counter()


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
                    wrap=WORD,
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
                                      text='RETRIEVE TEXT',
                                      command=retrieve_random_text,
                                      cursor='hand2',
                                      bg="yellow",
                                      fg="blue",
                                      width=20,
                                      font="Harvetica"

                                      )
retrieve_display_text_button.grid(row=1, column=0)

delete_display_text_button = Button(window,
                                    text='CLEAR TEXT',
                                    command=delete_random_text,
                                    cursor='hand2',
                                    bg="red",
                                    fg="white",
                                    justify=LEFT,
                                    width=20,
                                    font="Harvetica"
                                    )
delete_display_text_button.grid(row=1, column=2)

start_button = Button(window,
                      text='START',
                      command=check_counter_status,
                      cursor='hand2',
                      bg="green",
                      fg="white",
                      width=20,
                      font="Harvetica"
                      )
start_button.grid(row=1, column=1)

pause_button = Button(window,
                      text="PAUSE TASK",
                      command=pause_task,
                      bg="#974EC3",
                      width=20,
                      font="Harvetica",
                      relief="flat",
                      state=DISABLED,
                      fg="white")
pause_button.grid(row=5, column=1)

reset_button = Button(window,
                      text="RESET",
                      command=reset_task,
                      bg="red",
                      width=20,
                      font="Harvetica",
                      relief="flat",
                      fg="white"
                      )
reset_button.grid(row=5, column=2)

# ______________ ================================____________

# word count (labels)
word_count = Label(window, text=current_words, width=20, font="Harvetica")
word_count.grid(row=3, column=0)
input_word_count()

# counter and timer
current_seconds = 0
counter = Label(window, text=f"Elapsed seconds: {current_seconds}", width=20, font="Harvetica")
counter.grid(row=3, column=1)

# speed label word per minute
current_speed = 0
words_per_min = Label(window, text=f"Words/min: {current_speed}", width=20, font="Harvetica")
words_per_min.grid(row=3, column=2)

spliter = Label(window, height=2, bg='#313866')
spliter.grid(row=4, columnspan=3, column=0)

window.mainloop()

# by Pleymate (Hal)
