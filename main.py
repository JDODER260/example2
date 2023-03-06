import os
import sys
import random
from termcolor import colored
import logging
from rich.logging import RichHandler
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True)]
)
log = logging.getLogger("rich")


#!!!!!!!!!!!!!!!!!!!!!!NOTE blue = BLUE AND red = RED!!!!!!!!!!!!!!!!!!!!!!!!
print("Hello an welcome to the chess game!")
print("This game does not have the folowing")
print("Casaling:")
print("En Pasant:")
print("Ai might give you his king!")
print("Thanks for playing enjoy!!")
input("Press ENTER to play:")
question = input("Do you want to input your moves with two inputs(example)\nWhich piece do you want to move?:e2\nWhere do you want to move?:e4\nYes\nOr do you want to enter the coordinants in one form for example:e2e4?\nNo\nY/N:")
if question == "y" or question == "Y":
    question = True
elif question == 'n' or question == "N":
    question = False
else:
    question = True

dumb = input("Do you want to play easy or Hard?\nE/H:")
if dumb == "e" or dumb == "E" or dumb == "Easy" or dumb == "easy":
    dumb = True
elif dumb == 'h' or dumb == "H" or dumb == "hard" or dumb == "Hard":
    dumb = False
else:
    dumb = True

rr = colored('♜', 'red')
br = colored('♖', 'blue')
rp = colored('♟', 'red')
bp = colored('♙', 'blue')
bk = colored('♔', 'blue')
rk = colored('♚', 'red')
rq = colored('♛', 'red')
bq = colored('♕', 'blue')
bb = colored('♗', 'blue')
rb = colored('♝', 'red')
bn = colored('♘', 'blue')
rn = colored('♞', 'red')
blank = colored('-', 'green')
board_coords = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7',
                'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
blue_captures = []
red_captures = []


blue_piece = [br, bb, bn, bq, bk, bp]
red_piece = [rr, rb, rn, rq, rk, rp]
count = 0
count_time = 0


