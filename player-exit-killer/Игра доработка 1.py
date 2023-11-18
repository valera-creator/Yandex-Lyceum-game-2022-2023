import tkinter
import random


def check():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!", bg="green")
        master.bind("<KeyPress>", stop)


def move_wrap(canvas, obj, move):
    canvas.move(obj, move[0], move[1])
    coords = canvas.coords(obj)
    to_move_x = 0
    to_move_y = 0
    if coords[0] < 60:
        to_move_x = 540
    elif coords[1] < 60:
        to_move_y = 540
    elif coords[1] >= 600:
        to_move_y = -540
    elif coords[0] > 540:
        to_move_x = -540
    canvas.move(obj, to_move_x, to_move_y)
    check()


def stop(arg):
    pass


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(canvas, player, [0, -step])
    if event.keysym == 'Down':
        move_wrap(canvas, player, [0, step])
    if event.keysym == 'Right':
        move_wrap(canvas, player, [step, 0])
    if event.keysym == 'Left':
        move_wrap(canvas, player, [-step, 0])


def delit():
    global exit
    global player
    canvas.delete("all")
    canvas.create_image((300, 300), image=fons_img)
    label.config(text="Найди выход", bg="yellow")
    x_play = random.randint(1, 9)
    y_play = random.randint(1, 9)
    player = canvas.create_image((x_play * step, y_play * step),
                                 image=player_img)
    x_exit = random.randint(2, 8)
    y_exit = random.randint(2, 8)
    while abs(x_exit - x_play) < 3 or abs(y_exit - y_play) < 3:
        x_exit = random.randint(2, 8)
        y_exit = random.randint(2, 8)
    exit = canvas.create_image(x_exit * step, y_exit * step, image=exit_img)
    master.bind("<KeyPress>", key_pressed)


step = 60
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg="blue", height=600, width=600)
exit_img = tkinter.PhotoImage(file="exit.png")
player_img = tkinter.PhotoImage(file="player.png")
fons_img = tkinter.PhotoImage(file="fons.png")
canvas.create_image((300, 300), image=fons_img)
x_play = random.randint(1, 9)
y_play = random.randint(1, 9)
player = canvas.create_image((x_play * step, y_play * step),
                             image=player_img)
x_exit = random.randint(2, 8)
y_exit = random.randint(2, 8)
while abs(x_exit - x_play) < 3 or abs(y_exit - y_play) < 3:
    x_exit = random.randint(2, 8)
    y_exit = random.randint(2, 8)
exit = canvas.create_image(x_exit * step, y_exit * step, image=exit_img)
label = tkinter.Label(text="Найти выход", bg="yellow")
restart = tkinter.Button(text="restart", command=delit, bg="orange")
label.pack()
canvas.pack()
restart.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
