import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
def refresh():
	return pygame.display.flip()

def main():
	
	
	clock = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	#groups
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	#containers
	Shot.containers = (shots, updatable, drawable)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	#sprites
	asteroidfield = AsteroidField()
	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	
	
	
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		updatable.update(dt)
		
		for item in drawable:
			item.draw(screen)

		

		for item in asteroids:
			for shot in shots:
				if item.collision(shot):
					item.split()
					shot.kill()
			if item.collision(player):
				print("Game over!")
				return False
		
		refresh()
		dt = clock.tick(60) / 1000
		


if __name__ == "__main__":
	main()
