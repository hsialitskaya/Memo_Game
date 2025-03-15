import pygame
import sys
# Отображение запроса имени на экране
def get_player_name(font, gameWidht, gameHeight, screen, DEEPPINK_COLOR, BACKGROUND_COLOR):
    text = font.render("Wpisz swoje imię:", True, (0, 0, 0))  # текст на экране
    text_rect = text.get_rect(center=(gameWidht // 2, gameHeight // 2 - 30))  # расположение текста
    screen.blit(text, text_rect)  # отображение текста
    pygame.display.flip()
    input_box = pygame.Rect(gameWidht // 2 - 100, gameHeight // 2 + 10, 200, 32)  # расположение текста
    color = pygame.Color(DEEPPINK_COLOR)  # цвет ободка и цвет водимых букв
    active = True
    text = ''
    player_name = ''
    clock = pygame.time.Clock()  # Создание объекта часов

    # Цикл для ввода имени
    while active:
        # реакци на нажатия
        for event in pygame.event.get():
            # закрытие окна при нажатии на крестик
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # сохраниение мени при нажатии на enter
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                    player_name = text # Присваиваем введенный текст переменной player_name
                # удалени при нажатии на backspace
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
            # ввод текста с клавиатуры
            elif event.type == pygame.TEXTINPUT:
                text += event.text

        # Отрисовка поля ввода
        txt_surface = font.render(text, True, color)  # текст на экране
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width  # ширина окна будет установлена так, чтобы она была либо не менее 200 пикселей, либо достаточно широкой для отображения текста с запасом в 10 пикселей

        # Заполняем поле ввода цветом фона
        pygame.draw.rect(screen, BACKGROUND_COLOR, input_box)  # рисует прямоугольник на игровом экране
        screen.blit(txt_surface, (input_box.x + 5,
                                  input_box.y + 5))  # отображает текстовую поверхность, отступ в 5 пикселей от верхнего левого угла прямоугольника
        pygame.draw.rect(screen, color, input_box, 2)  # рисует контур прямоугольника

        pygame.display.flip()  # Обновление экрана

        clock.tick(30)  # частотa кадров

    # После выхода из цикла ввода, нарисуйте фон для перекрытия строки ввода
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    assert player_name != '', "Nazwa gracza powinna być niepustym ciągiem znaków"
    return player_name

