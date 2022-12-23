import os
import sys

import pygame


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
pay_group = pygame.sprite.Group()


first_level = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 3, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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


class Money(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__(pay_group, all_sprites)
        self.image = image
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


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

    return image


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Carrot(pygame.sprite.Sprite):
    speed = 3
    carrot_image = load_image('carrot.png')

    def __init__(self, x, y):
        super().__init__(player_group, all_sprites)
        self.image = Carrot.carrot_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        global pay_group

        delta_x = 0
        delta_y = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and not self.jumped:
            self.vel_y = -15
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            delta_x -= 5
        if key[pygame.K_RIGHT]:
            delta_x += 5
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        delta_y += self.vel_y

        # self.rect.y += delta_y
        # self.rect.x += delta_x
        self.rect.y += delta_y
        if pygame.sprite.spritecollideany(self, tiles_group):
            self.rect.y -= delta_y

        self.rect.x += delta_x

        if pygame.sprite.spritecollideany(self, tiles_group):
            self.rect.x -= delta_x

        if pygame.sprite.spritecollideany(self, pay_group):
            for elem in pay_group:
                if pygame.Rect.colliderect(elem.rect, self.rect):
                    room.money_up += 1
                    room.text = room.font.render(str(room.money_up), True, (255, 255, 255))
                    elem.kill()

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            delta_y = 0

        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


class World:
    def __init__(self, data):
        self.tile_sprites = pygame.sprite.Group()
        self.carrot = Carrot(60, 470)
        self.tile_list = []
        self.back_button = load_image('back.png')
        self.money_up = 0
        self.back_button = pygame.transform.scale(self.back_button, (50, 50))
        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render("0", True, (255, 255, 255))
        dirt_img = load_image('dirt.png')
        grass_img = load_image('grass.png')
        self.money_img = load_image('money.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    Tile(dirt_img, col_count, row_count)
                    self.tile_list.append(tile)
                elif tile == 2:
                    Tile(grass_img, col_count, row_count)
                    self.tile_list.append(tile)
                elif tile == 3:
                    Money(self.money_img, col_count, row_count)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def update(self, event):
        global room, all_sprites, tiles_group, player_group
        if event.type == pygame.MOUSEBUTTONUP and 0 < event.pos[0] < 50 and 0 < event.pos[1] < 50:
            room = Menu()
            all_sprites = pygame.sprite.Group()
            tiles_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()

        self.carrot.update()

    def draw(self):
        all_sprites.draw(screen)

        screen.blit(pygame.transform.scale(self.money_img, (25, 25)), (953, 2))
        screen.blit(self.text, (980, 0))

        screen.blit(self.back_button, (0, 0))


class Menu:
    def __init__(self):
        self.image = load_image('button.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 330

    def update(self, event):
        global room
        if event.type == pygame.MOUSEBUTTONUP and 409 < event.pos[0] < 614 and 338 < event.pos[1] < 397:
            room = World(first_level)

    def draw(self):
        screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
room = Menu()


def main():
    running = True

    while running:
        screen.blit(load_image('background.png'), (0, 0))
        if isinstance(room, World):
            room.carrot.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            room.update(event)
        # draw_grid()
        room.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
