import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Constants for the game window and map size
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
ZOMBIE_SPEED = 2
FOOD_RESTORE = 20
START_HEALTH = 100
START_HUNGER = 100
START_AMMO = 30
GUN_DAMAGE = 25
MELEE_DAMAGE = 10
ZOMBIE_DAMAGE = 10
START_CLOTHES = "T-shirt"

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
DARK_BLUE = (0, 0, 139)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Pygame screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Survival Sandbox")
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.health = START_HEALTH
        self.hunger = START_HUNGER
        self.ammo = START_AMMO
        self.weapon = "melee"  # default weapon is melee
        self.clothes = START_CLOTHES
        self.speed = PLAYER_SPEED

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        health_text = font.render(f"Health: {self.health}", True, WHITE)
        hunger_text = font.render(f"Hunger: {self.hunger}", True, WHITE)
        ammo_text = font.render(f"Ammo: {self.ammo}", True, WHITE)
        clothes_text = font.render(f"Clothes: {self.clothes}", True, WHITE)
        surface.blit(health_text, (10, 10))
        surface.blit(hunger_text, (10, 40))
        surface.blit(ammo_text, (10, 70))
        surface.blit(clothes_text, (10, 100))

# Zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = ZOMBIE_SPEED

    def update(self, player):
        direction_x = player.rect.centerx - self.rect.centerx
        direction_y = player.rect.centery - self.rect.centery
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance != 0:
            direction_x /= distance
            direction_y /= distance
        self.rect.x += direction_x * self.speed
        self.rect.y += direction_y * self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Food item class
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Gun class
class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 10))
        self.image.fill(DARK_BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = 10

    def update(self):
        self.rect.x += self.angle[0] * self.speed
        self.rect.y += self.angle[1] * self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Game class
class Game:
    def __init__(self):
        self.player = Player()
        self.zombies = pygame.sprite.Group()
        self.foods = pygame.sprite.Group()
        self.guns = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.player)
        self.spawn_food()
        self.spawn_gun()
        self.spawn_zombies()

    def spawn_zombies(self):
        for _ in range(5):
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            zombie = Zombie(x, y)
            self.zombies.add(zombie)
            self.all_sprites.add(zombie)

    def spawn_food(self):
        for _ in range(3):
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            food = Food(x, y)
            self.foods.add(food)
            self.all_sprites.add(food)

    def spawn_gun(self):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        gun = Gun(x, y)
        self.guns.add(gun)
        self.all_sprites.add(gun)

    def handle_collisions(self):
        # Player - Zombie collisions
        for zombie in self.zombies:
            if self.player.rect.colliderect(zombie.rect):
                self.player.health -= ZOMBIE_DAMAGE
                self.zombies.remove(zombie)
                self.all_sprites.remove(zombie)

        # Player - Food collisions
        for food in self.foods:
            if self.player.rect.colliderect(food.rect):
                self.player.hunger = min(self.player.hunger + FOOD_RESTORE, 100)
                self.foods.remove(food)
                self.all_sprites.remove(food)

        # Player - Gun collisions
        for gun in self.guns:
            if self.player.rect.colliderect(gun.rect):
                self.player.weapon = "gun"
                self.guns.remove(gun)
                self.all_sprites.remove(gun)

        # Bullet - Zombie collisions
        for bullet in self.bullets:
            for zombie in self.zombies:
                if bullet.rect.colliderect(zombie.rect):
                    self.zombies.remove(zombie)
                    self.all_sprites.remove(zombie)
                    self.bullets.remove(bullet)
                    self.all_sprites.remove(bullet)

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        # Update zombies
        for zombie in self.zombies:
            zombie.update(self.player)

        # Update bullets
        for bullet in self.bullets:
            bullet.update()

        self.handle_collisions()

        # Decrease hunger over time
        self.player.hunger -= 0.1
        if self.player.hunger <= 0:
            self.player.health -= 1

    def draw(self):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)
        self.player.draw(screen)
        pygame.display.update()

    def check_game_over(self):
        if self.player.health <= 0:
            return True
        return False

    def run(self):
        running = True
        while
