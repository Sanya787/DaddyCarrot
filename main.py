import os
import sys

import pygame
first_level = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

second_level = [
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


tile_size = 50
screen_width = 1000
screen_height = 700


def load_image(filename, colorkey=None):
    path = os.path.join('images', filename)
    if not os.path.isfile(path):
        print(f"Файл с изображением '{path}' не найден")
        sys.exit()
    image = pygame.image.load(path)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class Carrot:
    speed = 3

    def __init__(self, x, y):
        self.image = pygame.transform.scale(load_image('carrot.png'), (100, 160))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.delta_y = 0
        self.value_jump = 0
        self.maybe_x = 0
        self.maybe_y = 0

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if self.rect.y - 20 > -35:
                self.rect.y -= 20
        if key[pygame.K_LEFT]:
            self.rect.x -= Carrot.speed
        if key[pygame.K_RIGHT]:
            self.rect.x += Carrot.speed

        self.delta_y += 1
        if self.delta_y > 3:
            self.delta_y = 3
        if self.delta_y + self.rect.y < 480:
            self.rect.y += self.delta_y

        screen.blit(self.image, self.rect)


class World:
    def __init__(self, data):
        self.carrot = Carrot(20, 470)
        self.tile_list = []
        self.back_button = load_image('back.png')
        self.back_button = pygame.transform.scale(self.back_button, (50, 50))
        dirt_img = load_image('dirt.png')
        grass_img = load_image('grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    image = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (image, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    image = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (image, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def update(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        self.carrot.update()
        screen.blit(self.back_button, (0, 0))

    def get_event(self, event):
        global room
        x, y = event.pos
        if event.type == pygame.MOUSEBUTTONUP and 0 < x < 50 and 0 < y < 50:
            room = Menu()


class Menu:
    def __init__(self):
        self.image = load_image('button.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 330

    def update(self):
        screen.blit(self.image, self.rect)

    def get_event(self, event):
        global room
        x, y = event.pos
        if event.type == pygame.MOUSEBUTTONUP and 409 < x < 614 and 338 < y < 397:
            room = World(first_level)


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
room = Menu()


def main():
    running = True

    while running:
        screen.blit(load_image('background.png'), (0, 0))
        # draw_grid()
        room.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                room.get_event(event)
            else:
                room.update()
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
