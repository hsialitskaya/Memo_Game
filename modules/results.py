import pygame

def bubble_sort(dictionary):
    items = list(dictionary.items())
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def test_bubble_sort():
    assert bubble_sort({'A': 5.0, 'B': 3.0, 'C': 7.0}) == [('B', 3.0), ('A', 5.0), ('C', 7.0)]


def show_results(screen, font, gameWidht, gameHeight, results,BACKGROUND_COLOR,DEEPPINK_COLOR,BLACK):

    screen.fill(BACKGROUND_COLOR)
    restart_button_rect1 = pygame.Rect(gameWidht - 450, gameHeight - 60, 200, 50)
    restart_button_color1 = pygame.Color(DEEPPINK_COLOR)
    restart_button_text1 = font.render("Ponownie", True, (255, 255, 255))
    restart_button_text_rect1 = restart_button_text1.get_rect(center=restart_button_rect1.center)
    pygame.draw.rect(screen, restart_button_color1, restart_button_rect1)
    screen.blit(restart_button_text1, restart_button_text_rect1)


    restart_button_rect2 = pygame.Rect(gameWidht - 210, gameHeight - 60, 200, 50)
    restart_button_color2 = pygame.Color(DEEPPINK_COLOR)
    restart_button_text2 = font.render("Koniec", True, (255, 255, 255))
    restart_button_text_rect2 = restart_button_text2.get_rect(center=restart_button_rect2.center)
    pygame.draw.rect(screen, restart_button_color2, restart_button_rect2)
    screen.blit(restart_button_text2, restart_button_text_rect2)

    waiting_for_key = True
    sorted_results = bubble_sort(results)


    header_text = font.render("Wyniki gry", True, BLACK)
    header_rect = header_text.get_rect(center=(gameWidht // 2, 50))
    screen.blit(header_text, header_rect)

    y_position = 100
    result_number = 1
    for player, elapsed_time in sorted_results:
        result_text = f"{result_number}) {player}: {elapsed_time:.2f} sek"
        result_surface = font.render(result_text, True, BLACK)
        result_rect = result_surface.get_rect(topleft=(10, y_position))
        screen.blit(result_surface, result_rect)
        y_position += 30
        result_number += 1

    pygame.display.flip()
    assert restart_button_rect1.width > 0, "Szerokość restart_button_rect1 powinna być większa niż 0."
    assert restart_button_rect2.height > 0, "Wysokość restart_button_rect2 powinna być większa niż 0."
    return restart_button_rect1, restart_button_rect2

