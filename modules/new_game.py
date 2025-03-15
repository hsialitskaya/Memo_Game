import os
import pygame
import random
def start_new_game(picture_size_Widht,picture_size_Height,margin_left,margin_top,padding,columns):

    pictures_name = []


    for item in os.listdir('images/'):
        pictures_name.append(item.split('.')[0])

    random.shuffle(pictures_name)


    pictures = []
    pictures_rectangle = []
    hidden = []
    for item in pictures_name:
        image = pygame.image.load(f'images/{item}.jpg')
        image = pygame.transform.scale(image,
                                       (picture_size_Widht, picture_size_Height))
        pictures.append(image)
        image_rect = image.get_rect()
        pictures_rectangle.append(image_rect)

    for i in range(len(pictures_rectangle)):
        pictures_rectangle[i][0] = margin_left + ((picture_size_Widht + padding) * (i % columns))
        pictures_rectangle[i][1] = margin_top + ((picture_size_Height + padding) * (i // columns))
        hidden.append(False)

    assert len(pictures_name) == len(pictures) == len(pictures_rectangle) == len(hidden), "Liczba elementów się nie zgadza"
    return tuple((pictures_name, pictures, pictures_rectangle, hidden))