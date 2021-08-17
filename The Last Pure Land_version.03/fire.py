import pygame
import random
import math
import os
import random
from random import randint
from random import uniform
from settings import fire_PATH_1,fire_PATH_2, fire_frame_BASE
from color_settings import *
global wave

wave = 0
pygame.init()
FIRE_IMAGE = pygame.image.load(os.path.join("images", "fire_ball.png"))
class Fire:
    def __init__(self):
        self.path = fire_PATH_2
        self.path_index = 0
        self.move_count = 0
        self.stride = 10.2
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.path_index = 0
        self.move_count = 0

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count
        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]
class Fire_1(Fire):
    def __init__(self):
        self.path = fire_PATH_2
        global wave
        self.path_index = 0
        self.move_count = 0
        if wave == 2:
            self.stride = 10.5
        else:
            self.stride = 10.2
        self.image = pygame.transform.scale(FIRE_IMAGE, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.path_index = 0
        self.move_count = 0


class FireGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 60   # (unit: frame)
        self.__reserved_members = []
        self.__expedition = []

    def advance(self, model):
        self.campaign()
        for fire in self.__expedition:
            fire.move()
            # delete the object when it reach the base
            if fire_frame_BASE.collidepoint(fire.rect.centerx, fire.rect.centery):
                self.retreat(fire)
#                 if model.hp <= 0:
#                     model.game_over()

    def campaign(self):
        """Enemy go on an expedition."""
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num):
        """Generate the enemies for next wave"""
        global wave
        #rand_num = 0
        #enemy_ground = [Enemy1(), Enemy2(), Enemy3()]
        #en = random.choice(enemy_ground)
        if self.is_empty():
            wave +=1
            for i in range(num):#迴圈
                self.__reserved_members.append(Fire_1())#append進去
            return True
            

    def get(self):
        """Get the enemy list"""
        return self.__expedition

    def is_empty(self):
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.__expedition else True

    def retreat(self, enemy):
        """Remove the enemy from the expedition"""
        self.__expedition.remove(enemy)





