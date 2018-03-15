TITLE = 'Jumpy!'

#Basic settings
BLACK  = (0, 0, 0)
WHITE  = (255,255,255)
RED    = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN   = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CHAIN  = (0, 255, 255)

SIZE = WIDTH, HEIGHT = 480, 600
FPS = 60


# Platform settings
PLATFORM_LIST = [(0, HEIGHT - 30),
                 (40, HEIGHT - 150),
                 (50, HEIGHT - 550),
                 (300, HEIGHT - 250),
                 (0, HEIGHT - 350),]
# Player settings
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
PLAYER_JUMP = 25
GRAVITY = 1