from tkinter import *
from tkinter import ttk
import time

# window
window = Tk()
window.title('Xexi Type Speed')
window.config(pady=40, padx=40, bg='#313866')
window.minsize(width=1020, height=720)
window.maxsize(width=1920, height=1080)

# VARIABLES
WIDTH = 100
DISPLAY_HEIGHT = 10
INPUT_HEIGHT = 8


# Display text retrieval
def retrieve_random_text():
    #  can replace with a http text request
    text = ("Clashing color palettes can drive consumers away from your website. The best hues to use are pleasing to "
            "the eyes and easily legible at different screen sizes and formats. A well-designed website would not "
            "pair bright yellow and white together since combining two light hues makes it difficult to read "
            "information. It’s also crucial to take into account the layering and of colors and how they appear next "
            "to each other."

            "\n\nYour website’s color scheme is crucial to your brand image. It shapes how viewers see your site, "
            "develops a sense of"
            "order and hierarchy, and allows important information stand out. Having a cohesive color scheme also "
            "creates a sense of flow and balance amongst different pages. A harmonious color palette truly does more "
            "than provide aesthetics.")
    text_display.delete(0.0, END)
    text_display.insert(0.0, text)


current_words = 0


# input word counter
def input_word_count():
    global current_words
    input_text = text_input.get(1.0, 'end-1c')
    # print(input_text)
    # unclean_list = input_text.split(' ')

    # using list comprehension
    clean_list = [item for item in input_text.split(' ') if item.strip() != ""]

    current_words = len(clean_list)
    if input_text == "":
        current_words = 0
    word_count.config(text=f"Word Count: {current_words}")
    window.after(1000, input_word_count)


def timer():
    pass


# styling
style = ttk.Style()
style.configure('Rounded.TButton', relief='ridge', borderwidth=0, background='#974EC3')
style.map('Rounded.TButton', foreground=[('active', 'purple')], background=[('active', '#FF6AC2')])

# text display
text_display = Text(window,
                    state=NORMAL,
                    cursor='cross',
                    relief='solid',
                    font=14,
                    foreground='white',
                    )
text_display.pack()
text_display.config(height=DISPLAY_HEIGHT, width=WIDTH, bg='#974EC3', padx=3, pady=3)

# button
retrieve_display_text_button = ttk.Button(window,
                                          text='Retrieve Text',
                                          style="Rounded.TButton",
                                          command=retrieve_random_text,
                                          cursor='hand2',

                                          )
retrieve_display_text_button.pack()
retrieve_display_text_button.config()

# text input
text_input = Text(window, cursor='ibeam',
                  state=NORMAL,
                  insertbackground="#FF6AC2",
                  relief='solid',
                  foreground='black',
                  font=13
                  )
text_input.pack()
text_input.config(height=INPUT_HEIGHT, width=WIDTH, bg='white')
text_input.focus()

# word count (label)
word_count = Label(window, text=current_words)
word_count.pack()
input_word_count()

window.mainloop()
