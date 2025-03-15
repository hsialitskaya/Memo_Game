import pygame
import sys

def get_player_name(font, gameWidht, gameHeight, screen, DEEPPINK_COLOR, BACKGROUND_COLOR):
    text = font.render("Wpisz swoje imię:", True, (0, 0, 0))
    text_rect = text.get_rect(center=(gameWidht // 2, gameHeight // 2 - 30))
    screen.blit(text, text_rect)
    pygame.display.flip()
    input_box = pygame.Rect(gameWidht // 2 - 100, gameHeight // 2 + 10, 200, 32)
    color = pygame.Color(DEEPPINK_COLOR)
    active = True
    text = ''
    player_name = ''
    clock = pygame.time.Clock()


    while active:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                    player_name = text

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

            elif event.type == pygame.TEXTINPUT:
                text += event.text


        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width


        pygame.draw.rect(screen, BACKGROUND_COLOR, input_box)
        screen.blit(txt_surface, (input_box.x + 5,
                                  input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

        clock.tick(30)


    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    assert player_name != '', "Nazwa gracza powinna być niepustym ciągiem znaków"
    return player_name

