import pygame, sys
from simulation import Simulation

pygame.init()

DARK_GRAY = (40, 40, 40)
WIN_WIDTH = 800
WIN_HEIGHT = 800
CELL_SIZE = 20
FPS = 60

# Pygame Setup
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(WIN_WIDTH, WIN_HEIGHT, CELL_SIZE)

font = pygame.font.Font(None, 36)


def main():
    # Pygame Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // CELL_SIZE
                row = pos[1] // CELL_SIZE
                simulation.toggle_cell(col, row)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulation.toggle_sim()
                    if simulation.is_running():
                        pygame.display.set_caption("Simulation: RUNNING")
                    else:
                        pygame.display.set_caption("Simulation: PAUSED")
                if event.key == pygame.K_r:
                    simulation.fill_random()
                if event.key == pygame.K_c:
                    simulation.grid.clear()

        simulation.update()
        simulation.draw(window)

        # Draw the fps
        current_fps = clock.get_fps()
        fps_text = font.render(f"FPS: {current_fps:.2f}", True, pygame.Color("white"))
        window.blit(fps_text, (10, 10))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()