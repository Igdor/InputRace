from PIL import Image, ImageTk
import tkinter as tk

main_color = '#818589'
distance = 0

window = tk.Tk()
window.title("Input Race")
window.geometry("1400x900+10+20")
window.configure(bg=main_color)

lbl = tk.Label(window, text="Input Race", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color)
lbl.pack()
window.iconbitmap("icon.ico")

version = tk.Label(window, text="v1.01", fg='black', font=("Helvetica", 9), anchor="e", bg=main_color)
version.pack()

car_image = Image.open("resources/racing.png")
car_image = car_image.resize((190, 190))
car_image = ImageTk.PhotoImage(car_image)
finish_image = Image.open("resources/checkered.jpg")
finish_image = finish_image.resize((150, 460))
finish_image = ImageTk.PhotoImage(finish_image)

road = tk.Canvas(window, bg=main_color, width=1250, height=220, relief=tk.GROOVE, borderwidth=5)
road.place(x=80, y=140)

# Objects on the "road"

line_0 = road.create_line(200, 0, 200, 230, width=3, fill="#5A5A5A")
car = road.create_image(105, 120, image=car_image)
finish = road.create_image(1250, 0, image=finish_image)
line_100 = road.create_line(400, 0, 400, 210, width=3, fill="#5A5A5A")
text_100 = road.create_text(400, 220, text="100", font=('Helvetica', 14), fill='#5A5A5A')
line_200 = road.create_line(600, 0, 600, 210, width=3, fill="#5A5A5A")
text_200 = road.create_text(600, 220, text="200", font=('Helvetica', 14), fill='#5A5A5A')
line_300 = road.create_line(800, 0, 800, 210, width=3, fill="#5A5A5A")
text_300 = road.create_text(800, 220, text="300", font=('Helvetica', 14), fill='#5A5A5A')
line_400 = road.create_line(1000, 0, 1000, 210, width=3, fill="#5A5A5A")
text_400 = road.create_text(1000, 220, text="400", font=('Helvetica', 14), fill='#5A5A5A')
# line_500 = road.create_line(1200, 0, 1200, 210, width=3, fill="#5A5A5A")

# Interface under the "road" which appear afer start button were pressed

frame_interface = tk.Frame(window, bg=main_color, width=1250, height=220, relief=tk.GROOVE, borderwidth=0, border=0)
frame_interface.columnconfigure(2, weight=1)
frame_interface.rowconfigure(0, weight=1)

frame_distance = tk.Frame(frame_interface, width=150, height=150, relief=tk.GROOVE, borderwidth=5, bg=main_color)
frame_distance.grid(row=0, column=0, padx=30, pady=10)
frame_distance.grid_propagate(False)
frame_distance.columnconfigure(0, weight=1)
frame_distance.rowconfigure(1, weight=1)
label_distance_text = tk.Label(frame_distance, text="Distance:", font=("Helvetica", 16), bg=main_color, anchor="n")
label_distance_text.grid(row=0, column=0, columnspan=2)
label_distance = tk.Label(frame_distance, text="0", font=("Helvetica", 18), bg=main_color, anchor="center")
label_distance.grid(row=1, column=0, columnspan=2)

frame_last_boost = tk.Frame(frame_interface, width=150, height=150, relief=tk.GROOVE, borderwidth=5, bg=main_color)
frame_last_boost.grid(row=0, column=2, padx=30, pady=10)
frame_last_boost.grid_propagate(False)
frame_last_boost.columnconfigure(0, weight=1)
frame_last_boost.rowconfigure(1, weight=1)
label_last_boost_text = tk.Label(frame_last_boost, text="Boost:", font=("Helvetica", 16), bg=main_color, anchor="n")
label_last_boost_text.grid(row=0, column=0, columnspan=2, padx=2)
label_last_boost = tk.Label(frame_last_boost, text="+0", font=("Helvetica", 18), bg=main_color, anchor="center")
label_last_boost.grid(row=1, column=0, columnspan=2)


frame_input = tk.Frame(frame_interface, width=400, height=200, relief=tk.GROOVE, borderwidth=5, bg=main_color)
frame_input.grid(row=0, column=1)
frame_input.grid_propagate(False)
frame_input.columnconfigure(0, weight=1)
frame_input.rowconfigure(2, weight=1)
label_reaction = tk.Label(frame_input, text="Let`s go!", font=("Helvetica", 16), bg=main_color, anchor="n")
label_reaction.grid(row=0, column=0, columnspan=2, padx=40, pady=10)
field_input = tk.Entry(frame_input, bd=4, width=26, bg=main_color, font=("Helvetica", 18))
field_input.grid(row=1, column=0, padx=10, pady=10)

# Message with score which appear after winning the race

frame_winscore = tk.Frame(window, width=400, height=200, relief=tk.GROOVE, border=0, bg=main_color)
frame_winscore.columnconfigure(0, weight=1)
frame_winscore.rowconfigure(2, weight=1)
label_score = tk.Label(frame_winscore, text="Congratulations! You finished the race", font=("Helvetica", 12), bg=main_color)
label_score.grid(row=0, column=0, padx=10, pady=10)
label_score_2 = tk.Label(frame_winscore, text="Your score is:", font=("Helvetica", 12), bg=main_color)
label_score_2.grid(row=1, column=0, padx=10, pady=10)
label_winscore = tk.Label(frame_winscore, text="", font=("Helvetica", 25), bg=main_color)
label_winscore.grid(row=2, column=0, padx=10, pady=10)

label_tutorial = tk.Label(window, text="Welcome to the Input Race!\r Type any words and phrases to recieve boost and"
                                       " move your car to finish.\r Find out which words give better boost to achieve"
                                       " greater scores.\r Press Start to begin!", font=("Helvetica", 12), bg=main_color)
label_tutorial.place(x=395, y=560)
