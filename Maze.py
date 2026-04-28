import pygame
import random

Row = 20
Column = 20
Cell_length = 30
Width = Column * Cell_length
Height = Row * Cell_length
Speed = 60

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

class Maze:
    def __init__(self, rows, columns):
        self.Row = rows
        self.Column = columns
        self.northWall = []
        for i in range(rows +1):
            self.northWall.append([])
            for j in range(columns +1):
                self.northWall[i].append(1)
        
        self.eastWall = []
        for i in range(rows +1):
            self.eastWall.append([])
            for j in range(columns+1):
                self.eastWall[i].append(1)

        self.visited = []
        for i in range(rows+1):
            self.visited.append([])
            for j in range(columns +1):
                self.visited[i].append(False)