class Board():
    def __init__(self):
        self.coords = []
        self.blue_board = []
        self.red_board = []
        for i in range(8):
            self.coords.append([])
            self.coords[i] = [colored('-', 'green')] * 8
        self.coords[0] = [br, bn, bb, bq, bk, bb, bn, br]
        self.coords[1] = [bp, bp, bp, bp, bp, bp, bp, bp]
        self.coords[6] = [rp, rp, rp, rp, rp, rp, rp, rp]
        self.coords[7] = [rr, rn, rb, rq, rk, rb, rn, rr]

    def move(self, from_x, from_y, to_x, to_y):
        self.coords[to_y][to_x] = self.coords[from_y][from_x]
        self.coords[from_y][from_x] = blank

    def display_board(self):
        display = []
        for i in range(9):
            display.append([])
            display[i] = [colored('-', 'green')] * 8
        display[0] = ' '.join(['1'] + self.coords[0])
        display[1] = ' '.join(['2'] + self.coords[1])
        display[2] = ' '.join(['3'] + self.coords[2])
        display[3] = ' '.join(['4'] + self.coords[3])
        display[4] = ' '.join(['5'] + self.coords[4])
        display[5] = ' '.join(['6'] + self.coords[5])
        display[6] = ' '.join(['7'] + self.coords[6])
        display[7] = ' '.join(['8'] + self.coords[7])
        display[8] = ' '.join([' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        self.red_board = [display[0], display[1], display[2], display[3],
                          display[4], display[5], display[6], display[7], display[8]]
        self.blue_board = [display[7], display[6], display[5], display[4],
                           display[3], display[2], display[1], display[0], display[8]]

    def copy_from(self, other_board):
        for y in range(8):
            for x in range(8):
                self.coords[y][x] = other_board.coords[y][x]


board = Board()
pre_board = Board()


# ----------------------------------------------------------------


def display_all_valid_moves():
    moves = []
    for coords_from in board_coords:
        from_x = coords_from[0]
        from_y = coords_from[1]
        from_x = ord(from_x)
        from_y = int(from_y)-1
        from_x = from_x - 97
        for coords_to in board_coords:
            to_x = coords_to[0]
            to_y = coords_to[1]
            to_x = ord(to_x)
            to_y = int(to_y)-1
            to_x = to_x - 97
            if if_valid_move_no_visible_errors_with_red(from_x, from_y, to_x, to_y):
                moves.append({"from": coords_from, "to": coords_to})
    print("Your avalable moves are...")
    for x in moves:
        x_one = x["from"]
        x_two = x["to"]
        print(f"{x_one} to {x_two}: ")


def validate_user_input(piece_from, piece_to):
    if len(piece_from) > 2 or len(piece_to) > 2:
        return False
    try:
        from_y = piece_from[0]
        from_y = ord(from_y) - 97
        from_y = int(piece_from[1])
    except:
        log.warning("That was an invalid input.")
    else:
        return True


def is_rook(piece):
    if piece == br or piece == rr:
        return True
    else:
        return False


def is_bishop(piece):
    if piece == bb or piece == rb:
        return True
    else:
        return False


def is_knight(piece):
    if piece == bn or piece == rn:
        return True
    else:
        return False


def is_queen(piece):
    if piece == rq or piece == bq:
        return True
    else:
        return False


def is_king(piece):
    if piece == bk or piece == rk:
        return True
    else:
        return False


def is_blue_piece(piece):
    for x in blue_piece:
        if x == piece:
            return True
    return False


def is_red_piece(piece):
    for x in red_piece:
        if x == piece:
            return True
    return False


def is_jumping_rook(from_x, from_y, to_x, to_y):
    x_dir = 1 if to_x > from_x else -1
    y_dir = 1 if to_y > from_y else -1
    x_delta = abs(from_x - to_x)
    y_delta = abs(from_y - to_y)
    if x_delta == 0:
        for y in range(1, y_delta):
            y = from_y + y * y_dir
            pos = board.coords[y][from_x]
            if pos != blank:
                return True
        return False
    elif y_delta == 0:
        for x in range(1, x_delta):
            x = from_x + x * x_dir
            pos = board.coords[from_y][x]
            if pos != blank:
                return True
        return False
    else:
        return False


def is_jumping_pawn(place_from, from_x, from_y):
    if place_from == rp or place_from == bp:
        if from_y == 6:
            pos_mid = board.coords[from_y-1][from_x]
            if pos_mid != blank:
                return False
            return True
        if from_y == 1:
            pos_mid = board.coords[from_y+1][from_x]
            if pos_mid != blank:
                return False
            return True


def is_jumping_bishop(from_x, from_y, to_x, to_y):
    x_dir = 1 if to_x > from_x else -1
    y_dir = 1 if to_y > from_y else -1
    x_delta = to_x - from_x
    y_delta = to_y - from_y
    if abs(x_delta) == abs(y_delta):
        pass
    else:
        return False
    for i in range(1, abs(x_delta)):
        x = from_x + i * x_dir
        y = from_y + i * y_dir
        pos = board.coords[y][x]
        if pos != blank:
            return False
        else:
            pass
    return True


def has_captured_king(piece):
    board.display_board()
    if piece == bk:
        log.info("Red won!")
        for x in board.red_board:
            print(x)
        print(f"red captures: {len(red_captures)}")
        print(' '.join(red_captures))
        print(f"blue captures: {len(blue_captures)}")
        print(' '.join(blue_captures))
        sys.exit()
    if piece == rk:
        log.info("Blue won!")
        for x in board.blue_board:
            print(x)
        print(f"red captures: {len(red_captures)}")
        print(' '.join(red_captures))
        print(f"blue captures: {len(blue_captures)}")
        print(' '.join(blue_captures))
        sys.exit()


def is_valid_pawn_move(place_from, place_to, from_x, from_y, to_x, to_y):
    if place_from == rp or place_from == bp:
        if place_to != blank:
            if place_from == rp:
                if abs(from_x - to_x) == 1 and from_y - to_y == 1:
                    return True
            if place_from == bp:
                if abs(from_x - to_x) == 1 and from_y - to_y == -1:
                    return True
        if place_to == blank:
            if from_y == 6 or from_y == 1:
                if place_from == rp:
                    if from_x == to_x and from_y == to_y+2:
                        if is_jumping_pawn(place_from, from_x, from_y) != True:
                            return False
                        return True
                    if from_x == to_x and from_y == to_y+1:
                        return True
                    else:
                        return False
                elif place_from == bp:
                    if from_x == to_x and from_y == to_y-2:
                        if is_jumping_pawn(place_from, from_x, from_y) != True:
                            return False
                        return True
                    if from_x == to_x and from_y == to_y-1:
                        return True
                    else:
                        return False
            else:
                if place_from == rp:
                    if from_x == to_x and from_y == to_y+1:
                        return True
                    else:
                        return False
                elif place_from == bp:
                    if from_x == to_x and from_y == to_y-1:
                        return True
                    else:
                        return False
        else:
            return False
    else:
        return True


def is_valid_king_move(piece, from_x, from_y, to_x, to_y):
    if is_king(piece):
        if abs(from_x - to_x) == 1 or from_x - to_x == 0:
            if abs(from_y - to_y) == 1 or from_y - to_y == 0:
                return True
        return False
    else:
        return True


def is_valid_rook_move(place_from, from_x, from_y, to_x, to_y):
    if is_rook(place_from):
        if from_y == to_y or from_x == to_x:
            if is_jumping_rook(from_x, from_y, to_x, to_y):
                return False
            return True
        else:
            return False
    else:
        return True


def is_valid_bishop_move(place_from, from_x, from_y, to_x, to_y):
    if is_bishop(place_from):
        count = 18
        for x in range(count):
            if abs(from_x - to_x) == x and abs(from_y - to_y) == x:
                if is_jumping_bishop(from_x, from_y, to_x, to_y) != True:
                    return False
                else:
                    return True
    else:
        return True


def is_valid_knight_move(place_from, from_x, from_y, to_x, to_y):
    if is_knight(place_from):
        if abs(from_x - to_x) == 2 or abs(from_y - to_y) == 2:
            if abs(from_x - to_x) == 1 or abs(from_y - to_y) == 1:
                return True
        return False
    else:
        return True


def is_valid_queen_move(place_from, from_x, from_y, to_x, to_y):
    if is_queen(place_from):
        if from_y == to_y or from_x == to_x:
            if is_jumping_rook(from_x, from_y, to_x, to_y):
                return False
            else:
                return True
        count = 18
        for step in range(count):
            if abs(from_x - to_x) == step and abs(from_y - to_y) == step:
                if is_jumping_bishop(from_x, from_y, to_x, to_y) != True:
                    return False
                else:
                    return True
        return False
    else:
        return True


def blank_check(piece):
    if piece == blank:
        return False
    else:
        return True


def is_valid_move_for_red(place_from, place_to):
    if is_red_piece(place_to) != True and is_red_piece(place_from):
        return True
    return False


def is_valid_move_for_blue(place_from, place_to):
    if is_blue_piece(place_to) != True and is_blue_piece(place_from):
        return True
    return False


def is_not_same_place(place_from, place_to):
    if place_from == place_to:
        return False
    else:
        return True


def will_be_in_check():
    for coords_from in board_coords:
        from_x = coords_from[0]
        from_y = coords_from[1]
        from_x = ord(from_x)
        from_y = int(from_y)-1
        from_x = from_x - 97
        for coords_to in board_coords:
            to_x = coords_to[0]
            to_y = coords_to[1]
            to_x = ord(to_x)
            to_y = int(to_y)-1
            to_x = to_x - 97
            pos = pre_board.coords[to_y][to_x]
            if if_valid_move_no_visible_errors_without_check(from_x, from_y, to_x, to_y):
                if is_king(pos):
                    pre_board.copy_from(board)
                    return True
    pre_board.copy_from(board)
    return False


def is_in_check():
    for coords_from in board_coords:
        from_x = coords_from[0]
        from_y = coords_from[1]
        from_x = ord(from_x)
        from_y = int(from_y)-1
        from_x = from_x - 97
        for coords_to in board_coords:
            to_x = coords_to[0]
            to_y = coords_to[1]
            to_x = ord(to_x)
            to_y = int(to_y)-1
            to_x = to_x - 97
            pos = board.coords[to_y][to_x]
            if if_valid_move_no_visible_errors_without_check(from_x, from_y, to_x, to_y):
                if is_king(pos):
                    return True
    return False


def is_not_stupid():
    for coords_from in board_coords:
        from_x = coords_from[0]
        from_y = coords_from[1]
        from_x = ord(from_x)
        from_y = int(from_y)-1
        from_x = from_x - 97
        for coords_to in board_coords:
            to_x = coords_to[0]
            to_y = coords_to[1]
            to_x = ord(to_x)
            to_y = int(to_y)-1
            to_x = to_x - 97
            pos = pre_board.coords[to_y][to_x]
            if if_valid_move_no_visible_errors_with_red(from_x, from_y, to_x, to_y):
                if pos != blank:
                    pre_board.copy_from(board)
                    return False
    pre_board.copy_from(board)
    return True


def if_valid_move_no_visible_errors_without_check(from_x, from_y, to_x, to_y):
    place_to = board.coords[to_y][to_x]
    place_from = board.coords[from_y][from_x]
    if is_not_same_place(place_from, place_to) != True:
        return False
    if blank_check(place_from) == False:
        return False
    if is_valid_move_for_red(place_from, place_to) != True:
        return False
    if is_valid_queen_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_knight_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_bishop_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_rook_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_king_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_pawn_move(place_from, place_to, from_x, from_y, to_x, to_y) != True:
        return False
    return True


def if_valid_move_no_visible_errors_with_red(from_x, from_y, to_x, to_y):
    place_to = board.coords[to_y][to_x]
    place_from = board.coords[from_y][from_x]
    if is_not_same_place(place_from, place_to) != True:
        return False
    if blank_check(place_from) == False:
        return False
    if is_valid_move_for_blue(place_from, place_to) != True:
        return False
    if is_valid_queen_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_knight_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_bishop_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_rook_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_king_move(place_from, from_x, from_y, to_x, to_y) != True:
        return False
    if is_valid_pawn_move(place_from, place_to, from_x, from_y, to_x, to_y) != True:
        return False
    return True


def brain():
    global count, count_time
    count += 1
    turn = "red"
    random.shuffle(board_coords)
    random.shuffle(board_coords)
    while is_in_check():
        for piece_from in board_coords:
            for piece_to in board_coords:
                to_x = piece_to[0]
                to_y = piece_to[1]
                to_x = ord(to_x)
                to_y = int(to_y)-1
                to_x = to_x - 97
                from_x = piece_from[0]
                from_y = piece_from[1]
                from_x = ord(from_x)
                from_y = int(from_y)-1
                from_x = from_x - 97
                pos_to = board.coords[to_y][to_x]
                pos_from = board.coords[from_y][from_x]
                if if_valid_move_no_visible_errors_without_check(from_x, from_y, to_x, to_y):
                    if pos_to != blank:
                        pre_board.move(from_x, from_y, to_x, to_y)
                        if is_king(pos_from):
                            pre_board.move(from_x, from_y, to_x, to_y)
                            if will_be_in_check():
                                return False
                            pre_board.copy_from(board)
    for piece_from in board_coords:
        for piece_to in board_coords:
            to_x = piece_to[0]
            to_y = piece_to[1]
            to_x = ord(to_x)
            to_y = int(to_y)-1
            to_x = to_x - 97
            from_x = piece_from[0]
            from_y = piece_from[1]
            from_x = ord(from_x)
            from_y = int(from_y)-1
            from_x = from_x - 97
            pos_to = board.coords[to_y][to_x]
            pos_from = board.coords[from_y][from_x]
            if if_valid_move_no_visible_errors_without_check(from_x, from_y, to_x, to_y):
                if pos_to != blank:
                    pre_board.move(from_x, from_y, to_x, to_y)
                    if is_king(pos_from):
                        pre_board.move(from_x, from_y, to_x, to_y)
                        if will_be_in_check():
                            return False
                        pre_board.copy_from(board)
                    pre_board.move(from_x, from_y, to_x, to_y)
                    if is_not_stupid():
                        return(piece_from, piece_to, turn)
    for piece_from in board_coords:
        for piece_to in board_coords:
            to_x = piece_to[0]
            to_y = piece_to[1]
            to_x = ord(to_x)
            to_y = int(to_y)-1
            to_x = to_x - 97
            from_x = piece_from[0]
            from_y = piece_from[1]
            from_x = ord(from_x)
            from_y = int(from_y)-1
            from_x = from_x - 97
            pos_from = board.coords[from_y][from_x]
            if if_valid_move_no_visible_errors_without_check(from_x, from_y, to_x, to_y):
                pre_board.move(from_x, from_y, to_x, to_y)
                if is_king(pos_from):
                    pre_board.move(from_x, from_y, to_x, to_y)
                    if will_be_in_check():
                        return False
                    pre_board.copy_from(board)
                return(piece_from, piece_to, turn)


def brain_dumb():
    global count, count_time
    count += 1
    turn = "red"
    random.shuffle(board_coords)
    random.shuffle(board_coords)
    for piece_from in board_coords:
        for piece_to in board_coords:
            to_x = piece_to[0]
            to_y = piece_to[1]
            to_x = ord(to_x)
            to_y = int(to_y)-1
            to_x = to_x - 97
            from_x = piece_from[0]
            from_y = piece_from[1]
            from_x = ord(from_x)
            from_y = int(from_y)-1
            from_x = from_x - 97
            pos_to = board.coords[to_y][to_x]
            pos_from = board.coords[from_y][from_x]
            if if_valid_move_no_visible_errors_without_check(from_x, from_y, to_x, to_y):
                if pos_to != blank:
                    pre_board.move(from_x, from_y, to_x, to_y)
                    if is_king(pos_from):
                        pre_board.move(from_x, from_y, to_x, to_y)
                        if will_be_in_check():
                            return(piece_from, piece_to, turn)
                        pre_board.copy_from(board)
                    return(piece_from, piece_to, turn)
    for piece_from in board_coords:
        for piece_to in board_coords:
            to_x = piece_to[0]
            to_y = piece_to[1]
            to_x = ord(to_x)
            to_y = int(to_y)-1
            to_x = to_x - 97
            from_x = piece_from[0]
            from_y = piece_from[1]
            from_x = ord(from_x)
            from_y = int(from_y)-1
            from_x = from_x - 97
            pos_from = board.coords[from_y][from_x]
            if if_valid_move_no_visible_errors_without_check(from_x, from_y, to_x, to_y):
                return(piece_from, piece_to, turn)


def move_piece(pos_from, pos_to, turn):
    global blank, blue_captures, red_captures, pre_board
    if validate_user_input(pos_from, pos_to) != True:
        print("Invalid User Input")
        return False
    from_x = pos_from[0]
    from_y = pos_from[1]
    from_x = ord(from_x[0])
    from_y = int(from_y)-1
    from_x = from_x - 97
    to_x = pos_to[0]
    to_y = pos_to[1]
    to_x = ord(to_x)
    to_y = int(to_y)-1
    to_x = to_x - 97
    place_to = board.coords[to_y][to_x]
    place_from = board.coords[from_y][from_x]
    if is_not_same_place(place_from, place_to) != True:
        log.warning("That was an invalid move. It was the same place!")
        return False
    if blank_check(place_from) == False:
        log.warning("That was a blank place")
        return False
    if is_valid_queen_move(place_from, from_x, from_y, to_x, to_y) != True:
        log.warning(
            "That was an invalid move. You cant move your Queen Like that!")
        return False
    if is_valid_knight_move(place_from, from_x, from_y, to_x, to_y) != True:
        log.warning(
            "That was an invalid move. You cant move your Knights Like that!")
        return False
    if is_valid_bishop_move(place_from, from_x, from_y, to_x, to_y) != True:
        log.warning(
            "That was an invalid move, You cant move your bishop Like that!")
        return False
    if is_valid_rook_move(place_from, from_x, from_y, to_x, to_y) != True:
        log.warning(
            "That was an invalid move. You cant move your rook Like that!")
        return False
    if is_valid_king_move(place_from, from_x, from_y, to_x, to_y) != True:
        log.warning(
            "That was a invalid move. You can't move your king Like that!")
        return False
    if is_valid_pawn_move(place_from, place_to, from_x, from_y, to_x, to_y) != True:
        print('invalid_move')
        return False
    if turn == "red":
        if is_valid_move_for_red(place_from, place_to) != True:
            log.warning("That was an invalid move for red!")
            return False
    if turn == "blue":
        if is_valid_move_for_blue(place_from, place_to) != True:
            log.warning("That was an invalid move for blue!")
            return False
    if is_king(place_from):
        pre_board.move(from_x, from_y, to_x, to_y)
        if will_be_in_check():
            print("You can't move there! You would be in check!")
            return False
        pre_board.copy_from(board)
    has_captured_king(place_to)
    if place_to != blank:

        if turn == "red":
            red_captures.append(place_to)
        if turn == "blue":
            if is_valid_move_for_blue(place_from, place_to) != True:
                log.warning("That was an invalid move for blue!")
                return False
            blue_captures.append(place_to)
        print(f"You have captured {place_to}\n")
        # declares after confirmed true
    board.move(from_x, from_y, to_x, to_y)
    pre_board.copy_from(board)
    return True


def red_tern():
    while True:
        if dumb:
            piece_select, piece_move, turn = brain_dumb()
        else:
            piece_select, piece_move, turn = brain()
        if move_piece(piece_select, piece_move, turn):
            break


def blue_tern():
    while True:
        if question:
            piece_select = input("Which piece do you want to move?:")
            piece_move = input("Where do you want to move?:")
            if move_piece(piece_select, piece_move, turn="blue"):
                break
        else:
            both = input("Where do you want to move?:")
            if len(both) != 4:
                print(
                    "You should enter all coordinants ant the same time(example)\nWhere do you want to move?:e2e4")
            else:
                piece_select = both[:2]
                piece_move = both[2:4]
                if move_piece(piece_select, piece_move, turn="blue"):
                    break


while True:
    board.display_board()
    print("________________________________\n")
    print("Blue's Turn")
    print("________________________________")
    print("________________________________")
    for x in board.blue_board:
        print(x)
    blue_tern()
    print("________________________________\n")
    print("Red's Turn")
    print("________________________________\n")
    red_tern()
    print(f"red captures: {len(red_captures)}")
    print(' '.join(red_captures))
    print(f"blue captures: {len(blue_captures)}")
    print(' '.join(blue_captures))
