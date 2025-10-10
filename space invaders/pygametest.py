import pygame

#initialize all imported pygame modules
pygame.init()

#create a window of size 800x600
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("My Pygame Window")
icon = pygame.image.load('icon.png')  # Ensure you have an 'icon.png' file in the same directory
pygame.display.set_icon(icon)

#player image
playerImage = pygame.image.load('player.png')  # Ensure you have a 'player.png' file in the same directory
playerImage = pygame.transform.scale(playerImage, (100,80))  # Resize image if necessary
playerX = 370
playerY = 510
playerX_change = 0

def player(x,y):
    screen.blit(playerImage, (x, y))

#game loop
running = True
while running:

    screen.fill((0, 128, 255))  # Fill the screen with a color (RGB)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 1
            if event.key == pygame.K_RIGHT:
                playerX_change += 1
            if event.key == pygame.K_UP:
                playerY -= 10
            if event.key == pygame.K_DOWN:
                playerY += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerX_change -= 1
        #if event.type == pygame.KEYUP:
         #   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          #      playerX_change = 0 #issue with this line that it stops movement when either key is released so when you press one then the other and then release the 

    playerX += playerX_change
    if playerX <=10:
            playerX = 10
    elif playerX >=690:
            playerX = 690

    player(playerX,playerY)  # Draw the player
    pygame.display.update()    # Update the display
    
