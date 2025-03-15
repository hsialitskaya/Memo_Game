import os  # операционаая система
import pygame
import random
def start_new_game(picture_size_Widht,picture_size_Height,margin_left,margin_top,padding,columns):
    # Создание списка картинок
    pictures_name = []

    # импорт картинок из папки без расшиения
    for item in os.listdir('images/'):
        pictures_name.append(item.split('.')[0])

    # Чтобы картинки появлялись в разных местах
    random.shuffle(pictures_name)

    # Загружаем картинки в память
    pictures = []
    pictures_rectangle = []  # Делаем из них прямоугольники
    hidden = []  # Картинки спрятаны
    for item in pictures_name:
        image = pygame.image.load(f'images/{item}.jpg')  # Загружаем с расшрением
        image = pygame.transform.scale(image,
                                       (picture_size_Widht, picture_size_Height))  # Сжатие катинок по заданым размерам
        pictures.append(image)
        image_rect = image.get_rect()
        pictures_rectangle.append(image_rect)

    # Расположение картинок
    for i in range(len(pictures_rectangle)):
        pictures_rectangle[i][0] = margin_left + ((picture_size_Widht + padding) * (i % columns))
        pictures_rectangle[i][1] = margin_top + ((picture_size_Height + padding) * (i // columns))
        hidden.append(False)  # изображения скрыты

    assert len(pictures_name) == len(pictures) == len(pictures_rectangle) == len(hidden), "Liczba elementów się nie zgadza"
    return tuple((pictures_name, pictures, pictures_rectangle, hidden))