import tkinter
import random

spicok_vragov = []


def check():
    for elem in spicok_vragov:
        if canvas.coords(player) == canvas.coords(elem):
            label.config(text="Проиграть", bg="red")
            master.bind("<KeyPress>", stop)
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
    move_frag(canvas, obj, move)
    check()


def move_frag(canvas, obj, move):
    for sopernik in spicok_vragov:
        if canvas.coords(player)[0] < canvas.coords(sopernik)[0] and \
                canvas.coords(player)[1] == canvas.coords(sopernik)[1]:
            move[0] = - 60
            move[1] = 0
            canvas.move(sopernik, move[0], move[1])
            check()
            if canvas.coords(sopernik) != canvas.coords(player):
                canvas.move(sopernik, move[0], move[1])
        elif canvas.coords(player)[0] > canvas.coords(sopernik)[0] and \
                canvas.coords(player)[1] == canvas.coords(sopernik)[1]:
            move[0] = 60
            move[1] = 0
            canvas.move(sopernik, move[0], move[1])
            check()
            if canvas.coords(sopernik) != canvas.coords(player):
                canvas.move(sopernik, move[0], move[1])
        elif canvas.coords(player)[0] == canvas.coords(sopernik)[0] and \
                canvas.coords(player)[1] > canvas.coords(sopernik)[1]:
            move[0] = 0
            move[1] = 60
            canvas.move(sopernik, move[0], move[1])
            check()
            if canvas.coords(sopernik) != canvas.coords(player):
                canvas.move(sopernik, move[0], move[1])
        elif canvas.coords(player)[0] == canvas.coords(sopernik)[0] and \
                canvas.coords(player)[1] < canvas.coords(sopernik)[1]:
            move[0] = 0
            move[1] = -60
            canvas.move(sopernik, move[0], move[1])
            check()
            if canvas.coords(sopernik) != canvas.coords(player):
                canvas.move(sopernik, move[0], move[1])
        check()


def stop(x):
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
    global spicok_vragov
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
    update_vrag = []
    check_x_koords = set()
    check_y_koors = set()
    for i in range(6):
        x_frag = random.randint(1, 9)
        y_frag = random.randint(1, 9)
        while ((x_frag == x_play or x_frag == x_exit) or (
                y_frag == y_play or y_frag == y_exit)) or x_frag in check_x_koords or y_frag in check_y_koors \
                or x_frag + 1 == x_play and y_frag + 1 == y_play or x_frag - 1 == x_play and y_frag - 1 == y_play \
                or x_frag + 1 == x_play and y_frag - 1 == y_play or x_frag - 1 == x_play and y_frag + 1 == y_play:
            x_frag = random.randint(1, 9)
            y_frag = random.randint(1, 9)
        check_x_koords.add(x_frag)
        check_y_koors.add(y_frag)
        vrag = canvas.create_image(x_frag * step, y_frag * step, image=vrag_img)
        update_vrag.append(vrag)
    spicok_vragov = update_vrag.copy()
    spicok_vragov.copy()
    master.bind("<KeyPress>", key_pressed)


step = 60
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg="blue", height=600, width=600)
fons_img = tkinter.PhotoImage(file="fons.png")
canvas.create_image((300, 300), image=fons_img)
exit_img = tkinter.PhotoImage(file="exit.png")
player_img = tkinter.PhotoImage(file="player.png")
vrag_img = tkinter.PhotoImage(file="враг.png")
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
check_x_koords = set()
check_y_koors = set()
for i in range(6):
    x_frag = random.randint(1, 9)
    y_frag = random.randint(1, 9)
    while ((x_frag == x_play or x_frag == x_exit) or (
            y_frag == y_play or y_frag == y_exit)) or x_frag in check_x_koords or y_frag in check_y_koors \
            or x_frag + 1 == x_play and y_frag + 1 == y_play or x_frag - 1 == x_play and y_frag - 1 == y_play \
            or x_frag + 1 == x_play and y_frag - 1 == y_play or x_frag - 1 == x_play and y_frag + 1 == y_play:
        x_frag = random.randint(1, 9)
        y_frag = random.randint(1, 9)
    check_x_koords.add(x_frag)
    check_y_koors.add(y_frag)
    vrag = canvas.create_image(x_frag * step, y_frag * step, image=vrag_img)
    spicok_vragov.append(vrag)
restart = tkinter.Button(text="restart", command=delit, bg="orange")
label.pack()
canvas.pack()
restart.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
