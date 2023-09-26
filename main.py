import logging
from sys import stdout

import GameLogic
from Interface import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    handlers=[logging.FileHandler("info.log", encoding='utf-8', mode='w'), logging.StreamHandler(stdout)])

used_words = []

def start_game():
    btn_start.destroy()
    label_tutorial.destroy()
    frame_interface.place(x=290, y=480)
    logging.info("Game started")


def reaction(event):
    if event == "used":
        return "This input already used"
    elif event == "win":
        return "Congratulations! You finished the race."
    elif event == "zero":
        return "This input doesn't seem\r to have any power..."
    elif event == "short":
        return "Your input is too short!"
    else:
        return "You got boost!"


def end_game():
    frame_interface.destroy()
    frame_winscore.place(x=520, y=480)
    label_winscore.configure(text=str(GameLogic.win_score(used_words)))
    window.update()
    logging.info("Game ended with score " + str(GameLogic.win_score(used_words)) + ". Used words: " + str(used_words))


def boost():
    word = str(field_input.get())
    global distance
    global label_distance
    global label_last_boost
    if len(word) < 3:
        label_reaction.configure(text=reaction("short"))
        window.update()
        return None
    if word in used_words:
        label_reaction.configure(text=reaction("used"))
        window.update()
        return None
    else:
        added_distance = GameLogic.boost_calculator(word, used_words)
        distance += added_distance
        used_words.append(word)
        road.coords(car, [100+(distance*2), 120])
        road.tag_raise(car)
        if distance >= 500:
            end_game()
        else:
            label_distance.configure(text=str(round(distance, 2)))
            label_last_boost.configure(text="+" + str(round(added_distance, 2)))
            window.update()
            if added_distance == 0:
                label_reaction.configure(text=reaction("zero"))
            else:
                label_reaction.configure(text=reaction("boost"))


def press_enter(event):
    boost()


btn_start = tk.Button(window, text="START", bg="green", command=start_game, height=3, width=22, font=("Helvetica", 16))
btn_start.place(x=540, y=450)


btn_boost = tk.Button(frame_input, text="BOOST!", bg="green", command=boost, height=2, width=20, font=("Helvetica", 10))
btn_boost.grid(row=2, column=0, columnspan=2, padx=40, pady=10)
window.bind("<Return>", press_enter)

btn_exit = tk.Button(window, text="EXIT", bg="grey", command=exit,  height=2, width=6, font=("Helvetica", 10))
btn_exit.place(x=100, y=50)

window.mainloop()
