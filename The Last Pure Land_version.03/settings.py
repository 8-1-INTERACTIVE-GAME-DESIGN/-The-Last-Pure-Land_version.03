import pygame
import os

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600
# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)
# enemy path
PATH = [(802, 16),  (801, 55), (802, 75), (802, 98), (802, 122), (800, 142), (792, 165), (777, 186), 
        (757, 193), (731, 195), (705, 190), (678, 188), (656, 185), (628, 183), (607, 188),(587, 197), 
        (571, 214), (562, 233), (558, 276), (557, 321), (537, 330),(515, 338), (494, 353), (480, 370), 
        (459, 412), (439, 414), (416, 416), (395, 418),(375, 414), (354, 410), (330, 401), (312, 382), 
        (289, 365), (262, 346), (230, 344), (198, 340),(172, 331), (149, 314), (128, 291), (105, 270), 
        (81, 256), (61, 258)]
PATH2 = [(1002, 267), (969, 266), (934, 268), (908, 284), (899, 315), (898, 348), (890, 382), (870, 404), 
         (835, 417), (799, 419), (769, 415), (744, 415), (712, 417), (684, 417), (653, 417), (643, 441), 
         (634, 462), (616, 482), (587, 493), (550, 495), (520, 489), (491, 473), (478, 456), (468, 431), 
         (447, 414), (416, 414), (385, 414), (361, 410), (337, 405), (315, 391), (296, 371), (271, 353), 
         (242, 345), (217, 344), (194, 343), (171, 336), (151, 323), (139, 304), (125, 288), (107, 274), 
         (86, 261), (61, 258)]

# base
BASE = pygame.Rect(0, 200, 70, 80)

# image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("images", "Map.png"))
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (40, 40))
HP_IMAGE = pygame.transform.scale(pygame.image.load("images/hp.png"), (40, 40))
#COIN_BLACK = pygame.transform.scale(pygame.image.load("images/dollar_0.png"), (40, 40))
COIN = [pygame.transform.scale(pygame.image.load("images/dollar_1.png"), (40, 40)),
        pygame.transform.scale(pygame.image.load("images/dollar_0.png"), (40, 40))]
WAVE = pygame.transform.scale(pygame.image.load("images/battle.png"), (40, 40))
