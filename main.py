import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    group_upd = pygame.sprite.Group()
    group_draw = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (group_upd, group_draw)
    Asteroid.containers = (asteroids, group_upd, group_draw)
    Shot.containers = (shots, group_upd, group_draw)
    AsteroidField.containers = (group_upd,)
    asteroid = AsteroidField()
    ravi = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    dt = 0

    while   True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        group_upd.update(dt)
        
        for a in asteroids:
            if ravi.collision(a):
                print("Game Over!")
                return
        
        for a in asteroids:
            for s in shots:
                if a.collision(s):
                    
                    s.kill()
                    a.split()
                    break
            
        screen.fill("black")

        for entity in group_draw:
            entity.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
