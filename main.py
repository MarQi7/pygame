import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
def refresh():
	return pygame.display.flip()

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		refresh()


if __name__ == "__main__":
	main()
