# from tkinter import
from tkinter import *
from tkinter import ttk
import time

# window
window = Tk()
window.title('Xexi Type Speed')
window.config(pady=40, padx=40, bg='#313866')
window.minsize(width=1510, height=704)
window.maxsize(width=1920, height=1080)

# VARIABLES
WIDTH = 130
DISPLAY_HEIGHT = 15
INPUT_HEIGHT = 10


# Window size tracker
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
            "than provide aesthetics."

            "\n\nRead on to find thirty color palettes for a variety of industries, along with ten website mockups to "
            "help you visualize your own website palette. And, if your next adventure in color is establishing a "
            "palette for your brand, look no further than our color palette generator. You can extract color palettes "
            "from a photo and learn more about the color tools in Shutterstock Create.")
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


word_count = Label(window, text=current_words)
word_count.grid(row=4, column=2)

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
text_display.grid(row=0, column=0, columnspan=3, sticky=W)
text_display.config(height=DISPLAY_HEIGHT, width=WIDTH, bg='#974EC3', padx=3, pady=3)

# button
retrieve_display_text_button = ttk.Button(window,
                                          text='Retrieve Text',
                                          style="Rounded.TButton",
                                          command=retrieve_random_text,
                                          cursor='hand2',

                                          )
retrieve_display_text_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
retrieve_display_text_button.config()

# text input
text_input = Text(window, cursor='ibeam',
                  state=NORMAL,
                  insertbackground="#FF6AC2",
                  relief='solid',
                  foreground='black',
                  font=13
                  )
text_input.grid(row=3, column=0, columnspan=10, padx=3, pady=10, sticky="nsew", rowspan=1)
text_input.config(height=INPUT_HEIGHT, width=WIDTH, bg='white')
text_input.focus()

# get txt
input_word_count()

window.mainloop()
