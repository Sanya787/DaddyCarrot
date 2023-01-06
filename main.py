import os
import sys

from dialogs import all_dialogs
import sqlite3
import pygame


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        return [line.strip() for line in mapFile]


base_of_levels = [
    'first_level.txt',
    'second_level.txt',
    'third_level.txt',
]


def create_groups():
    global all_sprites, tiles_group, dead_group,\
        player_group, pay_group, finish_group,\
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


SCIN = 'carrot'
PAUSE = False
LEVEL = 0
screen_width = 1000
screen_height = 700
tile_size = 25

create_groups()


class Finish(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, image, pos_x, pos_y):

        super().__init__(finish_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Key(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, pos_x, pos_y):

        super().__init__(key_group, all_sprites)

        self.image = load_image('key.png')
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class KeyBlock(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, pos_x, pos_y):

        super().__init__(tiles_group, blocks_key_group, all_sprites)

        self.image = load_image('break.png')
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Money(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, image, pos_x, pos_y):

        super().__init__(pay_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Blob(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, pos_x, pos_y):

        super().__init__(blobs_group, all_sprites, dead_group)

        self.image = load_image('blob.png')
        self.image = pygame.transform.scale(self.image, (31, 24))

        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)
        self.step = 1
        self.count_step = 0

    def update(self):
        self.count_step += 1

        if self.count_step > 100:
            self.step *= -1
            self.count_step = 0
        self.rect.x += self.step


class Lava(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, image, pos_x, pos_y):

        super().__init__(dead_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


def load_image(filename, colorkey=None):
    # ------- Загрузка изображения ------- #
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


carrot_left = [
    pygame.transform.scale(load_image('carrot_left_1.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_left_2.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_left_3.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_left_4.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_left_5.png'), (50, 72))
]

carrot_right = [
    pygame.transform.scale(load_image('carrot_right_1.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_right_2.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_right_3.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_right_4.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_right_5.png'), (50, 72))
]

cool_carrot_left = [
    pygame.transform.scale(load_image('cool_carrot_left_1.png'), (50, 72)),
    pygame.transform.scale(load_image('cool_carrot_left_2.png'), (50, 72)),
    pygame.transform.scale(load_image('cool_carrot_left_3.png'), (50, 72)),
    pygame.transform.scale(load_image('cool_carrot_left_4.png'), (50, 72)),
    pygame.transform.scale(load_image('cool_carrot_left_5.png'), (50, 72))
]

cool_carrot_right = [
    pygame.transform.scale(load_image('cool_carrot_right_1.png'), (50, 72)),
    pygame.transform.scale(load_image('cool_carrot_right_2.png'), (50, 72)),
    pygame.transform.scale(load_image('cool_carrot_right_3.png'), (50, 72)),
    pygame.transform.scale(load_image('cool_carrot_right_4.png'), (50, 72)),
    pygame.transform.scale(load_image('cool_carrot_right_5.png'), (50, 72))
]
#


def take_image(index, see_right_true):
    if SCIN == 'cool_carrot':
        if see_right_true:
            return cool_carrot_right[index]
        else:
            return cool_carrot_left[index]
    elif SCIN == 'carrot':
        if see_right_true:
            return carrot_right[index]
        else:
            return carrot_left[index]


def draw_grid():
    # ------- Рисовать сетку ------- #
    for line in range(0, 40):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class Tile(pygame.sprite.Sprite):
    # ------- Создать блок------- #
    def __init__(self, image, pos_x, pos_y):

        super().__init__(tiles_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Carrot(pygame.sprite.Sprite):
    speed = 4
    carrot_image = load_image('carrot_right_1.png')

    def __init__(self, x, y):
        super().__init__(player_group, all_sprites)

        self.image = pygame.transform.scale(Carrot.carrot_image, (50, 70))
        self.rect = self.image.get_rect()
        self.dialog = False
        self.index_dialog = 0
        self.index = 0
        self.jumped = False
        self.dead = False
        self.rect.x = x
        self.count_wait = 0
        self.rect.y = y
        self.vel_y = 0
        self.see_right = False
        self.jump_count = 0

    def draw(self):
        # ------- Рисовать игрока ------- #
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        global room, LEVEL, PAUSE

        cooldown = 4
        self.count_wait += 1
        if self.count_wait > cooldown and not self.dead:
            self.index += 1
            self.count_wait = 0
            self.index = self.index % 5
            self.image = take_image(self.index, self.see_right)

        if not PAUSE and not self.dead and not self.dialog:
            delta_x = 0
            delta_y = 0

            key = pygame.key.get_pressed()

            # ------- Перемещение ------- #
            if key[pygame.K_SPACE] and not self.jumped and self.jump_count < 2:
                self.vel_y = -13
                self.jump_count += 1
                self.jumped = True
                sound_jump.play()
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
            # ------- Перемещение ------- #
            # ------- Проверка столкновения ------- #
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
                sound_coin.play()
                for elem in pay_group:
                    if pygame.Rect.colliderect(elem.rect, self.rect):
                        room.money_up += 1
                        room.text = room.font.render(str(room.money_up), True, (255, 255, 255))
                        elem.kill()

            if pygame.sprite.spritecollideany(self, key_group):
                sound_break.play()
                for elem in key_group:
                    elem.kill()
                    for element in blocks_key_group:
                        element.kill()

                # ------- Проверка столкновения -------
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                delta_y = 0

            if pygame.sprite.spritecollideany(self, finish_group):
                self.dialog = True

                connection = sqlite3.connect('Progress.db')
                cursor = connection.cursor()

                query = f'''
                    SELECT Money FROM info'''
                cursor.execute(query)
                connection.commit()
                cash = cursor.fetchall()[0][0] + room.money_up

                query = f'''
                UPDATE info SET Money={cash}'''
                cursor.execute(query)
                connection.commit()

                LEVEL += 1

                query = f'''
                SELECT levels FROM info'''

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
                    self.image = pygame.transform.scale(load_image('dead_carrot_right.png'), (50, 70))
                else:
                    self.image = pygame.transform.scale(load_image('dead_carrot.png'), (50, 70))

                sound_dead.play()
                self.dead = True


class ChangeLevel:
    def __init__(self):
        self.levels = [1]

    def update(self, event):
        global room, LEVEL

        if event.type == pygame.MOUSEBUTTONUP and 5 < event.pos[0] < 55 and 5 < event.pos[1] < 55:
            room = Menu()
            sound_click.play()

            create_groups()

        elif event.type == pygame.MOUSEBUTTONUP and 225 < event.pos[0] < 315 and 242 < event.pos[1] < 332:
            room = World(load_level('first_level.txt'))
            sound_click.play()
            LEVEL = 0
        elif event.type == pygame.MOUSEBUTTONUP and 340 < event.pos[0] < 430 and 242 < event.pos[1] < 332:
            if 2 in self.levels:
                sound_click.play()
                room = World(load_level('second_level.txt'))
                LEVEL = 1
        elif event.type == pygame.MOUSEBUTTONUP and 455 < event.pos[0] < 535 and 242 < event.pos[1] < 332:
            if 3 in self.levels:
                sound_click.play()
                room = World(load_level('third_level.txt'))
                LEVEL = 2

    def draw(self):
        screen.blit(pygame.transform.scale(load_image('back.png'), (50, 50)), (5, 5))

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
                    screen.blit(pygame.transform.scale(load_image(f'lvl{i * 5 + j + 1}.png'), (90, 90)),
                                (coord_x[j], coord_y[i]))
                else:
                    screen.blit(pygame.transform.scale(load_image(f'close_lvl.png'), (90, 90)),
                                (coord_x[j], coord_y[i]))


class Info:
    def __init__(self):
        self.image = load_image('info.png')

    def update(self, event):
        global room

        if event.type == pygame.MOUSEBUTTONUP and 2 < event.pos[0] < 52 and 2 < event.pos[1] < 52:
            room = Menu()
            sound_click.play()

    def draw(self):
        screen.blit(self.image, (0, 0))


class ChangeScin:
    def __init__(self):
        self.list = ['carrot_right_1.png', 'cool_carrot_right_1.png']
        self.index = 0
        self.sail = 0
        self.res = None
        self.button_select = False

    def update(self, event):
        global room, SCIN

        connection = sqlite3.connect('Progress.db')
        cursor = connection.cursor()

        query = f'''SELECT cool_carrot FROM info'''

        cursor.execute(query)
        self.res = cursor.fetchall()[0][0]
        connection.commit()
        connection.close()

        if event.type == pygame.MOUSEBUTTONUP and 5 < event.pos[0] < 55 and 5 < event.pos[1] < 55:
            room = Menu()
            sound_click.play()

            create_groups()

        elif event.type == pygame.MOUSEBUTTONUP and 700 < event.pos[0] < 750 and 350 < event.pos[1] < 400:
            sound_click.play()
            if self.index + 1 > len(self.list) - 1:
                self.index = 0
            else:
                self.index += 1

            self.button_select = False

        elif event.type == pygame.MOUSEBUTTONUP and 300 < event.pos[0] < 350 and 350 < event.pos[1] < 400:
            sound_click.play()
            if self.index - 1 < 0:
                self.index = len(self.list) - 1
            else:
                self.index -= 1

            self.button_select = False

        elif event.type == pygame.MOUSEBUTTONUP and 380 < event.pos[0] < 680 and 500 < event.pos[1] < 600:
            sound_click.play()

            if self.list[self.index] == 'carrot_right_1.png':
                SCIN = 'carrot'
                self.button_select = not self.button_select
            elif self.list[self.index] == 'cool_carrot_right_1.png':
                if self.res == 'True':
                    SCIN = 'cool_carrot'
                    self.button_select = not self.button_select
                    if not self.button_select:
                        SCIN = 'carrot'
                else:
                    connection = sqlite3.connect('Progress.db')
                    cursor = connection.cursor()

                    query = f'''
                        SELECT Money FROM info'''
                    cursor.execute(query)
                    connection.commit()
                    money = cursor.fetchall()[0][0]

                    if money >= 65:
                        query = f'''UPDATE info SET Money={money - 65}'''
                        cursor.execute(query)
                        connection.commit()

                        query = f'''UPDATE info SET cool_carrot="True"'''
                        cursor.execute(query)
                        connection.commit()
                        self.button_select = True
                        room.draw()

                    connection.close()

    def draw(self):
        screen.blit(pygame.transform.scale(load_image('back.png'), (50, 50)), (5, 5))
        screen.blit(pygame.transform.scale(load_image(self.list[self.index]), (200, 288)), (400, 206))
        screen.blit(load_image('shop_title.png'), (30, 0))
        screen.blit(pygame.transform.scale(load_image('step_right.png'), (50, 50)), (700, 350))
        screen.blit(pygame.transform.scale(load_image('step_left.png'), (50, 50)), (300, 350))
        if self.list[self.index] == 'cool_carrot_right_1.png' and self.res == 'False':
            screen.blit(load_image('button_pay_cool.png'), (380, 500))
        else:
            if self.button_select:
                screen.blit(load_image('select_button.png'), (380, 500))
            else:
                screen.blit(load_image('button_scin.png'), (380, 500))


class World:
    def __init__(self, data):
        self.font = pygame.font.Font(None, 50)
        self.tile_sprites = pygame.sprite.Group()
        self.text = self.font.render("0", True, (255, 255, 255))
        self.back_button = pygame.transform.scale(load_image('back.png'), (50, 50))
        self.tile_list = []
        self.money_up = 0
        self.money_img = load_image('money.png')
        dirt_img = load_image('dirt.png')
        lava_img = load_image('lava.png')
        grass_img = load_image('grass.png')
        finish_img = load_image('checkpoint.png')

        # ------- Сгенерировать уровень по карте (data) ------- #
        row_count = 0
        for row in data:
            col_count = 0
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
                    self.carrot = Carrot(col_count * tile_size, row_count * tile_size)
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
        # ------- Обновить уровень ------- #
        global room, PAUSE

        if self.carrot.dialog:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.carrot.index_dialog += 1
                if self.carrot.index_dialog == len(all_dialogs[LEVEL - 1]):
                    create_groups()
                    if LEVEL == len(base_of_levels):
                        room = Menu()
                    else:
                        room = World(load_level(base_of_levels[LEVEL]))

        if self.carrot.dead:
            if event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 290 < event.pos[1] < 340:

                self.carrot.dead = False

                create_groups()
                sound_click.play()

                room = World(load_level('first_level.txt'))

            elif event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 365 < event.pos[1] < 414:

                self.carrot.dead = False

                room = Menu()
                sound_click.play()

                create_groups()

        if not PAUSE and not self.carrot.dead:

            if event.type == pygame.MOUSEBUTTONUP and 945 < event.pos[0] < 995 and 5 < event.pos[1] < 55:
                PAUSE = not PAUSE
                sound_click.play()

        else:

            if event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 290 < event.pos[1] < 340:
                PAUSE = not PAUSE
                sound_click.play()

            elif event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 365 < event.pos[1] < 414:

                PAUSE = not PAUSE
                sound_click.play()

                room = Menu()

                create_groups()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            PAUSE = not PAUSE

        # ------- Обновить нужно только игрока на поле ------- #
        self.carrot.update()

    def draw(self):
        # ------- Нарисовать уровень ------- #
        blobs_group.update()

        all_sprites.draw(screen)

        # ------- Счетчик монет ------- #
        screen.blit(pygame.transform.scale(self.money_img, (25, 25)), (3, 3))
        screen.blit(self.text, (31, 0))

        screen.blit(pygame.transform.scale(load_image('pause.png'), (50, 50)), (945, 5))

        if PAUSE:
            screen.blit(load_image('pause_slide.png'), (350, 250))

        if self.carrot.dead:
            screen.blit(load_image('fail_title.png'), (0, 0))
            screen.blit(load_image('fail_slide.png'), (350, 250))

        if self.carrot.dialog:
            if self.carrot.index_dialog % 2 == 0:
                text = all_dialogs[LEVEL - 1][self.carrot.index_dialog]
                screen.blit(load_image('dialog_1.png'), (0, 500))
                if type(text) == type((0, 1)):
                    index = 0
                    for elem in text:
                        index += 1
                        text = self.font.render(elem, True, (255, 255, 255))
                        screen.blit(text, (0, 475 + index * 45))
                else:
                    screen.blit(load_image('dialog_1.png'), (0, 500))
                    text = self.font.render(text, True, (255, 255, 255))
                    screen.blit(text, (0, 515))
            else:
                text = all_dialogs[LEVEL - 1][self.carrot.index_dialog]
                screen.blit(load_image('dialog_2.png'), (0, 500))
                if type(text) == type((0, 1)):
                    index = 0
                    for elem in text:
                        index += 1
                        text = self.font.render(elem, True, (255, 255, 255))
                        screen.blit(text, (355, 470 + index * 45))
                else:
                    screen.blit(load_image('dialog_2.png'), (0, 500))
                    text = self.font.render(text, True, (255, 255, 255))
                    screen.blit(text, (355, 515))
            text = self.font.render('[SPACE] - continue', True, (255, 255, 255))
            screen.blit(text, (330, 15))


class Menu:
    def __init__(self):

        self.font = pygame.font.Font(None, 50)
        self.image = load_image('button_start.png')
        self.image_change = load_image('button_change_lvl.png')
        self.rect = self.image.get_rect()
        self.money_img = load_image('money.png')

    def update(self, event):
        # ------- Обновить меню ------- #
        global room, LEVEL
        # ------- Если нажали начать: ------- #
        if event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 250 < event.pos[1] < 300:
            room = World(load_level('first_level.txt'))
            sound_click.play()
            LEVEL = 0
        elif event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 325 < event.pos[1] < 375:
            room = ChangeLevel()
            sound_click.play()

            connection = sqlite3.connect('Progress.db')
            cursor = connection.cursor()

            query = f'''SELECT levels FROM info'''

            cursor.execute(query)
            connection.commit()

            answer = cursor.fetchall()[0][0]
            if answer == 1:
                room.levels = [1]
            else:
                room.levels = list(map(int, answer.split(', ')))

            connection.close()

        elif event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 400 < event.pos[1] < 450:
            room = ChangeScin()
            sound_click.play()

        elif event.type == pygame.MOUSEBUTTONUP and 5 < event.pos[0] < 55 and 645 < event.pos[1] < 695:
            room = Info()
            sound_click.play()

    def draw(self):
        # ------- Отрисовать меню ------- #
        screen.blit(self.image, (385, 250))
        screen.blit(self.image_change, (385, 325))
        screen.blit(load_image('button_change_scin.png'), (385, 400))
        screen.blit(load_image('title.png'), (0, 15))
        screen.blit(load_image('info_button.png'), (5, 645))

        # ------- Счетчик монет ------- #
        screen.blit(pygame.transform.scale(self.money_img, (25, 25)), (3, 3))

        connection = sqlite3.connect('Progress.db')
        cursor = connection.cursor()

        query = f'''
        SELECT Money FROM info'''

        cursor.execute(query)
        connection.commit()
        cash = str(cursor.fetchall()[0][0])
        connection.close()

        text = self.font.render(cash, True, (255, 255, 255))
        screen.blit(text, (31, 0))


pygame.init()

sound_jump = pygame.mixer.Sound('sound/jump.wav')
sound_coin = pygame.mixer.Sound('sound/coin.wav')
sound_break = pygame.mixer.Sound('sound/break.wav')
sound_dead = pygame.mixer.Sound('sound/dead.wav')
sound_click = pygame.mixer.Sound('sound/button.wav')

screen = pygame.display.set_mode((screen_width, screen_height))
room = Menu()


def main():
    global tile_size

    running = True

    while running:
        # ------- Залить фон ------- #
        screen.blit(load_image('background.png'), (0, 0))

        # ------- Если это какой-то уровень: ------- #
        if isinstance(room, World):
            room.carrot.update()

        # ------- Нажатия ------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                tile_size = screen_height / screen_width * 35.7
            # ------- Обновить с event ------- #
            room.update(event)

        # ------- Отрисовать: ------- #
        # draw_grid()
        room.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
