#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Arturs Kurzemnieks
# artursk
# artursk@kth.se

from dubins import *
import math
import random

MAX_STEER = math.pi / 4.

TARGET_CHECK_FREQUENCY = 10
CHECK_TIME = 3

class RRT:
    def __init__(self, car):
        self.car = car

        self._random_iteration = 0

        self.vertices = [(car.x0, car.y0)]
        self.edges = []

    def random_point(self):
        if self._random_iteration % TARGET_CHECK_FREQUENCY == 0:
            self._random_iteration = 0
            return self.car.xt, self.car.yt
        else:
            self._random_iteration += 1
            x = random.uniform(self.car.xlb, self.car.xub)
            y = random.uniform(self.car.ylb, self.car.yub)

            while not self.car._environment.obstacle_free(x, y):
                x = random.uniform(self.car.xlb, self.car.xub)
                y = random.uniform(self.car.ylb, self.car.yub)
            
            return x, y

    def find_closest_vertex(self, x,y):
        closest = self.vertices[0]
        closest_dist = math.sqrt((x - closest[0])**2 + (y - closest[1])**2)

        for i, vert in enumerate(self.vertices[1:]):
            dist = math.sqrt((x - vert[0])**2 + (y - vert[1])**2)
            if dist < closest_dist:
                closest_dist = dist
                closest = i
        return closest

    def expand(self):
        xt, yt = self.random_point()
        x0, y0 = self.find_closest_vertex(xt, yt)

        # get Dubins path


def solution(car):
    random.seed()

    x, y = car.x0, car.y0
    theta = 0

    ''' <<< write your code below >>> '''
    controls=[]
    times=[0]

    rrt = RRT(car)

    for t in range(1, 1001):
        x, y, theta = step(car, x, y, theta, 0)
        controls.append(0)
        times.append(t * 0.01)

    ''' <<< write your code below >>> '''

    return controls, times
