import tkinter

WHITE = "Белый"
BLACK = "Черный"


class Board:
    def __init__(self):
        self.check_realization_castling = False
        self.replace_castling = []
        self.game_over = False
        self.color = WHITE
        self.field = []
        self.coords = []
        self.replace_pawn = False
        for i in range(8):
            self.field.append([None] * 8)
        self.placement()

    def placement(self):
        self.first_black_officer = Officer(2, 7, BLACK)  # офицеры
        self.first_white_officer = Officer(2, 0, WHITE)
        self.second_black_officer = Officer(5, 7, BLACK)
        self.second_white_officer = Officer(5, 0, WHITE)
        """запасные офицеры"""
        self.first_reserv_officer_black = Officer(None, None, BLACK)
        self.second_reserv_officer_black = Officer(None, None, BLACK)
        self.third_reserv_officer_black = Officer(None, None, BLACK)
        self.four_reserv_officer_black = Officer(None, None, BLACK)
        self.five_reserv_officer_black = Officer(None, None, BLACK)
        self.six_reserv_officer_black = Officer(None, None, BLACK)
        self.seven_reserv_officer_black = Officer(None, None, BLACK)
        self.eight_reserv_officer_black = Officer(None, None, BLACK)
        self.first_reserv_officer_white = Officer(None, None, WHITE)
        self.second_reserv_officer_white = Officer(None, None, WHITE)
        self.third_reserv_officer_white = Officer(None, None, WHITE)
        self.four_reserv_officer_white = Officer(None, None, WHITE)
        self.five_reserv_officer_white = Officer(None, None, WHITE)
        self.six_reserv_officer_white = Officer(None, None, WHITE)
        self.seven_reserv_officer_white = Officer(None, None, WHITE)
        self.eight_reserv_officer_white = Officer(None, None, WHITE)

        self.first_knight_black = Knight(1, 7, BLACK)  # кони
        self.first_knight_white = Knight(1, 0, WHITE)
        self.second_knight_black = Knight(6, 7, BLACK)
        self.second_knight_white = Knight(6, 0, WHITE)
        """запасные кони"""
        self.first_reserv_knight_black = Knight(None, None, BLACK)
        self.second_reserv_knight_black = Knight(None, None, BLACK)
        self.third_reserv_knight_black = Knight(None, None, BLACK)
        self.four_reserv_knight_black = Knight(None, None, BLACK)
        self.five_reserv_knight_black = Knight(None, None, BLACK)
        self.six_reserv_knight_black = Knight(None, None, BLACK)
        self.seven_reserv_knight_black = Knight(None, None, BLACK)
        self.eight_reserv_knight_black = Knight(None, None, BLACK)
        self.first_reserv_knight_white = Knight(None, None, WHITE)
        self.second_reserv_knight_white = Knight(None, None, WHITE)
        self.third_reserv_knight_white = Knight(None, None, WHITE)
        self.four_reserv_knight_white = Knight(None, None, WHITE)
        self.five_reserv_knight_white = Knight(None, None, WHITE)
        self.six_reserv_knight_white = Knight(None, None, WHITE)
        self.seven_reserv_knight_white = Knight(None, None, WHITE)
        self.eight_reserv_knight_white = Knight(None, None, WHITE)

        self.first_rook_black = Rook(0, 7, BLACK)  # туры
        self.first_rook_white = Rook(0, 0, WHITE)
        self.second_rook_black = Rook(7, 7, BLACK)
        self.second_rook_white = Rook(7, 0, WHITE)
        """запасные ладьи"""
        self.first_reserv_rook_black = Rook(None, None, BLACK)
        self.first_reserv_rook_black.castling = False
        self.second_reserv_rook_black = Rook(None, None, BLACK)
        self.second_reserv_rook_black.castling = False
        self.third_reserv_rook_black = Rook(None, None, BLACK)
        self.third_reserv_rook_black.castling = False
        self.four_reserv_rook_black = Rook(None, None, BLACK)
        self.four_reserv_rook_black.castling = False
        self.five_reserv_rook_black = Rook(None, None, BLACK)
        self.five_reserv_rook_black.castling = False
        self.six_reserv_rook_black = Rook(None, None, BLACK)
        self.six_reserv_rook_black.castling = False
        self.seven_reserv_rook_black = Rook(None, None, BLACK)
        self.seven_reserv_rook_black.castling = False
        self.eight_reserv_rook_black = Rook(None, None, BLACK)
        self.eight_reserv_rook_black.castling = False
        self.first_reserv_rook_white = Rook(None, None, WHITE)
        self.first_reserv_rook_white.castling = False
        self.second_reserv_rook_white = Rook(None, None, WHITE)
        self.second_reserv_rook_white.castling = False
        self.third_reserv_rook_white = Rook(None, None, WHITE)
        self.third_reserv_rook_white.castling = False
        self.four_reserv_rook_white = Rook(None, None, WHITE)
        self.four_reserv_rook_white.castling = False
        self.five_reserv_rook_white = Rook(None, None, WHITE)
        self.five_reserv_rook_white.castling = False
        self.six_reserv_rook_white = Rook(None, None, WHITE)
        self.six_reserv_rook_white.castling = False
        self.seven_reserv_rook_white = Rook(None, None, WHITE)
        self.seven_reserv_rook_white.castling = False
        self.eight_reserv_rook_white = Rook(None, None, WHITE)
        self.eight_reserv_rook_white.castling = False

        self.black_king = King(3, 7, BLACK)  # короли
        self.white_king = King(3, 0, WHITE)

        self.black_queen = Queen(4, 7, BLACK)  # ферзи
        self.white_queen = Queen(4, 0, WHITE)
        """запасные ферзи"""
        self.first_reserv_queen_black = Queen(None, None, BLACK)
        self.second_reserv_queen_black = Queen(None, None, BLACK)
        self.third_reserv_queen_black = Queen(None, None, BLACK)
        self.four_reserv_queen_black = Queen(None, None, BLACK)
        self.five_reserv_queen_black = Queen(None, None, BLACK)
        self.six_reserv_queen_black = Queen(None, None, BLACK)
        self.seven_reserv_queen_black = Queen(None, None, BLACK)
        self.eight_reserv_queen_black = Queen(None, None, BLACK)
        self.first_reserv_queen_white = Queen(None, None, WHITE)
        self.second_reserv_queen_white = Queen(None, None, WHITE)
        self.third_reserv_queen_white = Queen(None, None, WHITE)
        self.four_reserv_queen_white = Queen(None, None, WHITE)
        self.five_reserv_queen_white = Queen(None, None, WHITE)
        self.six_reserv_queen_white = Queen(None, None, WHITE)
        self.seven_reserv_queen_white = Queen(None, None, WHITE)
        self.eight_reserv_queen_white = Queen(None, None, WHITE)

        self.first_black_pawn = Pawn(0, 6, BLACK)
        self.second_black_pawn = Pawn(1, 6, BLACK)
        self.third_black_pawn = Pawn(2, 6, BLACK)
        self.four_black_pawn = Pawn(3, 6, BLACK)
        self.five_black_pawn = Pawn(4, 6, BLACK)
        self.six_black_pawn = Pawn(5, 6, BLACK)
        self.seven_black_pawn = Pawn(6, 6, BLACK)
        self.eight_black_pawn = Pawn(7, 6, BLACK)

        self.first_white_pawn = Pawn(0, 1, WHITE)
        self.second_white_pawn = Pawn(1, 1, WHITE)
        self.third_white_pawn = Pawn(2, 1, WHITE)
        self.four_white_pawn = Pawn(3, 1, WHITE)
        self.five_white_pawn = Pawn(4, 1, WHITE)
        self.six_white_pawn = Pawn(5, 1, WHITE)
        self.seven_white_pawn = Pawn(6, 1, WHITE)
        self.eight_white_pawn = Pawn(7, 1, WHITE)
        self.field[2][7] = self.first_black_officer
        self.field[5][7] = self.second_black_officer
        self.field[2][0] = self.first_white_officer
        self.field[5][0] = self.second_white_officer
        self.field[1][7] = self.first_knight_black
        self.field[6][7] = self.second_knight_black
        self.field[1][0] = self.first_knight_white
        self.field[6][0] = self.second_knight_white
        self.field[0][7] = self.first_rook_black
        self.field[7][7] = self.second_rook_black
        self.field[0][0] = self.first_rook_white
        self.field[7][0] = self.second_rook_white
        self.field[4][7] = self.black_queen
        self.field[4][0] = self.white_queen
        self.field[3][7] = self.black_king
        self.field[3][0] = self.white_king
        self.field[0][6] = self.first_black_pawn
        self.field[1][6] = self.second_black_pawn
        self.field[2][6] = self.third_black_pawn
        self.field[3][6] = self.four_black_pawn
        self.field[4][6] = self.five_black_pawn
        self.field[5][6] = self.six_black_pawn
        self.field[6][6] = self.seven_black_pawn
        self.field[7][6] = self.eight_black_pawn
        self.field[0][1] = self.first_white_pawn
        self.field[1][1] = self.second_white_pawn
        self.field[2][1] = self.third_white_pawn
        self.field[3][1] = self.four_white_pawn
        self.field[4][1] = self.five_white_pawn
        self.field[5][1] = self.six_white_pawn
        self.field[6][1] = self.seven_white_pawn
        self.field[7][1] = self.eight_white_pawn
        self.black_reserv_shapes = [self.first_reserv_officer_black, self.second_reserv_officer_black,
                                    self.third_reserv_officer_black,
                                    self.four_reserv_officer_black, self.five_reserv_officer_black,
                                    self.six_reserv_officer_black,
                                    self.seven_reserv_officer_black,
                                    self.first_reserv_knight_black, self.second_reserv_knight_black,
                                    self.third_reserv_knight_black,
                                    self.four_reserv_knight_black, self.five_reserv_knight_black,
                                    self.six_reserv_knight_black,
                                    self.seven_reserv_knight_black,
                                    self.first_reserv_rook_black, self.second_reserv_rook_black,
                                    self.third_reserv_rook_black,
                                    self.four_reserv_rook_black, self.five_reserv_rook_black,
                                    self.six_reserv_rook_black,
                                    self.seven_reserv_rook_black,
                                    self.first_reserv_queen_black, self.second_reserv_queen_black,
                                    self.third_reserv_queen_black,
                                    self.four_reserv_queen_black, self.five_reserv_queen_black,
                                    self.six_reserv_queen_black,
                                    self.seven_reserv_queen_black, self.eight_reserv_rook_black,
                                    self.eight_reserv_knight_black,
                                    self.eight_reserv_officer_black,
                                    self.eight_reserv_queen_black]  # черные фигуры после дохождения пешки

        self.white_reserv_shapes = [self.first_reserv_officer_white, self.second_reserv_officer_white,
                                    self.third_reserv_officer_white,
                                    self.four_reserv_officer_white, self.five_reserv_officer_white,
                                    self.six_reserv_officer_white,
                                    self.seven_reserv_officer_white,
                                    self.first_reserv_knight_white, self.second_reserv_knight_white,
                                    self.third_reserv_knight_white,
                                    self.four_reserv_knight_white, self.five_reserv_knight_white,
                                    self.six_reserv_knight_white,
                                    self.seven_reserv_knight_white,
                                    self.first_reserv_rook_white, self.second_reserv_rook_white,
                                    self.third_reserv_rook_white,
                                    self.four_reserv_rook_white, self.five_reserv_rook_white,
                                    self.six_reserv_rook_white,
                                    self.seven_reserv_rook_white,
                                    self.first_reserv_queen_white, self.second_reserv_queen_white,
                                    self.third_reserv_queen_white,
                                    self.four_reserv_queen_white, self.five_reserv_queen_white,
                                    self.six_reserv_queen_white,
                                    self.seven_reserv_queen_white, self.eight_reserv_rook_white,
                                    self.eight_reserv_knight_white,
                                    self.eight_reserv_officer_white,
                                    self.eight_reserv_queen_white]  # белый фигуры после дохождения пешки

        self.all_black_shapes = [self.first_rook_black, self.second_rook_black, self.first_knight_black,
                                 self.second_knight_black,
                                 self.first_black_officer,
                                 self.second_black_officer, self.black_king, self.black_queen, self.first_black_pawn,
                                 self.second_black_pawn,
                                 self.third_black_pawn, self.four_black_pawn, self.five_black_pawn, self.six_black_pawn,
                                 self.seven_black_pawn, self.eight_black_pawn] + self.black_reserv_shapes

        self.all_white_shapes = [self.first_rook_white, self.second_rook_white, self.first_knight_white,
                                 self.second_knight_white,
                                 self.first_white_officer,
                                 self.second_white_officer, self.white_king, self.white_queen, self.first_white_pawn,
                                 self.second_white_pawn,
                                 self.third_white_pawn, self.four_white_pawn, self.five_white_pawn, self.six_white_pawn,
                                 self.seven_white_pawn, self.eight_white_pawn] + self.white_reserv_shapes

    def transform_color(self):
        if self.color == WHITE:
            self.color = BLACK
        else:
            self.color = WHITE

    def replace_coords(self, row1, col1, row2, col2):
        """если фигуру съели, то делаем ее координаты None"""
        if not self.field[row2][col2] is None:
            self.field[row2][col2].col = None
            self.field[row2][col2].row = None
        if not self.field[row1][col1] is None:
            self.field[row1][col1].col = col2
            self.field[row1][col1].row = row2

    def check_color(self, row, col):
        if self.field[row][col].color != self.color:
            transform_help_label.config(text=f"Ошибка: не твой цвет дорогой xd, ходит: {self.color}", bg="yellow",
                                        width=39,
                                        font=100)
            return False
        return True

    def check_exit_predel(self, row, col):
        """проверка на выход за пределы"""
        if not (0 <= row < 8 and 0 <= col < 8):
            transform_help_label.config(text=f"Ошибка: вышел за пределы, ходит: {self.color}", bg="yellow", width=36,
                                        font=100)
            return False
        return True

    def game_over_click(self):
        if not self.game_over:
            transform_help_label.config(text=f"{self.color} король испугался и свалил", bg="yellow", width=32,
                                        font=100)
            self.game_over = True

    def check_usually_chax(self):
        if self.color == WHITE:
            for elem in self.all_black_shapes:
                if elem.col is not None:
                    if elem.can_attack(board, elem.row, elem.col, self.white_king.row, self.white_king.col):
                        transform_help_label.config(text=f"Шах, Ходит: {self.color}",
                                                    bg="red", width=20, font=100)
                        return True
        elif self.color == BLACK:
            for elem in self.all_white_shapes:
                if elem.col is not None:
                    if elem.can_attack(board, elem.row, elem.col, self.black_king.row, self.black_king.col):
                        transform_help_label.config(text=f"Шах, Ходит: {self.color}",
                                                    bg="red", width=20, font=100)
                        return True
        transform_help_label.config(text=f"Ходит: {self.color}",
                                    bg="yellow", width=20, font=100)
        return False

    def mat_or_pat(self):
        count_shape = 0
        for elem in self.all_black_shapes:
            if elem.row is not None:
                count_shape += 1
        for elem in self.all_white_shapes:
            if elem.row is not None:
                count_shape += 1
        if count_shape == 2:
            transform_help_label.config(text="Ничья", bg="yellow", width=20, font=100)
            self.game_over = True
            return True
        attack = False
        """цвет соответствует цвету хода"""
        if self.color == BLACK:
            for shape in self.all_black_shapes:
                if shape.row is not None:
                    for i in range(8):
                        for j in range(8):
                            if shape.check_hod(board, shape.row, shape.col, i, j):
                                transform_help_label.config(text=f"Ходит: {self.color}", bg="yellow", width=20,
                                                            font=100)
                                return False
            for shape in self.all_white_shapes:
                if shape.row is not None:
                    for i in range(8):
                        for j in range(8):
                            if shape.can_attack(board, shape.row, shape.col, self.black_king.row, self.black_king.col):
                                attack = True
        if self.color == WHITE:
            for shape in self.all_white_shapes:
                if shape.row is not None:
                    for i in range(8):
                        for j in range(8):
                            if shape.check_hod(board, shape.row, shape.col, i, j):
                                transform_help_label.config(text=f"Ходит: {self.color}", bg="yellow", width=20,
                                                            font=100)
                                return False
            for shape in self.all_black_shapes:
                if shape.row is not None:
                    for i in range(8):
                        for j in range(8):
                            if shape.can_attack(board, shape.row, shape.col, self.white_king.row, self.white_king.col):
                                attack = True
        if not attack:
            transform_help_label.config(text="Пат", bg="yellow", width=20, font=100)
        else:
            transform_help_label.config(text="Мат королю", bg="red", width=20, font=100)
        self.game_over = True
        return True

    def realization_castling(self):
        self.check_realization_castling = False
        self.field[self.replace_castling[0]][self.replace_castling[1]] = \
            self.field[self.replace_castling[2]][self.replace_castling[3]]
        self.field[self.replace_castling[0]][self.replace_castling[1]].row += \
            self.replace_castling[4]
        self.field[self.replace_castling[2]][self.replace_castling[3]] = None
        canvas.delete("all")
        create_cells()
        create_update_field()
        transform_help_label.config(text=f"Ходит: {self.color}", bg="yellow", width=20, font=100)
        self.replace_castling = []
        self.mat_or_pat()
        if self.game_over:
            return None
        self.check_usually_chax()

    def replace_shape(self, text):
        result = self.check_replace_shape()
        if result is not None:
            self.coords = result
        row2, col2, index_shape = self.coords
        self.field[row2][col2].col = None
        self.field[row2][col2].row = None
        if self.color != WHITE:  # иллюзия что пешка прошла
            self.field[row2][col2] = self.eight_reserv_queen_white
        else:
            self.field[row2][col2] = self.eight_reserv_queen_black
        canvas.delete("all")
        create_cells()
        create_update_field()
        transform_help_label.config(
            text="Введите одно из названий: ладья, конь, офицер, ферзь а затем нажмите на сходить",
            bg="green", width=70,
            font=100)
        if len(text) == 1:
            self.transform_color()
            if board.color == WHITE:
                self.field[row2][col2] = self.eight_reserv_queen_white
            else:
                self.field[row2][col2] = self.eight_reserv_queen_black
            if text[0] == "ладья":
                shape = Rook
            elif text[0] == "конь":
                shape = Knight
            elif text[0] == "офицер":
                shape = Officer
            else:
                shape = Queen
            if self.color == WHITE:
                self.white_reserv_shapes[index_shape].row = None  # если не ферзь
                self.white_reserv_shapes[index_shape].col = None
                for i in range(len(self.white_reserv_shapes)):
                    if isinstance(self.white_reserv_shapes[i], shape):
                        if self.white_reserv_shapes[i].col is None:
                            self.field[row2][col2] = self.white_reserv_shapes[i]
                            self.field[row2][col2].col = col2
                            self.field[row2][col2].row = row2
                            break
            if self.color == BLACK:
                self.black_reserv_shapes[index_shape].row = None  # если не ферзь
                self.black_reserv_shapes[index_shape].col = None
                for i in range(len(self.black_reserv_shapes)):
                    if isinstance(self.black_reserv_shapes[i], shape):
                        if self.black_reserv_shapes[i].col is None:
                            self.field[row2][col2] = self.black_reserv_shapes[i]
                            self.field[row2][col2].col = col2
                            self.field[row2][col2].row = row2
                            break
            canvas.delete("all")
            create_cells()
            create_update_field()
            self.replace_pawn = False
            self.transform_color()
            transform_help_label.config(text=f"Ходит: {self.color}", bg="yellow", width=20, font=100)
            self.mat_or_pat()
            if self.game_over:
                return None
            self.check_usually_chax()
            self.coords = []

    def check_replace_shape(self):
        for i in range(len(self.all_black_shapes)):
            if isinstance(self.all_black_shapes[i], Pawn) and self.all_black_shapes[i].col == 0:
                self.replace_pawn = True
                return (self.all_black_shapes[i].row, self.all_black_shapes[i].col, i)
        for i in range(len(self.all_white_shapes)):
            if isinstance(self.all_white_shapes[i], Pawn) and self.all_white_shapes[i].col == 7:
                self.replace_pawn = True
                return (self.all_white_shapes[i].row, self.all_white_shapes[i].col, i)

    def main(self):
        if not self.game_over:
            text = hod_input.get().split()
            create_cells()
            create_update_field()
            if not self.replace_pawn:
                transform_help_label.config(text=f"Ходит: {self.color}", bg="yellow", width=20, font=100)
                if len(text) == 4:
                    if text[0].isdigit() and text[1].isdigit() and text[2].isdigit() and text[3].isdigit():
                        text = list(map(lambda x: int(x), text))  # превращение в int
                        text[0], text[1] = text[1], text[0]
                        text[2], text[3] = text[3], text[2]
                        if self.check_exit_predel(text[0], text[1]) and self.check_exit_predel(text[2],
                                                                                               text[3]):  # диапозон
                            if not self.field[text[0]][text[1]] is None:  # не пустая клетка
                                if self.check_color(text[0], text[1]):
                                    if self.field[text[0]][text[1]].check_hod(board, text[0], text[1], text[2],
                                                                              text[3]):
                                        self.replace_coords(text[0], text[1], text[2], text[3])
                                        self.field[text[2]][text[3]] = self.field[text[0]][text[1]]
                                        self.field[text[0]][text[1]] = None
                                        if isinstance(self.field[text[2]][text[3]], King) or isinstance(
                                                self.field[text[2]][text[3]], Rook):
                                            self.field[text[2]][text[3]].castling = False
                                        if isinstance(self.field[text[2]][text[3]], Pawn):
                                            self.field[text[2]][text[3]].first_hod = True
                                        canvas.delete("all")
                                        create_cells()
                                        create_update_field()
                                        self.transform_color()
                                        if not self.replace_pawn:
                                            self.mat_or_pat()
                                            if self.game_over:
                                                return None
                                            self.check_usually_chax()
                            else:
                                transform_help_label.config(
                                    text=f"Ошибка: нельзя передвинуть ничего, ходит: {self.color}",
                                    bg="yellow",
                                    width=42, font=100)
                if self.check_realization_castling:
                    self.realization_castling()
            self.check_replace_shape()
            if self.replace_pawn:
                self.replace_shape(text)


