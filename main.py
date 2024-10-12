import pygame
import random

# Инициировали pygame
pygame.init()
# Создаем константы, неизменяемые величины, для экрана: ширина 800 пикселей, высота 600
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Создаем переменную для экрана, и далее функцию для экрана, чтобы экран появился
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Вводим название экрана
pygame.display.set_caption('Игра Тир')
# Загружаем изображение, картинку игры: создаем переменную, где будет храниться картинка
icon = pygame.image.load('img/лого тир.jpeg')
# Устанавливаем иконку
pygame.display.set_icon(icon)
# Создаем цель по которой будем стрелять: сначала переменную с картинкой
target_img = pygame.image.load('img/target.png')
# Пропишем ширину и высоту иконки
target_width = 80
target_heigth = 80
# Пропишем рандомные координаты, по которым будет перемещаться цель
target_х = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_heigth)
# Зададим рандомное значение для заливки фона
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))





runnig = True
while running:
    pass

pygame.quit()
