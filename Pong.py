import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1020,400))
clock = pygame.time.Clock()
running = True

def initialise():

    global ball_list

    ball_list = pygame.sprite.Group()

    ball_list.add(Ball())

    left_score = 0
    right_score = 0

    score_init()

def draw_background():
    Black_colour = ("#000000")

    screen.fill(Black_colour)

    White_colour = ("#FFFFFF")

    width = 2
    x = 0 
    while x < 720:
        pygame.draw.rect(screen, White_colour, pygame.Rect((1020+width)/2, x, width, 10))
        x += 20

def score_init():
    WHITE = (255,255,255)

    number_font = pygame.font.SysFont(None, 60, bold=True)

    global left_score
    global right_score
    global left_number_image
    global right_number_image

    left_score = 0
    right_score = 0

    left_number_text = str(left_score)
    right_number_text = str(right_score)

    left_number_image = number_font.render(left_number_text, True, WHITE)
    right_number_image = number_font.render(right_number_text, True, WHITE)


def score_increment(side):
    WHITE = (255,255,255)

    number_font = pygame.font.SysFont(None, 60, bold=True)

    global left_score
    global right_score
    global left_number_image
    global right_number_image

    if side == "left":
        left_score += 1
    elif side == "right":
        right_score += 1
    else:
        raise ValueError("your side is wrong")

    left_number_text = str(left_score)
    right_number_text = str(right_score)

    left_number_image = number_font.render(left_number_text, True, WHITE)
    right_number_image = number_font.render(right_number_text, True, WHITE)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.velocity = [4,-3]
        self.position = [360, 200]
        self.image = pygame.Surface((20,20))
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        if self.position[1] <= 10 or self.position[1] >= 390:
            self.velocity[1] = -self.velocity[1]
        if self.position[0] <= 10:
            score_increment("right")
            self.position = [510, 200]
            self.velocity[0] = random.randint(-5,-2) - random.random()
            self.velocity[1] = random.randint(-5,-2) - random.random()
        elif self.position[0] >= 1010:
            score_increment("left")
            self.position = [510, 200]
            self.velocity[0] = random.randint(2,5) + random.random()
            self.velocity[1] = random.randint(2,5) + random.random()

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        pygame.draw.circle(screen, ("#FFFFFF"), self.position, 10)

        self.rect = self.image.get_rect()

class Bat(pygame.sprite.Sprite):
    def __init__(self, side):
        self.side = side
        if self.side == "left":
            self.xcoord = 50
        elif self.side == "right":
            self.xcoord = 1020 - 50
        self.ycoord = 175

    def move():
        if self.side == "left":
            pass
        elif self.side == "right":
            pass

initialise()

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    draw_background()

    ball_list.update() 

    screen.blit(left_number_image, (250,50))
    screen.blit(right_number_image, (750,50))  

    pygame.display.flip()

    clock.tick(60)

pygame.quit()