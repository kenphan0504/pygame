# Pygame Program in General has have the following:
# handle the events by calling either pygame.event.pump() or pygame.event.get().
# update the game states and positions of objects dependent on the input events and time (respectively frames)
# clear the entire display or draw the background
# draw the entire scene (blit all the objects)
# update the display by calling either pygame.display.update() or pygame.display.flip()
# limit frames per second to limit CPU usage with pygame.time.Clock.tick

import pygame
pygame.init()

# creating a window (height, width) for the game 
screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))

# set the name for the window/game
pygame.display.set_caption("First Game")

clock = pygame.time.Clock()
run = True

# making a character
x = 50
y = 50
width = 40
height = 50
vel = 5 # velocity

isJump = False
jumpCount = 10

while run:
    pygame.time.delay(50)
    # handle events
    # an event in pygame is anything that happens from the user i.e a mouse click
    for event in pygame.event.get(): # get a list of all the event that happens
        if event.type == pygame.QUIT: # if we click the red X, the game closes
            run = False

    # update game objects
    # [...]

    # detect key pressed and update change 
    # get_pressed() returns a sequence of boolean values representing the state of every key on the keyboard.
    # Use the key constant values to index the array. A True value means that the button is pressed.
    # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_height - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10: # this is to check when to set the falling of the jump
            neg = 1          # multiplying by negative will give positive, to go down
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # clear display to black (0, 0, 0) for each instance of change, if fill() isn't called, the shape will "drag" instead of "move"
    win.fill((0, 0, 0))
    # draw a rectangle of color red (255,0,0) and size (width, height) on coordinates (x, y)
    # coordinates starts at top left: i.e top left (0, 0), top right (500, 0), bottom left (0, 500), bottom right (500, 500)
    pygame.draw.rect(win, (255,0, 0), (x, y, width, height))

    # update this display to show what's changed i.e a rectangle is drawn
    # pygame.flip() would update the entire display
    # update() with no argument update the entire display, same as flip()
    # update(arg) takes in drawn object via fns like rect(), or blit() and update only the new drawn area
    pygame.display.update() 

    # clear display
    # win.fill((0, 0, 0))

    # limit frames per second
    clock.tick(60)

pygame.quit()
