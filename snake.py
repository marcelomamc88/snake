#1 - colocar uma cobra de lenght 1 na tela
#2 - movimentar a cobra de len 1 na tela
#3 - colar a comida na tela, posição aleatoria
#4 - qunado a cobra passar na comida, reposicionar a comida
#5 - fazer a cobra aumentar o tamanho
#6 - movimentar cada parte do seu corpo relativamente
#7 - ao passar para os extremos da tela, colcar do lado oposto
#8 - se o head passar por parte do corpo da cobra, game over, mostrar na tela
#9 - mostrar a quantidade de pontos

from tkinter import *
import random

root = Tk()
root.title("Snake Marcelo Conceição")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)
canvas = Canvas(root, width=250, height=250, bd=0,highlightthickness=0)
canvas.pack()
root.update()

class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10, 10, fill="green")
        self.move_random()

    def move_random(self):
        rand_x = random.randint(1,self.canvas.winfo_width())
        rand_y = random.randint(1,self.canvas.winfo_height())
        self.canvas.move(self.id, rand_x-self.canvas.coords(self.id)[0],
                         rand_y-self.canvas.coords(self.id)[1])

class Snake:
    def __init__(self, canvas, Food):
        self.pieces = []
        self.canvas = canvas
        self.size = 10
        self.walk = 5
        self.head = self.create_piece(0,0)

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
        self.canvas.bind_all("<KeyPress-Up>", self.move_up)
        self.canvas.bind_all("<KeyPress-Down>", self.move_down)

    def create_piece(self, walk_x, walk_y):
        new_piece = canvas.create_rectangle(0, 0, self.size, self.size, fill="red")
        qty_pieces = len(self.pieces);

        if qty_pieces == 0:
            self.canvas.move(new_piece, random.randint(1, self.canvas.winfo_width()),
                                        random.randint(1, self.canvas.winfo_height()))
        else:
            previous_piece = self.pieces[qty_pieces-1]
            self.canvas.move(new_piece, self.canvas.coords(previous_piece)[0]+walk_x,
                                        self.canvas.coords(previous_piece)[1]+walk_y)

        self.pieces.append(new_piece)

        return new_piece

    def ate(self):
        x = self.canvas.coords(self.head)[0]
        y = self.canvas.coords(self.head)[1]

        if (Food.canvas.coords(Food.id)[0]-x) < 10 and (Food.canvas.coords(Food.id)[0]-x) >= -10:
            if (Food.canvas.coords(Food.id)[1]-y) < 10 and (Food.canvas.coords(Food.id)[1]-y) >= -10:
                self.create_piece(self.size, 0)
                Food.move_random()

    def limit_screen(self):
        if self.canvas.coords(self.head)[0] > self.canvas.winfo_width():
            self.canvas.move(self.head, self.canvas.winfo_width()*-1, 0)
        elif self.canvas.coords(self.head)[0] < 0:
            self.canvas.move(self.head, self.canvas.winfo_width(), 0)
        elif self.canvas.coords(self.head)[1] > self.canvas.winfo_height():
            self.canvas.move(self.head, 0, self.canvas.winfo_height() * -1)
        elif self.canvas.coords(self.head)[1] < 0:
            self.canvas.move(self.head, 0, self.canvas.winfo_height())

    def update_pieces(self):
        self.limit_screen()


        for i in reversed(range(len(self.pieces))):
            if i == 0:
                break

            self.canvas.move(
                    self.pieces[i],
                    self.canvas.coords(self.pieces[i-1])[0]-self.canvas.coords(self.pieces[i])[0],
                    self.canvas.coords(self.pieces[i-1])[1]-self.canvas.coords(self.pieces[i])[1])

    def move_left(self, event):
        self.update_pieces()
        add_x, add_y = self.walk*-1, 0
        self.canvas.move(self.head, add_x, add_y)
        self.ate()

    def move_right(self, event):
        self.update_pieces()
        add_x, add_y = self.walk, 0
        self.canvas.move(self.head, add_x, add_y)
        self.ate()

    def move_up(self, event):
        self.update_pieces()
        add_x, add_y = 0, self.walk*(-1)
        self.canvas.move(self.head, add_x, add_y)
        self.ate()

    def move_down(self, event):
        self.update_pieces()
        add_x, add_y = 0, self.walk
        self.canvas.move(self.head, add_x, add_y)
        self.ate()


Snake = Snake(canvas, Food)
Food = Food(canvas)
root.mainloop()
