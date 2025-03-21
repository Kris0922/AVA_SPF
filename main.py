import pygame
import subprocess


def draw_button(screen, rect, text, font, color1, color2, border_color):
    pygame.draw.rect(screen, border_color, rect, border_radius=10)
    gradient = pygame.Surface((rect.width, rect.height))
    for y in range(rect.height):
        blend = y / rect.height
        r = int((1 - blend) * color1[0] + blend * color2[0])
        g = int((1 - blend) * color1[1] + blend * color2[1])
        b = int((1 - blend) * color1[2] + blend * color2[2])
        pygame.draw.line(gradient, (r, g, b), (0, y), (rect.width, y))
    screen.blit(gradient, (rect.x, rect.y))

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


def main():
    pygame.init()

    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Algorithm Visualizer")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE_LIGHT = (100, 150, 255)
    BLUE_DARK = (0, 0, 200)
    RED_LIGHT = (255, 100, 100)
    RED_DARK = (200, 0, 0)
    BORDER_COLOR = BLACK

    font = pygame.font.SysFont("comicsans", 30)
    title_font = pygame.font.SysFont("comicsans", 35)

    sorting_button = pygame.Rect(150, 140, 300, 50)
    pathfinding_button = pygame.Rect(100, 220, 400, 50)

    running = True
    while running:
        screen.fill(WHITE)

        title_text = title_font.render("Choose the desired visualization", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
        screen.blit(title_text, title_rect)

        draw_button(screen, sorting_button, "Sorting Algorithms", font, BLUE_LIGHT, BLUE_DARK, BORDER_COLOR)
        draw_button(screen, pathfinding_button, "Pathfinding Algorithms", font, RED_LIGHT, RED_DARK, BORDER_COLOR)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sorting_button.collidepoint(event.pos):
                    subprocess.run(["python", "sorting.py"])
                elif pathfinding_button.collidepoint(event.pos):
                    subprocess.run(["python", "pathFinder.py"])

    pygame.quit()


if __name__ == "__main__":
    main()
