import os
import pygame
import sys
# import btm.py

pygame.init()
size = width, height = 750, 650
fps = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Guitar hero')
all_sprites = pygame.sprite.Group()
btm_sprites = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('sprites', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Green_btm(pygame.sprite.Sprite):
    green_btm = load_image("G1_1.png", - 1)
    green_btm_active = load_image('G3.png', -1)

    red_btm = load_image('R1.png', -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Green_btm.green_btm
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (75, 75))
        # while True:
        self.rect.x = 125
        self.rect.y = 550
            # if not pygame.sprite.spritecollideany(self, all_sprites):
                # break
    '''
    def update(self):
        # if self.rect.collidepoint(pos):
            # pass
        self.image = Green_btm.green_btm_active
        self.image = pygame.transform.scale(self.image, (50, 50))
    '''

    def back(self):
        self.image = Green_btm.green_btm
        self.image = pygame.transform.scale(self.image, (75, 75))


class Red_btm(pygame.sprite.Sprite):

    red_btm = load_image('R1_1.png', -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Red_btm.red_btm
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (75, 75))
        # while True:
        self.rect.x = 250
        self.rect.y = 550


class Yellow_btm(pygame.sprite.Sprite):

    yellow_btm = load_image('Y1_1.png', -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Yellow_btm.yellow_btm
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (75, 75))
        # while True:
        self.rect.x = 375
        self.rect.y = 550


class Blue_btm(pygame.sprite.Sprite):

    blue_btm = load_image('B1.png', -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Blue_btm.blue_btm
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (75, 75))
        # while True:
        self.rect.x = 510
        self.rect.y = 550

class Green_ball(pygame.sprite.Sprite):

    green_ball = load_image('G2.png', -1)
    fire = load_image('fire.png', -1)

    def __init__(self, y, *group):
        super().__init__(*group)
        self.image = Green_ball.green_ball
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        # while True:
        self.rect.x = 135
        self.rect.y = y
            # if not pygame.sprite.spritecollideany(self, all_sprites):
                # break

    def update(self):
        self.rect = self.rect.move(0, 5)
        if pygame.sprite.spritecollideany(self, btm_sprites) and pygame.key.get_pressed()[pygame.K_1]:
            print('wow')
            self.image = Green_ball.fire
            self.image = pygame.transform.scale(self.image, (50, 50))
    '''
    def boom(self):
        self.image = Green_ball.fire
        self.image = pygame.transform.scale(self.image, (50, 50))
    '''

class Red_ball(pygame.sprite.Sprite):
    red_ball = load_image('R2.png', -1)
    fire = load_image('fire.png', -1)

    def __init__(self, y, *group):
        super().__init__(*group)
        self.image = Red_ball.red_ball
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        # while True:
        self.rect.x = 265
        self.rect.y = y

    def update(self):
        self.rect = self.rect.move(0, 5)
        if pygame.sprite.spritecollideany(self, btm_sprites) and pygame.key.get_pressed()[pygame.K_2]:
            print('wow')
            self.image = Red_ball.fire
            self.image = pygame.transform.scale(self.image, (50, 50))


class Yellow_ball(pygame.sprite.Sprite):
    yellow_ball = load_image('Y2.png', -1)
    fire = load_image('fire.png', -1)

    def __init__(self, y, *group):
        super().__init__(*group)
        self.image = Yellow_ball.yellow_ball
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        # while True:
        self.rect.x = 385
        self.rect.y = y

    def update(self):
        self.rect = self.rect.move(0, 5)
        if pygame.sprite.spritecollideany(self, btm_sprites) and pygame.key.get_pressed()[pygame.K_3]:
            print('wow')
            self.image = Yellow_ball.fire
            self.image = pygame.transform.scale(self.image, (50, 50))


class Blue_ball(pygame.sprite.Sprite):
    blue_ball = load_image('B2.png', -1)
    fire = load_image('fire.png', -1)

    def __init__(self, y, *group):
        super().__init__(*group)
        self.image = Blue_ball.blue_ball
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        # while True:
        self.rect.x = 525
        self.rect.y = y

    def update(self):
        self.rect = self.rect.move(0, 5)
        if pygame.sprite.spritecollideany(self, btm_sprites) and pygame.key.get_pressed()[pygame.K_4]:
            print('wow')
            self.image = Blue_ball.fire
            self.image = pygame.transform.scale(self.image, (50, 50))


class Field():
    def __init__(self):
        self.color_white = pygame.Color('white')
        self.score = 0
        self.believer = pygame.mixer.music
        self.believer.load('Believer.mp3')
        self.believer.set_volume(0.3)
        self.play_music = 0

        # линии
        self.line_1 = [(250, 0), (250, 650)]
        self.line_2 = [(325, 0), (325, 650)]
        self.line_3 = [(400, 0), (400, 650)]
        self.line_4 = [(475, 0), (475, 650)]

    def render(self, screen):

        # рендер линий

        pygame.draw.line(screen, self.color_white, self.line_1[0], self.line_1[1], 1)
        pygame.draw.line(screen, self.color_white, self.line_2[0], self.line_2[1], 1)
        pygame.draw.line(screen, self.color_white, self.line_3[0], self.line_3[1], 1)
        pygame.draw.line(screen, self.color_white, self.line_4[0], self.line_4[1], 1)

    def song(self):

        # start

        if self.play_music == 0:
            print('beggin')
            self.believer.play()
            self.play_music = 1

        # pause

        elif self.play_music == 1:
            self.believer.pause()
            self.play_music = 2
            print('pause', self.play_music)

        # continue

        elif self.play_music == 2:
            print('cont')
            self.believer.unpause()
            self.play_music = 1


# btm

green_btm = Green_btm()
green_btm.add(btm_sprites)
red_btm = Red_btm()
red_btm.add(btm_sprites)
yellow_btm = Yellow_btm()
yellow_btm.add(btm_sprites)
blue_btm = Blue_btm()
blue_btm.add(btm_sprites)

# bals
for i in range(7):

    green_ball = Green_ball(-i * 2320 + -1000)
    green_ball.add(all_sprites)
    red_ball = Red_ball(-i * 2320 + -1125)
    red_ball.add(all_sprites)
    yellow_ball = Yellow_ball(-i * 2300 + -1275)
    yellow_ball.add(all_sprites)
    # blue_ball = Blue_ball(-1000)
    # blue_ball.add(all_sprites)

    # 2

    yellow_ball = Yellow_ball(-i * 2320 + -1425)
    yellow_ball.add(all_sprites)
    blue_ball = Blue_ball(-i * 2320 + -1475)
    blue_ball.add(all_sprites)
    yellow_ball = Yellow_ball(-i * 2320 + -1525)
    yellow_ball.add(all_sprites)
    blue_ball = Blue_ball(-i * 2320 + -1575)
    blue_ball.add(all_sprites)

    # 3

    red_ball = Red_ball(-i * 2320 + -1700)
    red_ball.add(all_sprites)
    yellow_ball = Yellow_ball(-i * 2320 + -1825)
    yellow_ball.add(all_sprites)

    # 4

    yellow_ball = Yellow_ball(-i * 2320 + -2050)
    yellow_ball.add(all_sprites)
    blue_ball = Blue_ball(-i * 2320 + -2100)
    blue_ball.add(all_sprites)
    yellow_ball = Yellow_ball(-i * 2320 + -2150)
    yellow_ball.add(all_sprites)
    blue_ball = Blue_ball(-i * 2320 + -2200)
    blue_ball.add(all_sprites)

    # 5

    red_ball = Red_ball(-i * 2320 + -2350)
    red_ball.add(all_sprites)
    yellow_ball = Yellow_ball(-i * 2320 + -2475)
    yellow_ball.add(all_sprites)

    # 6

    yellow_ball = Yellow_ball(-i * 2320 + -2675)
    yellow_ball.add(all_sprites)
    blue_ball = Blue_ball(-i * 2320 + -2725)
    blue_ball.add(all_sprites)
    yellow_ball = Yellow_ball(-i * 2320 + -2775)
    yellow_ball.add(all_sprites)
    blue_ball = Blue_ball(-i * 2320 + -2825)
    blue_ball.add(all_sprites)

    # 7

    red_ball = Red_ball(-i * 2320 + -2925)
    red_ball.add(all_sprites)
    yellow_ball = Yellow_ball(-i * 2320 + -3075)
    yellow_ball.add(all_sprites)


running = True
field = Field()
key = pygame.key.get_pressed()
clock = pygame.time.Clock()
start = 0
a = 0

while running:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if key[pygame.K_LEFT]:
            field.song()
        if key[pygame.K_RIGHT]:
            a += 1
            print(a)
        # if key[pygame.K_1]:
            # a.update()
            # a.back()

    if start < 300:
        print(start)
        start += 1
    elif start == 300:
        print('start')
        field.song()
        start += 1
    screen.fill(pygame.Color("black"))
    all_sprites.update()
    btm_sprites.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
