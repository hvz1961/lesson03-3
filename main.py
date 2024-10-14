import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы для размера экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Установка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра Тир')

# Загрузка и установка иконки
icon = pygame.image.load('img/логотир.jpeg')
pygame.display.set_icon(icon)

# Загрузка изображения мишени
target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

# Функция для генерации случайной позиции мишени
def spawn_target():
    return random.randint(0, SCREEN_WIDTH - target_width), random.randint(0, SCREEN_HEIGHT - target_height)

# Инициализация мишени
target_x, target_y = spawn_target()

# Основной цвет фона
background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Основной игровой цикл
running = True
while running:
    # Заполнение экрана цветом
    screen.fill(background_color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Если мишень попали, переместим её на новое место
                target_x, target_y = spawn_target()

    # Отрисовка мишени
    screen.blit(target_img, (target_x, target_y))

    # Обновление экрана
    pygame.display.update()

# Завершение Pygame
pygame.quit()
