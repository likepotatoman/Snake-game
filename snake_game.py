# Throw this code into Pyxel Studio or go to this link https://www.pyxelstudio.net/ps/9atxc3mp
import pyxel
import random

pyxel.init(128,128, title = "SNAKE GAME")

class Snake:
    def __init__(self):
        self.body = [(16, 64), (24, 64), (32, 64), (40, 64)]
        self.direction  = 0 #up to 3, 0 being looking right and rotating in the trigonometric direction
    
    def change_direction(self, target_direction):
        if self.direction == 0 and target_direction != 2:
            self.direction = target_direction
        if self.direction == 1 and target_direction != 3:
            self.direction = target_direction
        if self.direction == 2 and target_direction != 0:
            self.direction = target_direction
        if self.direction == 3 and target_direction != 1:
            self.direction = target_direction
    
    def next_block(self):
        if self.direction == 0:
            return (self.body[-1][0] + 8, self.body[-1][1])
        if self.direction == 1:
            return (self.body[-1][0], self.body[-1][1] - 8)
        if self.direction == 2:
            return (self.body[-1][0] - 8, self.body[-1][1])
        if self.direction == 3:
            return (self.body[-1][0], self.body[-1][1] + 8)
    
    def move(self):
        self.body.pop(0)
        if self.direction == 0:
            self.body.append((self.body[-1][0] + 8, self.body[-1][1]))
        if self.direction == 1:
            self.body.append((self.body[-1][0], self.body[-1][1] - 8))
        if self.direction == 2:
            self.body.append((self.body[-1][0] - 8, self.body[-1][1]))
        if self.direction == 3:
            self.body.append((self.body[-1][0], self.body[-1][1] + 8))
    
    def eat(self):
        if self.direction == 0:
            self.body.append((self.body[-1][0] + 8, self.body[-1][1]))
        if self.direction == 1:
            self.body.append((self.body[-1][0], self.body[-1][1] - 8))
        if self.direction == 2:
            self.body.append((self.body[-1][0] - 8, self.body[-1][1]))
        if self.direction == 3:
            self.body.append((self.body[-1][0], self.body[-1][1] + 8))


class Apples:
    def __init__(self, n):
        self.position = set()
        for i in range(n):
            added = False
            while added == False:
                random_x = random.randint(1,15)
                random_y = random.randint(1,15)
                if (random_x * 8, random_y * 8) not in snake.body and (random_x * 8, random_y * 8) not in self.position and (random_x * 8, random_y * 8) not in outside_walls:
                    self.position.add((random_x * 8, random_y * 8))
                    added = True

    def eaten(self, eaten_apple_position):
        self.position.remove(eaten_apple_position)
        added = False
        while added == False:
            random_x = random.randint(1,15)
            random_y = random.randint(1,15)
            if (random_x * 8, random_y * 8) not in snake.body and (random_x * 8, random_y * 8) not in self.position and (random_x * 8, random_y * 8) not in outside_walls:
                self.position.add((random_x * 8, random_y * 8))
                added = True

outside_walls = set()
for i in range(0, 128, 8):
        outside_walls.add((0, i))
        outside_walls.add((120, i))
for i in range(0, 128, 8):
        outside_walls.add((i, 0))
        outside_walls.add((i, 120))

snake = Snake()
apples = Apples(3) #change here to have more or less apples 
target_direction = None

def update():
    global snake, apples, outside_walls, target_direction
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    
    
    if pyxel.btnp(pyxel.KEY_D):
        target_direction = 0
    elif pyxel.btnp(pyxel.KEY_W):
        target_direction = 1
    elif pyxel.btnp(pyxel.KEY_A):
        target_direction = 2
    elif pyxel.btnp(pyxel.KEY_S):
        target_direction = 3
    

    if pyxel.frame_count % 5 == 0: #change here to speed up or slow down the snake
        if target_direction != None:
            snake.change_direction(target_direction)
            target_direction = None
        if snake.next_block() in snake.body or snake.next_block() in outside_walls:
            print("game over")
            pyxel.quit()
        elif snake.next_block() in apples.position:
            apples.eaten(snake.next_block())
            snake.eat()
        else:
            snake.move()

def draw():
    global snake, apples, outside_walls
    pyxel.cls(0)
    
    wall_positions = list(outside_walls)
    for block in wall_positions:
        pyxel.rect(block[0], block[1], 8, 8, 13)
    
    body_position = snake.body
    for block in body_position:
        pyxel.rect(block[0], block[1], 8, 8, 5)
    
    apple_positions = list(apples.position)
    for block in apple_positions:
        pyxel.rect(block[0], block[1], 8, 8, 8)
    
    if len(snake.body) == 196 :
        print("Bro absolutely try harded snake game")
        pyxel.rect(0, 0, 128, 128, 10)
    
pyxel.run(update, draw)
