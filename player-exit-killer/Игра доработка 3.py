import tkinter
import random

spicok_vragov = []
spicok_new_vragov = []
flag = False


def check():
    for elem in spicok_new_vragov:
        if canvas.coords(player) == canvas.coords(elem):
            label.config(text="А не надо было жульничать", bg="red")
            master.bind("<KeyPress>", stop)
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
    if not flag:
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


def new_vrag():
    global spicok_new_vragov
    spicok_new_vragov = []
    coords_exit = canvas.coords(exit)
    first_new_vrag_coords_x = coords_exit[0] - 60
    first_new_vrag_coords_y = coords_exit[1]
    first_new_vrag = canvas.create_image(first_new_vrag_coords_x, first_new_vrag_coords_y, image=new_vrag_img)
    second_new_vrag_coords_x = coords_exit[0] + 60
    second_new_vrag_coords_y = coords_exit[1]
    second_new_vrag = canvas.create_image(second_new_vrag_coords_x, second_new_vrag_coords_y, image=new_vrag_img)
    third_new_vrag_coords_x = coords_exit[0]
    third_new_vrag_coords_y = coords_exit[1] - 60
    third_new_vrag = canvas.create_image(third_new_vrag_coords_x, third_new_vrag_coords_y, image=new_vrag_img)
    four_new_vrag_coords_x = coords_exit[0]
    four_new_vrag_coords_y = coords_exit[1] + 60
    four_new_vrag = canvas.create_image(four_new_vrag_coords_x, four_new_vrag_coords_y, image=new_vrag_img)
    spicok_new_vragov.append(first_new_vrag)
    spicok_new_vragov.append(second_new_vrag)
    spicok_new_vragov.append(third_new_vrag)
    spicok_new_vragov.append(four_new_vrag)
    global flag
    flag = True
    check()


def delit():
    global exit
    global player
    global spicok_vragov
    global flag
    flag = False
    canvas.delete("all")
    canvas.create_image((300, 300), image=fons_img)
    label.config(text="Найди выход", bg="yellow")
    x_play = random.randint(1, 9)
    y_play = random.randint(1, 9)
    player = canvas.create_image((x_play * step, y_play * step),
                                 image=player_img)
    x_exit = random.randint(2, 8)
    y_exit = random.randint(2, 8)
    while abs(x_exit - x_play) < 3 or abs(y_exit - y_play) < 2:
        x_exit = random.randint(2, 8)
        y_exit = random.randint(2, 8)
    exit = canvas.create_image(x_exit * step, y_exit * step, image=exit_img)
    spicok_vragov = []
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
    master.bind("<KeyPress>", key_pressed)


step = 60
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg="blue", height=600, width=600)
fons_img = tkinter.PhotoImage(file="fons.png")
canvas.create_image((300, 300), image=fons_img)
exit_img = tkinter.PhotoImage(file="exit.png")
player_img = tkinter.PhotoImage(file="player.png")
vrag_img = tkinter.PhotoImage(file="враг.png")
new_vrag_img = tkinter.PhotoImage(file="дополнительный враг.png")
x_play = random.randint(1, 9)
y_play = random.randint(1, 9)
player = canvas.create_image((x_play * step, y_play * step),
                             image=player_img)
x_exit = random.randint(2, 8)
y_exit = random.randint(2, 8)
while abs(x_exit - x_play) < 2 or abs(y_exit - y_play) < 3:
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
label_itog = tkinter.Button(text="stop врагов", command=new_vrag, bg="green")
label.pack()
canvas.pack()
label_itog.pack()
restart.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
