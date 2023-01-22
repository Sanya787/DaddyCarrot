#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""This is a python game."""
import os
import sys
import json
import sqlite3
import pygame


class Manager:
    """Game resource management."""

    _singleton = None

    def __init__(self):
        """Object creation."""
        self.base_of_levels = [
            'first_level.txt',
            'second_level.txt',
            'third_level.txt',
            'fourth_level.txt',
            'fifth_level.txt',

        ]
        self.carrot_left = [
            pygame.transform.scale(self.load_image('carrot_left_1.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('carrot_left_2.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('carrot_left_3.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('carrot_left_4.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('carrot_left_5.png'),
                                   player_size)
        ]
        self.carrot_right = [
            pygame.transform.scale(self.load_image('carrot_right_1.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('carrot_right_2.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('carrot_right_3.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('carrot_right_4.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('carrot_right_5.png'),
                                   player_size)
        ]
        self.cool_carrot_left = [
            pygame.transform.scale(self.load_image('cool_carrot_left_1.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('cool_carrot_left_2.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('cool_carrot_left_3.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('cool_carrot_left_4.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('cool_carrot_left_5.png'),
                                   player_size)
        ]
        self.cool_carrot_right = [
            pygame.transform.scale(self.load_image('cool_carrot_right_1.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('cool_carrot_right_2.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('cool_carrot_right_3.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('cool_carrot_right_4.png'),
                                   player_size),
            pygame.transform.scale(self.load_image('cool_carrot_right_5.png'),
                                   player_size)
        ]

    def __new__(cls):
        """Give the old one instead of a new instance."""
        if cls._singleton is None:
            cls._singleton = super(Manager, cls).__new__(cls)

        return cls._singleton

    def load_image(self, filename, colorkey=None):
        """Load an image."""
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

    def get_sound(self, filename):
        """Load sound."""
        return pygame.mixer.Sound(f'sound/{filename}')

    def load_level(self, filename):
        """Load level."""
        filename = "data/" + filename
        with open(filename, 'r') as mapFile:
            return [line.strip() for line in mapFile]

    def take_image(self, index, see_right_true):
        """Return the next frame of the carrot."""
        global SKIN
        if SKIN == 'cool_carrot':
            if see_right_true:
                return self.cool_carrot_right[index]
            else:
                return self.cool_carrot_left[index]
        elif SKIN == 'carrot':
            if see_right_true:
                return self.carrot_right[index]
            else:
                return self.carrot_left[index]


def create_groups():
    """Create groups of sprites."""
    global all_sprites, tiles_group, dead_group, \
        player_group, pay_group, finish_group, \
        blobs_group, key_group, blocks_key_group
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    dead_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    pay_group = pygame.sprite.Group()
    finish_group = pygame.sprite.Group()
    blobs_group = pygame.sprite.Group()
    blocks_key_group = pygame.sprite.Group()
    key_group = pygame.sprite.Group()


class Finish(pygame.sprite.Sprite):
    """Finish Sprite."""

    def __init__(self, image, pos_x, pos_y):
        """Object creation."""
        super().__init__(finish_group, all_sprites)

        self.image = image
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Key(pygame.sprite.Sprite):
    """Key Sprite."""

    def __init__(self, pos_x, pos_y):
        """Object creation."""
        manager = Manager()

        super().__init__(key_group, all_sprites)

        self.image = manager.load_image('key.png')
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class KeyBlock(pygame.sprite.Sprite):
    """KeyBlock Sprite."""

    def __init__(self, pos_x, pos_y):
        """Object creation."""
        manager = Manager()

        super().__init__(tiles_group, blocks_key_group, all_sprites)

        self.image = manager.load_image('break.png')
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Money(pygame.sprite.Sprite):
    """Money Sprite."""

    def __init__(self, image, pos_x, pos_y):
        """Object creation."""
        super().__init__(pay_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Blob(pygame.sprite.Sprite):
    """Blob Sprite."""

    def __init__(self, pos_x, pos_y):
        """Object creation."""
        manager = Manager()

        super().__init__(blobs_group, all_sprites, dead_group)

        self.image = manager.load_image('blob.png')
        self.image = pygame.transform.scale(self.image, (31, 24))
        self.step = 1
        self.count_step = 0
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)

    def update(self):
        """Move the blob."""
        self.count_step += 1

        if self.count_step > 100:
            self.step *= -1
            self.count_step = 0

        self.rect.x += self.step


class Lava(pygame.sprite.Sprite):
    """Lava Sprite."""

    def __init__(self, image, pos_x, pos_y):
        """Object creation."""
        super().__init__(dead_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Tile(pygame.sprite.Sprite):
    """Tile Sprite."""

    def __init__(self, image, pos_x, pos_y):
        """Object creation."""
        super().__init__(tiles_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Carrot(pygame.sprite.Sprite):
    """Player Sprite."""

    speed = 4

    def __init__(self, x, y):
        """Object creation."""
        manager = Manager()
        super().__init__(player_group, all_sprites)

        self.load_image = manager.load_image
        self.load_sound = manager.get_sound
        self.take_image = manager.take_image

        carrot_image = self.load_image('carrot_right_1.png')

        self.sound_jump = self.load_sound('jump.wav')
        self.sound_coin = self.load_sound('coin.wav')
        self.sound_break = self.load_sound('break.wav')
        self.sound_dead = self.load_sound('dead.wav')

        self.image = pygame.transform.scale(carrot_image, (50, 70))
        self.rect = self.image.get_rect()

        self.dialog = False
        self.jumped = False
        self.dead = False
        self.see_right = False

        self.index_dialog = 0
        self.index = 0
        self.count_wait = 0
        self.vel_y = 0
        self.jump_count = 0

        self.rect.x = x
        self.rect.y = y

    def draw(self):
        """Draw player."""
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        """Handle event."""
        global PAUSE, LEVEL

        cooldown = 4
        self.count_wait += 1

        if self.count_wait > cooldown and not self.dead:
            self.index += 1
            self.count_wait = 0
            self.index = self.index % 5
            self.image = self.take_image(self.index, self.see_right)

        if not PAUSE and not self.dead and not self.dialog:
            delta_x = 0
            delta_y = 0

            key = pygame.key.get_pressed()

            # ------- Перемещение ------- #
            if key[pygame.K_SPACE] and not self.jumped and self.jump_count < 2:
                self.vel_y = -13
                self.jump_count += 1
                self.jumped = True
                self.sound_jump.play()

            if not key[pygame.K_SPACE]:
                self.jumped = False

            if key[pygame.K_LEFT]:
                self.see_right = False
                delta_x -= Carrot.speed

            if key[pygame.K_RIGHT]:
                self.see_right = True
                delta_x += Carrot.speed

            self.vel_y += 1

            if self.vel_y > 10:
                self.vel_y = 10

            delta_y += self.vel_y
            self.rect.y += delta_y

            if pygame.sprite.spritecollideany(self, tiles_group):
                tile = pygame.sprite.spritecollide(self, tiles_group, False)[0]
                self.rect.y -= delta_y

                if tile.rect[1] - 10 > self.rect.y + 50:
                    self.rect.y = tile.rect[1] - 70
                    self.jump_count = 0

                elif tile.rect[1] - 10 < self.rect.y + 50:
                    self.rect.y = tile.rect[1] + 25
                    self.vel_y = 0

            self.rect.x += delta_x

            if pygame.sprite.spritecollideany(self, tiles_group):
                tile = pygame.sprite.spritecollide(self, tiles_group, False)[0]
                self.rect.x -= delta_x

                if tile.rect[0] - tile_size / 2 > self.rect.x + 35:
                    self.rect.x = tile.rect[0] - 50

                elif tile.rect[0] - tile_size / 2 < self.rect.x + 35:
                    self.rect.x = tile.rect[0] + 25

            if pygame.sprite.spritecollideany(self, pay_group):
                self.sound_coin.play()

                for elem in pay_group:

                    if pygame.Rect.colliderect(elem.rect, self.rect):
                        room.money_up += 1
                        room.text = room.font.render(str(room.money_up), True,
                                                     (255, 255, 255))
                        elem.kill()

            if pygame.sprite.spritecollideany(self, key_group):
                self.sound_break.play()

                for elem in key_group:
                    elem.kill()

                    for element in blocks_key_group:
                        element.kill()

            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                delta_y = 0

            if pygame.sprite.spritecollideany(self, finish_group):
                self.dialog = True

                connection = sqlite3.connect('Progress.db')
                cursor = connection.cursor()
                query = '''SELECT Money FROM info'''
                cursor.execute(query)
                connection.commit()
                cash = cursor.fetchall()[0][0] + room.money_up
                query = f'''UPDATE info SET Money={cash}'''
                cursor.execute(query)
                connection.commit()
                query = '''SELECT levels FROM info'''

                LEVEL += 1

                cursor.execute(query)
                connection.commit()
                levels = str(cursor.fetchall()[0][0])

                if str(LEVEL + 1) not in levels:
                    levels += f', {LEVEL + 1}'

                query = f'''
                UPDATE info SET levels="{levels}";'''
                cursor.execute(query)
                connection.commit()

                connection.close()

            if pygame.sprite.spritecollideany(self, dead_group):

                if self.see_right:
                    self.image = pygame.transform.scale(
                        self.load_image('dead_carrot_right.png'), player_size)

                else:
                    self.image = pygame.transform.scale(
                        self.load_image('dead_carrot.png'), player_size)

                self.sound_dead.play()
                self.dead = True


class ChangeLevelMenu:
    """Level selection window class."""

    def __init__(self):
        """Object creation."""
        manager = Manager()

        self.sound_click = manager.get_sound('button.wav')
        self.levels = [1]

    def update(self, event):
        """Handle event."""
        global room, LEVEL

        manager = Manager()

        if (event.type == pygame.MOUSEBUTTONUP
                and 5 < event.pos[0] < 55 and 5 < event.pos[1] < 55):
            room = Menu()
            self.sound_click.play()

            create_groups()

        elif (event.type == pygame.MOUSEBUTTONUP
              and 225 < event.pos[0] < 315 and 242 < event.pos[1] < 332):
            room = World(manager.load_level('first_level.txt'))
            self.sound_click.play()
            LEVEL = 0

        elif (event.type == pygame.MOUSEBUTTONUP
              and 340 < event.pos[0] < 430 and 242 < event.pos[1] < 332):
            if 2 in self.levels:
                self.sound_click.play()
                room = World(manager.load_level('second_level.txt'))
                LEVEL = 1

        elif (event.type == pygame.MOUSEBUTTONUP
              and 455 < event.pos[0] < 535 and 242 < event.pos[1] < 332):
            if 3 in self.levels:
                self.sound_click.play()
                room = World(manager.load_level('third_level.txt'))
                LEVEL = 2

        elif (event.type == pygame.MOUSEBUTTONUP
              and 570 < event.pos[0] < 640 and 242 < event.pos[1] < 332):
            if 4 in self.levels:
                self.sound_click.play()
                room = World(manager.load_level('fourth_level.txt'))
                LEVEL = 3

        elif (event.type == pygame.MOUSEBUTTONUP
              and 685 < event.pos[0] < 745 and 242 < event.pos[1] < 332):
            if 5 in self.levels:
                self.sound_click.play()
                room = World(manager.load_level('fifth_level.txt'))
                LEVEL = 4

    def draw(self):
        """Draw window."""
        manager = Manager()

        screen.blit(pygame.transform.scale(manager.load_image('back.png'),
                                           (50, 50)), (5, 5))

        coord_x = [
            225, 340, 455, 570, 685
        ]

        coord_y = [
            242, 357
        ]

        for i in range(2):
            for j in range(5):
                lvl_number = i * 5 + j + 1
                if lvl_number in self.levels:
                    screen.blit(pygame.transform.scale(
                        manager.load_image(f'lvl{i * 5 + j + 1}.png'),
                        (90, 90)),
                        (coord_x[j], coord_y[i]))
                else:
                    screen.blit(pygame.transform.scale(
                        manager.load_image('close_lvl.png'),
                        (90, 90)),
                        (coord_x[j], coord_y[i]))


class InfoMenu:
    """Information window class."""

    def __init__(self):
        """Object creation."""
        manager = Manager()
        self.sound_click = manager.get_sound('button.wav')
        self.image = manager.load_image('info.png')

    def update(self, event):
        """Handle event."""
        global room

        if (event.type == pygame.MOUSEBUTTONUP
                and 2 < event.pos[0] < 52 and 2 < event.pos[1] < 52):
            room = Menu()
            self.sound_click.play()

    def draw(self):
        """Draw window."""
        screen.blit(self.image, (0, 0))


class ChangeSkinMenu:
    """Skin selection window class."""

    def __init__(self):
        """Object creation."""
        manager = Manager()

        self.sail = 0
        self.index = 0
        self.res = None
        self.button_select = False
        self.sound_click = manager.get_sound('button.wav')
        self.list = ['carrot_right_1.png', 'cool_carrot_right_1.png']

    def update(self, event):
        """Handle event."""
        global room, SKIN

        connection = sqlite3.connect('Progress.db')
        cursor = connection.cursor()
        query = '''SELECT cool_carrot FROM info'''
        cursor.execute(query)

        self.res = cursor.fetchall()[0][0]
        connection.commit()
        connection.close()

        if (event.type == pygame.MOUSEBUTTONUP
                and 5 < event.pos[0] < 55 and 5 < event.pos[1] < 55):
            room = Menu()
            self.sound_click.play()

            create_groups()

        elif (event.type == pygame.MOUSEBUTTONUP
              and 700 < event.pos[0] < 750 and 350 < event.pos[1] < 400):

            self.sound_click.play()

            if self.index + 1 > len(self.list) - 1:
                self.index = 0
            else:
                self.index += 1

            self.button_select = False

        elif (event.type == pygame.MOUSEBUTTONUP
              and 300 < event.pos[0] < 350 and 350 < event.pos[1] < 400):

            self.sound_click.play()

            if self.index - 1 < 0:
                self.index = len(self.list) - 1
            else:
                self.index -= 1

            self.button_select = False

        elif (event.type == pygame.MOUSEBUTTONUP
              and 380 < event.pos[0] < 680 and 500 < event.pos[1] < 600):

            self.sound_click.play()

            if self.list[self.index] == 'carrot_right_1.png':
                SKIN = 'carrot'
                self.button_select = not self.button_select

            elif self.list[self.index] == 'cool_carrot_right_1.png':
                if self.res == 'True':
                    SKIN = 'cool_carrot'
                    self.button_select = not self.button_select
                    if not self.button_select:
                        SKIN = 'carrot'

                else:
                    connection = sqlite3.connect('Progress.db')
                    cursor = connection.cursor()
                    query = '''SELECT Money FROM info'''
                    cursor.execute(query)
                    connection.commit()

                    money = cursor.fetchall()[0][0]

                    if money >= 65:
                        query = f'''UPDATE info SET Money={money - 65}'''
                        cursor.execute(query)
                        connection.commit()

                        query = '''UPDATE info SET cool_carrot="True"'''
                        cursor.execute(query)
                        connection.commit()

                        self.button_select = True
                        room.draw()

                    connection.close()

    def draw(self):
        """Draw window."""
        manager = Manager()

        screen.blit(manager.load_image('shop_title.png'), (30, 0))
        screen.blit(pygame.transform.scale(
            manager.load_image('back.png'), (50, 50)), (5, 5))
        screen.blit(pygame.transform.scale(
            manager.load_image('step_left.png'), (50, 50)), (300, 350))
        screen.blit(pygame.transform.scale(
            manager.load_image('step_right.png'), (50, 50)), (700, 350))
        screen.blit(pygame.transform.scale(
            manager.load_image(self.list[self.index]), (200, 288)), (400, 206))

        if (self.list[self.index] == 'cool_carrot_right_1.png'
                and self.res == 'False'):
            screen.blit(manager.load_image('button_pay_cool.png'),
                        (380, 500))
        else:
            if self.button_select:
                screen.blit(manager.load_image('select_button.png'),
                            (380, 500))

            else:
                screen.blit(manager.load_image('button_skin.png'),
                            (380, 500))


class World:
    """World window class."""

    def __init__(self, data):
        """Object creation."""
        manager = Manager()

        self.money_up = 0
        self.tile_list = []
        self.font = pygame.font.Font(None, 50)
        self.tile_sprites = pygame.sprite.Group()
        self.money_img = manager.load_image('money.png')
        self.sound_click = manager.get_sound('button.wav')
        self.text = self.font.render("0", True, (255, 255, 255))
        self.back_button = pygame.transform.scale(
            manager.load_image('back.png'), (50, 50))

        dirt_img = manager.load_image('dirt.png')
        lava_img = manager.load_image('lava.png')
        grass_img = manager.load_image('grass.png')
        finish_img = manager.load_image('little_carrot.png')

        # ------- Сгенерировать уровень по карте (data) ------- #
        row_count = -1
        for row in data:
            col_count = -1
            for tile in row:
                tile = int(tile)
                if tile == 1:
                    Tile(dirt_img, col_count, row_count)
                    self.tile_list.append(tile)
                elif tile == 2:
                    Tile(grass_img, col_count, row_count)
                    self.tile_list.append(tile)
                elif tile == 3:
                    Money(self.money_img, col_count, row_count)
                elif tile == 4:
                    Finish(finish_img, col_count, row_count)
                elif tile == 5:
                    self.carrot = Carrot(
                        col_count * tile_size, row_count * tile_size
                    )
                elif tile == 6:
                    Lava(lava_img, col_count, row_count)
                elif tile == 7:
                    Blob(col_count, row_count)
                elif tile == 8:
                    Key(col_count, row_count)
                elif tile == 9:
                    KeyBlock(col_count, row_count)
                col_count += 1
            row_count += 1

    def update(self, event):
        """Handle event."""
        global room, PAUSE
        manager = Manager()

        if self.carrot.dialog:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                self.carrot.index_dialog += 1

                with open('dialogs.json') as f:
                    templates = json.load(f)
                    dialogs = templates[f'level{LEVEL}']
                if self.carrot.index_dialog == len(dialogs):

                    create_groups()

                    if LEVEL == len(manager.base_of_levels):
                        room = Menu()
                    else:
                        room = World(
                            manager.load_level(manager.base_of_levels[LEVEL])
                        )

        if self.carrot.dead:
            if (event.type == pygame.MOUSEBUTTONUP
                    and 385 < event.pos[0] < 615 and 290 < event.pos[1] < 340):

                self.carrot.dead = False

                create_groups()
                room = World(manager.load_level(manager.base_of_levels[LEVEL]))

                self.sound_click.play()

            elif (event.type == pygame.MOUSEBUTTONUP
                  and 385 < event.pos[0] < 615 and 365 < event.pos[1] < 414):

                self.carrot.dead = False

                room = Menu()
                create_groups()

                self.sound_click.play()

        if not PAUSE and not self.carrot.dead:

            if (event.type == pygame.MOUSEBUTTONUP
                    and 945 < event.pos[0] < 995 and 5 < event.pos[1] < 55):
                PAUSE = not PAUSE
                self.sound_click.play()

        else:

            if (event.type == pygame.MOUSEBUTTONUP
                    and 385 < event.pos[0] < 615 and 290 < event.pos[1] < 340):
                PAUSE = not PAUSE
                self.sound_click.play()

            elif (event.type == pygame.MOUSEBUTTONUP
                  and 385 < event.pos[0] < 615 and 365 < event.pos[1] < 414):

                PAUSE = not PAUSE
                self.sound_click.play()

                room = Menu()

                create_groups()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            PAUSE = not PAUSE

        self.carrot.update()

    def draw(self):
        """Draw the world."""
        global PAUSE
        manager = Manager()
        if not PAUSE:
            blobs_group.update()

        all_sprites.draw(screen)

        # ------- Счетчик монет ------- #
        screen.blit(self.text, (31, 0))
        screen.blit(pygame.transform.scale(self.money_img, (25, 25)), (3, 3))
        screen.blit(pygame.transform.scale(manager.load_image('pause.png'),
                                           (50, 50)), (945, 5))

        if PAUSE:
            screen.blit(manager.load_image('pause_slide.png'), (350, 250))

        if self.carrot.dead:
            screen.blit(manager.load_image('fail_title.png'), (0, 0))
            screen.blit(manager.load_image('fail_slide.png'), (350, 250))

        if self.carrot.dialog:
            if self.carrot.index_dialog % 2 == 0:

                with open('dialogs.json') as f:
                    templates = json.load(f)
                    text = templates[f'level{LEVEL}'][self.carrot.index_dialog]

                screen.blit(manager.load_image('dialog_1.png'), (0, 500))

                if type(text) == list:

                    index = 0
                    for elem in text:
                        index += 1
                        text = self.font.render(elem, True, (255, 255, 255))
                        screen.blit(text, (0, 475 + index * 45))

                else:

                    screen.blit(manager.load_image('dialog_1.png'), (0, 500))
                    text = self.font.render(text, True, (255, 255, 255))
                    screen.blit(text, (0, 515))
            else:

                with open('dialogs.json') as f:
                    templates = json.load(f)
                    text = templates[f'level{LEVEL}'][self.carrot.index_dialog]

                screen.blit(manager.load_image('dialog_2.png'), (0, 500))
                if type(text) == list:

                    index = 0
                    for elem in text:
                        index += 1
                        text = self.font.render(elem, True, (255, 255, 255))
                        screen.blit(text, (355, 470 + index * 45))

                else:

                    screen.blit(manager.load_image('dialog_2.png'), (0, 500))
                    text = self.font.render(text, True, (255, 255, 255))
                    screen.blit(text, (355, 515))

            text = self.font.render('[SPACE] - continue',
                                    True,
                                    (255, 255, 255)
                                    )
            screen.blit(text, (330, 15))


class Menu:
    """Menu window class."""

    def __init__(self):
        """Object creation."""
        manager = Manager()

        self.image = manager.load_image('button_start.png')

        self.rect = self.image.get_rect()
        self.font = pygame.font.Font(None, 50)
        self.money_img = manager.load_image('money.png')
        self.sound_click = manager.get_sound('button.wav')
        self.image_change = manager.load_image('button_change_lvl.png')

    def update(self, event):
        """Handle event."""
        global room, LEVEL

        manager = Manager()

        if (event.type == pygame.MOUSEBUTTONUP
                and 385 < event.pos[0] < 615 and 250 < event.pos[1] < 300):
            room = World(manager.load_level('first_level.txt'))
            LEVEL = 0

            self.sound_click.play()
        elif (event.type == pygame.MOUSEBUTTONUP
              and 385 < event.pos[0] < 615 and 325 < event.pos[1] < 375):
            room = ChangeLevelMenu()
            self.sound_click.play()

            connection = sqlite3.connect('Progress.db')
            cursor = connection.cursor()
            query = '''SELECT levels FROM info'''
            cursor.execute(query)
            connection.commit()
            answer = cursor.fetchall()[0][0]

            if answer == 1:
                room.levels = [1]
            else:
                room.levels = list(map(int, answer.split(', ')))

            connection.close()

        elif (event.type == pygame.MOUSEBUTTONUP
              and 385 < event.pos[0] < 615 and 400 < event.pos[1] < 450):
            room = ChangeSkinMenu()

            self.sound_click.play()

        elif (event.type == pygame.MOUSEBUTTONUP
              and 5 < event.pos[0] < 55 and 645 < event.pos[1] < 695):
            room = InfoMenu()

            self.sound_click.play()

    def draw(self):
        """Draw the menu."""
        manager = Manager()

        screen.blit(self.image, (385, 250))
        screen.blit(self.image_change, (385, 325))
        screen.blit(manager.load_image('button_change_scin.png'), (385, 400))
        screen.blit(manager.load_image('title.png'), (0, 15))
        screen.blit(manager.load_image('info_button.png'), (5, 645))

        # ------- Счетчик монет ------- #
        screen.blit(pygame.transform.scale(self.money_img, (25, 25)), (3, 3))

        connection = sqlite3.connect('Progress.db')
        cursor = connection.cursor()
        query = '''SELECT Money FROM info'''
        cursor.execute(query)
        connection.commit()

        cash = str(cursor.fetchall()[0][0])
        connection.close()

        text = self.font.render(cash, True, (255, 255, 255))
        screen.blit(text, (31, 0))


LEVEL = 0
SKIN = 'carrot'
PAUSE = False

create_groups()

screen_width = 1000
screen_height = 700
tile_size = 25
player_size = (50, 72)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
room = Menu()


def main():
    """Run the main game loop."""
    global tile_size

    running = True
    manager = Manager()
    while running:
        screen.blit(manager.load_image('background.png'), (0, 0))

        if isinstance(room, World):
            room.carrot.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            room.update(event)

        room.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
