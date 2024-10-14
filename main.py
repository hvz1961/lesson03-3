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

# Инициализация счета
score = 0
font = pygame.font.Font(None, 36)  # Шрифт для отображения счета

# Фиксация начального времени
start_ticks = pygame.time.get_ticks()  # Начальное время в миллисекундах

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

                # Если мишень попали, увеличиваем счет и перемещаем мишень# Если мишень попали, переместим её на новое место
                score += 1
                target_x, target_y = spawn_target()

    # Отрисовка мишени
    screen.blit(target_img, (target_x, target_y))

    # Отрисовка счета
    score_text = font.render(f'Счет: {score}', True, (255, 255, 255))  # Белый цвет текста
    screen.blit(score_text, (10, 10))  # Отобразить счет в верхнем левом углу

    # Вычисление и отображение прошедшего времени
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Прошедшее время в секундах
    time_text = font.render(f'Время: {int(seconds)} сек', True, (255, 255, 255))  # Белый цвет текста
    screen.blit(time_text, (10, 50))  # Отобразить время ниже счета

        # Обновление экрана
    pygame.display.update()

# Завершение Pygame
pygame.quit()
