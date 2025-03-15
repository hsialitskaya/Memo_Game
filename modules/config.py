import pygame

gameWidht = 840
gameHeight = 640
columns = 4
rows = 4
picture_size_Widht = 130
picture_size_Height = 140
padding = 10
margin_left = (gameWidht - ((picture_size_Widht + padding) * columns)) // 2
margin_top = (gameHeight - ((picture_size_Height + padding) * rows)) // 2
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (255, 239, 223)
DEEPPINK_COLOR = pygame.Color('deeppink')
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 36)  # шрифт
game_completed = False
running = False
hidden = False
restart_button_rect1 = None
restart_button_rect2 = None


screen = pygame.display.set_mode((gameWidht, gameHeight))
screen.fill(BACKGROUND_COLOR)
pygame.display.flip()
pygame.display.set_caption("My Game")
gameIcon = pygame.image.load('logo_icon/animal.png')
pygame.display.set_icon(gameIcon)