class Shape:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def check_castling(self, board, row1, col1, row2, col2):
        if not board.field[row1][col1].castling:
            transform_help_label.config(text=f"Ошибка: король уже ходил, Ходит: {board.color}",
                                        bg="yellow",
                                        width=34, font=100)
            return False
        if row1 > row2:
            if board.field[row1][col1].color == BLACK:
                if board.first_rook_black.col is None:
                    transform_help_label.config(text=f"Ошибка: ладью кильнули, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                if not board.first_rook_black.castling:
                    transform_help_label.config(text=f"Ошибка: ладья уже ходила, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                if not board.field[1][7] is None or not board.field[2][7] is None:
                    transform_help_label.config(text=f"Ошибка: поле занято, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                for elem in board.all_white_shapes:
                    if elem.row is not None:
                        if elem.can_attack(board, elem.row, elem.col, 1, 7) or elem.can_attack(board, elem.row,
                                                                                               elem.col, 2, 7):
                            transform_help_label.config(text=f"Ошибка: угроза королю, Ходит: {board.color}",
                                                        bg="yellow",
                                                        width=37, font=100)
                            return False

                board.check_realization_castling = True
                board.replace_castling = [2, 7, 0, 7, 2]
            elif board.field[row1][col1].color == WHITE:
                if board.first_rook_white.col is None:
                    transform_help_label.config(text=f"Ошибка: ладью кильнули, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                if not board.first_rook_white.castling:
                    transform_help_label.config(text=f"Ошибка: ладья уже ходила, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                if not board.field[1][0] is None or not board.field[2][0] is None:
                    transform_help_label.config(text=f"Ошибка: поле занято, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                for elem in board.all_black_shapes:
                    if elem.row is not None:
                        if elem.can_attack(board, elem.row, elem.col, 1, 0) or elem.can_attack(board, elem.row,
                                                                                               elem.col, 2, 0):
                            transform_help_label.config(text=f"Ошибка: угроза королю, Ходит: {board.color}",
                                                        bg="yellow",
                                                        width=37, font=100)
                            return False

                board.replace_castling = [2, 0, 0, 0, 2]
                board.check_realization_castling = True
            return True
        else:
            if board.field[row1][col1].color == BLACK:
                if board.second_rook_black.col is None:
                    transform_help_label.config(text=f"Ошибка: ладью кильнули, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                if not board.second_rook_black.castling:
                    transform_help_label.config(text=f"Ошибка: ладья уже ходила, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                if not board.field[4][7] is None or not board.field[5][7] is None or not board.field[6][7] is None:
                    transform_help_label.config(text=f"Ошибка: поле занято, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                for elem in board.all_white_shapes:
                    if elem.row is not None:
                        if elem.can_attack(board, elem.row, elem.col, 4, 7) or elem.can_attack(board, elem.row,
                                                                                               elem.col, 5, 7):
                            transform_help_label.config(text=f"Ошибка: угроза королю, Ходит: {board.color}",
                                                        bg="yellow",
                                                        width=37, font=100)
                            return False

                board.replace_castling = [4, 7, 7, 7, -3]
                board.check_realization_castling = True
            if board.field[row1][col1].color == WHITE:
                if board.second_rook_white.col is None:
                    transform_help_label.config(text=f"Ошибка: ладью кильнули, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                if not board.second_rook_white.castling:
                    transform_help_label.config(text=f"Ошибка: ладья уже ходила, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                if not board.field[4][0] is None or not board.field[5][0] is None or not board.field[6][0] is None:
                    transform_help_label.config(text=f"Ошибка: поле занято, Ходит: {board.color}",
                                                bg="yellow",
                                                width=34, font=100)
                    return False
                for elem in board.all_black_shapes:
                    if elem.row is not None:
                        if elem.can_attack(board, elem.row, elem.col, 4, 0) or elem.can_attack(board, elem.row,
                                                                                               elem.col, 5, 0):
                            transform_help_label.config(text=f"Ошибка: угроза королю, Ходит: {board.color}",
                                                        bg="yellow",
                                                        width=37, font=100)
                            return False

                board.replace_castling = [4, 0, 7, 0, -3]
                board.check_realization_castling = True
            return True

    def check_chax_in_hod(self, board, row1, col1, row2, col2):
        """если короля всеравно атакуют после передвижения то False"""
        first = board.field[row1][col1]
        second = board.field[row2][col2]
        save_row_second = ""
        if board.field[row2][col2] is not None:
            save_row_second = board.field[row2][col2].row
            board.field[row2][col2].row = None
        board.field[row2][col2] = board.field[row1][col1]
        board.field[row1][col1] = None
        if board.color == BLACK:
            for elem in board.all_white_shapes:
                if elem.row is not None:
                    if elem.can_attack(board, elem.row, elem.col, board.black_king.row, board.black_king.col):
                        transform_help_label.config(text=f"Ошибка: Шах черному королю, Ходит: {board.color}",
                                                    bg="red",
                                                    width=37, font=100)
                        board.field[row1][col1] = first
                        board.field[row2][col2] = second
                        if save_row_second != "":
                            board.field[row2][col2].row = save_row_second

                        return False
            board.field[row1][col1] = first
            board.field[row2][col2] = second
            if save_row_second != "":
                board.field[row2][col2].row = save_row_second
            return True
        elif board.color == WHITE:
            for elem in board.all_black_shapes:
                if elem.row is not None:
                    if elem.can_attack(board, elem.row, elem.col, board.white_king.row, board.white_king.col):
                        transform_help_label.config(text=f"Ошибка: Шах белому королю, Ходит: {board.color}",
                                                    bg="red",
                                                    width=37, font=100)
                        board.field[row1][col1] = first
                        board.field[row2][col2] = second
                        if save_row_second != "":
                            board.field[row2][col2].row = save_row_second
                        return False
            board.field[row1][col1] = first
            board.field[row2][col2] = second
            if save_row_second != "":
                board.field[row2][col2].row = save_row_second
            return True

    def check_line(self, board, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            return False
        if row2 < row1:
            for i in range(row2 + 1, row1):
                if not board.field[i][col2] is None:
                    if not isinstance(board.field[i][col2], King) or isinstance(board.field[i][col2], King) and \
                            board.field[i][col2].color == board.field[row1][col1].color:
                        transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                    bg="yellow",
                                                    width=46, font=100)
                        return False
        elif row2 > row1:
            for i in range(row1 + 1, row2):
                if not board.field[i][col2] is None:
                    if not isinstance(board.field[i][col2], King) or isinstance(board.field[i][col2], King) and \
                            board.field[i][col2].color == board.field[row1][col1].color:
                        transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                    bg="yellow",
                                                    width=46, font=100)
                        return False

        elif col2 < col1:
            for i in range(col1 - 1, col2, -1):
                if not board.field[row1][i] is None:
                    if not isinstance(board.field[row1][i], King) or isinstance(board.field[row1][i], King) and \
                            board.field[row1][i].color == board.field[row1][col1].color:
                        transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                    bg="yellow",
                                                    width=46, font=100)
                        return False
        elif col1 < col2:
            for i in range(col1 + 1, col2):
                if not board.field[row1][i] is None:
                    if not isinstance(board.field[row1][i], King) or isinstance(board.field[row1][i], King) and \
                            board.field[row1][i].color == board.field[row1][col1].color:
                        transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                    bg="yellow",
                                                    width=46, font=100)
                        return False
        return True

    def check_diaganal(self, board, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            return False
        if row2 > row1 and col1 > col2:
            j = col1 - 1
            for i in range(row1 + 1, row2):
                if not board.field[i][j] is None:
                    if not isinstance(board.field[i][j], King) or isinstance(board.field[i][j], King) and \
                            board.field[i][j].color == board.field[row1][col1].color:
                        transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                    bg="yellow",
                                                    width=46, font=100)
                        return False
                j -= 1
        elif row2 > row1 and col1 < col2:
            j = col1 + 1
            for i in range(row1 + 1, row2):
                if not board.field[i][j] is None:
                    if not isinstance(board.field[i][j], King) or isinstance(board.field[i][j], King) and \
                            board.field[i][j].color == board.field[row1][col1].color:
                        transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                    bg="yellow",
                                                    width=46, font=100)
                        return False
                j += 1
        elif row2 < row1 and col1 > col2:
            j = col1 - 1
            for i in range(row1 - 1, row2, - 1):
                if not board.field[i][j] is None:
                    if not isinstance(board.field[i][j], King) or isinstance(board.field[i][j], King) and \
                            board.field[i][j].color == board.field[row1][col1].color:
                        transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                    bg="yellow",
                                                    width=46, font=100)
                        return False
                j -= 1
        elif row2 < row1 and col1 < col2:
            j = col1 + 1
            for i in range(row1 - 1, row2, -1):
                if not board.field[i][j] is None:
                    if not isinstance(board.field[i][j], King) or isinstance(board.field[i][j], King) and \
                            board.field[i][j].color == board.field[row1][col1].color:
                        transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                    bg="yellow",
                                                    width=46, font=100)
                        return False
                j += 1
        return True

    def team_eating(self, board, row1, col1, row2, col2):
        if not board.field[row2][col2] is None and board.field[row1][col1].color == board.field[row2][col2].color:
            transform_help_label.config(text=f"Ошибка: жрать своих нельзя! предатель!!! Ходит: {board.color}",
                                        bg="yellow",
                                        width=50, font=100)  # проверка на конечную позицию
            return False
        return True


class Officer(Shape):
    def check_hod(self, board, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            transform_help_label.config(text=f"Ошибка: одна и тажа клетка, ходит: {board.color}",
                                        bg="yellow",
                                        width=37, font=100)
            return False
        if abs(col1 - col2) != abs(row2 - row1):  # проверка на диаганаль
            transform_help_label.config(text=f"Ошибка: не диаганаль, Ходит: {board.color}",
                                        bg="yellow",
                                        width=31, font=100)
            return False
        if not self.team_eating(board, row1, col1, row2, col2):  # проверка на конечную позицию
            return False
        if not self.check_chax_in_hod(board, row1, col1, row2, col2):
            return False
        return self.check_diaganal(board, row1, col1, row2, col2)

    def can_attack(self, board, row1, col1, row2, col2):
        return abs(col1 - col2) == abs(row2 - row1) and self.check_diaganal(board, row1, col1, row2, col2)


class Knight(Shape):
    def check_hod(self, board, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            transform_help_label.config(text=f"Ошибка: одна и тажа клетка, ходит: {board.color}",
                                        bg="yellow",
                                        width=37, font=100)
            return False
        if abs(row1 - row2) == 2 and abs(col1 - col2) == 1 or abs(col1 - col2) == 2 and abs(row1 - row2) == 1:

            if not self.team_eating(board, row1, col1, row2, col2):  # проверка на конечную позицию
                return False
            return self.check_chax_in_hod(board, row1, col1, row2, col2)
        transform_help_label.config(text=f"Ошибка: не буква г!!!, Ходит: {board.color}",
                                    bg="yellow",
                                    width=30, font=100)
        return False

    def can_attack(self, board, row1, col1, row2, col2):
        return abs(row1 - row2) == 2 and abs(col1 - col2) == 1 or abs(col1 - col2) == 2 and abs(row1 - row2) == 1


class Rook(Shape):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.castling = True

    def check_hod(self, board, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            transform_help_label.config(text=f"Ошибка: одна и тажа клетка, ходит: {board.color}",
                                        bg="yellow",
                                        width=37, font=100)
            return False
        if row1 != row2 and col1 != col2:
            transform_help_label.config(text=f"Ошибка: тура может двигаться только по прямой, Ходит: {board.color}",
                                        bg="yellow",
                                        width=54, font=100)
            return False
        if not self.team_eating(board, row1, col1, row2, col2):  # проверка на конечную позицию
            return False
        if not self.check_chax_in_hod(board, row1, col1, row2, col2):
            return False
        return self.check_line(board, row1, col1, row2, col2)

    def can_attack(self, board, row1, col1, row2, col2):
        return self.check_line(board, row1, col1, row2, col2) and not (row1 != row2 and col1 != col2)


class Queen(Shape):
    def check_hod(self, board, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            transform_help_label.config(text=f"Ошибка: одна и тажа клетка, ходит: {board.color}",
                                        bg="yellow",
                                        width=36, font=100)
            return False
        if not self.team_eating(board, row1, col1, row2, col2):  # проверка на конечную позицию
            return False
        if row1 != row2 and col1 != col2 and abs(col1 - col2) != abs(row2 - row1):
            transform_help_label.config(text=f"Ошибка: Так ферзь не ходит, Ходит: {board.color}",
                                        bg="yellow",
                                        width=36, font=100)
            return False
        if not self.check_chax_in_hod(board, row1, col1, row2, col2):
            return False
        if row1 != row2 and col1 != col2:
            return self.check_diaganal(board, row1, col1, row2, col2)
        else:
            return self.check_line(board, row1, col1, row2, col2)

    def can_attack(self, board, row1, col1, row2, col2):
        if row1 != row2 and col1 != col2 and abs(col1 - col2) != abs(row2 - row1):
            return False
        if row1 != row2 and col1 != col2:
            return self.check_diaganal(board, row1, col1, row2, col2)
        return self.check_line(board, row1, col1, row2, col2)


class King(Shape):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.castling = True

    def check_hod(self, board, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            transform_help_label.config(text=f"Ошибка: одна и тажа клетка, ходит: {board.color}",
                                        bg="yellow",
                                        width=35, font=100)
            return False
        if not self.team_eating(board, row1, col1, row2, col2):
            return False
        if abs(row1 - row2) == 2 and col1 == col2:
            if not self.check_castling(board, row1, col1, row2, col2):
                return False
        elif abs(col1 - col2) > 1 or abs(row1 - row2) > 1:
            transform_help_label.config(text=f"Ошибка: Король так не ходит, ходит: {board.color}",
                                        bg="yellow",
                                        width=35, font=100)
            return False
        if board.color == WHITE:
            for elem in board.all_black_shapes:
                if elem.col is not None:
                    if elem.can_attack(board, elem.row, elem.col, row2, col2):
                        transform_help_label.config(text=f"Ошибка: Ход под шах, Ходит: {board.color}",
                                                    bg="red",
                                                    width=30, font=100)
                        if isinstance(elem, King):
                            transform_help_label.config(text=f"Ошибка: король к королю не ходит, Ходит: {board.color}",
                                                        bg="yellow",
                                                        width=42, font=100)
                        return False
        if board.color == BLACK:
            for elem in board.all_white_shapes:
                if elem.col is not None:
                    if elem.can_attack(board, elem.row, elem.col, row2, col2):
                        transform_help_label.config(text=f"Ошибка: Ход под шах, Ходит: {board.color}",
                                                    bg="red",
                                                    width=30, font=100)
                        if isinstance(elem, King):
                            transform_help_label.config(text=f"Ошибка: король к королю не ходит, Ходит: {board.color}",
                                                        bg="yellow",
                                                        width=42, font=100)
                        return False
        return True

    def can_attack(self, board, row1, col1, row2, col2):
        return abs(col1 - col2) <= 1 and abs(row1 - row2) <= 1


class Pawn(Shape):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first_hod = False

    def check_hod(self, board, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            transform_help_label.config(text=f"Ошибка: одна и тажа клетка, ходит: {board.color}",
                                        bg="yellow",
                                        width=36, font=100)
            return False
        if abs(row1 - row2) > 1 or abs(col1 - col2) > 1 and abs(row1 - row2) != 0:
            transform_help_label.config(text=f"Ошибка: пешка так не ходит, ходит: {board.color}",
                                        bg="yellow",
                                        width=35, font=100)
            return False
        if self.first_hod and abs(col1 - col2) > 1:  # на две нельзя если не первый ход
            transform_help_label.config(text=f"Ошибка: нельзя на 2 если не первый ход, Ходит: {board.color}",
                                        bg="yellow",
                                        width=46, font=100)
            return False
        if col2 == col1 and abs(row1 - row2) >= 1:  # право лево нельзя
            transform_help_label.config(text=f"Ошибка: просто так лево право, Ходит: {board.color}",
                                        bg="yellow",
                                        width=46, font=100)
            return False
        if board.field[row1][col1].color == BLACK and col2 > col1:  # назад черный
            transform_help_label.config(text=f"Ошибка: черная пешка ушла назад, Ходит: {board.color}",
                                        bg="yellow",
                                        width=46, font=100)
            return False
        if board.field[row1][col1].color == WHITE and col1 > col2:  # назад белый
            transform_help_label.config(text=f"Ошибка: белая пешка ушла назад, Ходит: {board.color}",
                                        bg="yellow",
                                        width=41, font=100)
            return False
        if abs(col1 - col2) > 2 and not self.first_hod:  # изначально больше двух
            transform_help_label.config(text=f"Ошибка: больше двух изначально, Ходит: {board.color}",
                                        bg="yellow",
                                        width=41, font=100)
            return False
        if row1 != row2:  # пытается съесть пустоту
            if board.field[row2][col2] is None:
                transform_help_label.config(text=f"Ошибка: есть нечего, Ходит: {board.color}",
                                            bg="yellow",
                                            width=30, font=100)
                return False
        if not board.field[row2][col2] is None and row1 == row2:  # съесть
            transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                        bg="yellow",
                                        width=46, font=100)
            return False
        if not self.team_eating(board, row1, col1, row2, col2):  # проверка на конечную позицию
            return False
        if not self.first_hod:
            if row2 == row1 and abs(col2 - col1) == 2:
                if not board.field[row1][min(col1, col2) + 1] is None:
                    transform_help_label.config(text=f"Ошибка: нельзя пройти сквозь фигуру!!! Ходит: {board.color}",
                                                bg="yellow",
                                                width=46, font=100)
                    return False
        return self.check_chax_in_hod(board, row1, col1, row2, col2)

    def can_attack(self, board, row1, col1, row2, col2):
        if board.field[row1][col1].color == WHITE:
            return row1 + 1 == row2 and col1 + 1 == col2 or row1 - 1 == row2 and col1 + 1 == col2
        if board.field[row1][col1].color == BLACK:
            return row1 + 1 == row2 and col1 - 1 == col2 or row1 - 1 == row2 and col1 - 1 == col2


board = Board()


def create_cells():
    for x in range(20, 820, 200):
        for y in range(0, 800, 200):
            canvas.create_rectangle((x, y), (x + 100, y + 100), fill="white")
            canvas.create_rectangle((x + 100, y), (x + 200, y + 100), fill="#64400F")
            canvas.create_rectangle((x + 100, y + 100), (x + 200, y + 200), fill="white")
            canvas.create_rectangle((x, y + 100), (x + 100, y + 200), fill="#64400F")
    for x in range(20, 820, 100):
        for y in range(0, 800, 100):
            if x == 20:
                canvas.create_image(70, 810, image=zero_image)
            if x == 120:
                canvas.create_image(170, 810, image=first_image)
            if x == 220:
                canvas.create_image(270, 810, image=second_image)
            if x == 320:
                canvas.create_image(370, 810, image=third_image)
            if x == 420:
                canvas.create_image(470, 810, image=four_image)
            if x == 520:
                canvas.create_image(570, 810, image=fifth_image)
            if x == 620:
                canvas.create_image(670, 810, image=six_image)
            if x == 720:
                canvas.create_image(770, 810, image=seven_image)
            if y == 0:
                canvas.create_image(10, 50, image=zero_image)
            if y == 100:
                canvas.create_image(10, 150, image=first_image)
            if y == 200:
                canvas.create_image(10, 250, image=second_image)
            if y == 300:
                canvas.create_image(10, 350, image=third_image)
            if y == 400:
                canvas.create_image(10, 450, image=four_image)
            if y == 500:
                canvas.create_image(10, 550, image=fifth_image)
            if y == 600:
                canvas.create_image(10, 650, image=six_image)
            if y == 700:
                canvas.create_image(10, 750, image=seven_image)


def create_update_field():
    i_koord = -1
    for i in range(20, 820, 100):
        i_koord += 1
        j_koord = -1
        for j in range(0, 800, 100):
            j_koord += 1
            update_field(i, j, i_koord, j_koord)


def update_field(i, j, i_koord, j_koord):
    """если board.pole[i_koord][j_koord] not NONE то нарисовать и узнать к какому экземпляру относятся и цвет"""
    if isinstance(board.field[i_koord][j_koord], Officer):
        if board.field[i_koord][j_koord].color == BLACK:
            canvas.create_image(i + 50, j + 54, image=black_officer_image)
        else:
            canvas.create_image(i + 50, j + 55, image=white_officer_image)
    if isinstance(board.field[i_koord][j_koord], Knight):
        if board.field[i_koord][j_koord].color == BLACK:
            canvas.create_image(i + 50, j + 55, image=black_knight_image)
        else:
            canvas.create_image(i + 50, j + 55, image=white_knight_image)
    if isinstance(board.field[i_koord][j_koord], Rook):
        if board.field[i_koord][j_koord].color == BLACK:
            canvas.create_image(i + 50, j + 55, image=black_rook_image)
        else:
            canvas.create_image(i + 50, j + 55, image=white_rook_image)
    if isinstance(board.field[i_koord][j_koord], King):
        if board.field[i_koord][j_koord].color == BLACK:
            canvas.create_image(i + 50, j + 50, image=black_king_image)
        else:
            canvas.create_image(i + 50, j + 50, image=white_king_image)
    if isinstance(board.field[i_koord][j_koord], Queen):
        if board.field[i_koord][j_koord].color == BLACK:
            canvas.create_image(i + 50, j + 50, image=black_queen_image)
        else:
            canvas.create_image(i + 50, j + 50, image=white_queen_image)
    if isinstance(board.field[i_koord][j_koord], Pawn):
        if board.field[i_koord][j_koord].color == BLACK:
            canvas.create_image(i + 50, j + 55, image=black_pawn_image)
        else:
            canvas.create_image(i + 50, j + 55, image=white_pawn_image)


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=820, width=820)
hod_button = tkinter.Button(fg="white", text="Сходить", bg="blue", command=board.main, width=19,
                            font=("Times New Roman", 12, "bold"))
hod_input = tkinter.Entry(bg="violet", width=30)
transform_help_label = tkinter.Label(bg="yellow", width=25, font=100)
help_first_label = tkinter.Button(
    text="Чтобы сходить введите старые а затем новые координаты фигуры, затем клацните на сходить",
    font=5, bg="green", width=90)
help_second_label = tkinter.Button(
    text="Сначала в розовом прямоугольнике указывается номер по столбцу, затем по строке",
    font=13, bg="orange", width=90)
game_over_label = tkinter.Button(text="Лан, я задолбался воевать, гоу мир :)", command=board.game_over_click,
                                 bg="violet",
                                 font=13, width=90)
"""загрузка картинок черных фигур"""
black_officer_image = tkinter.PhotoImage(file="black_officer_image.png")
black_king_image = tkinter.PhotoImage(file="black_king_image.png")
black_queen_image = tkinter.PhotoImage(file="black_queen_image.png")
black_knight_image = tkinter.PhotoImage(file="black_knight_image.png")
black_rook_image = tkinter.PhotoImage(file="black_rook_image.png")
black_pawn_image = tkinter.PhotoImage(file="black_pawn_image.png")

"""загрузка картинок белых фигур"""
white_officer_image = tkinter.PhotoImage(file="white_officer_image.png")
white_king_image = tkinter.PhotoImage(file="white_king_image.png")
white_queen_image = tkinter.PhotoImage(file="white_queen_image.png")
white_knight_image = tkinter.PhotoImage(file="white_knight_image.png")
white_rook_image = tkinter.PhotoImage(file="white_rook_image.png")
white_pawn_image = tkinter.PhotoImage(file="white_pawn_image.png")

"""загрузка цифер для полей"""
zero_image = tkinter.PhotoImage(file="zero_image.png")
first_image = tkinter.PhotoImage(file="one_image.png")
second_image = tkinter.PhotoImage(file="two_image.png")
third_image = tkinter.PhotoImage(file="three_image.png")
four_image = tkinter.PhotoImage(file="four_image.png")
fifth_image = tkinter.PhotoImage(file="five_image.png")
six_image = tkinter.PhotoImage(file="six_image.png")
seven_image = tkinter.PhotoImage(file="seven_image.png")

create_cells()
board.main()
hod_button.pack()
hod_input.pack()
transform_help_label.pack()
canvas.pack()
help_first_label.pack()
help_second_label.pack()
game_over_label.pack()
master.mainloop()
