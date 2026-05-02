# Maze Game

## Logic and Data Structure

The maze is represented with a 2D array and also to manage the boundaries I used the edge rows and columns as stated in the assignment:

- self.northWall[R+1][C+1]: Stores the integrity of the upper wall. The zeroth row is an edge row representing the bottom edge of the maze

- self.eastWall[R+1][C+1]: Stores the integrity of the right wall. The zeroth column is an edge column representing the left edge of the maze

## Stack based Generation with Depth first search 

The mouse checks neighbors that are located at:

- North

- East

- West

- South 

If a neighbor hasn't been visited the mouse will move there and eat the wall between them

If the mouth reaches dead end it will pop the stack to return to the last cell with unvisited neighbors

## Loom Recording 

This Loom record demonstrates the eating proccess where the maze is being generated dynamically and the solver where the "red dot" mouse finding its way and the "blue dots" marking dead ends

  [![Maze game demo](https://img.shields.io/badge/Video-Demo-green)](https://www.loom.com/share/c7af003caec54ad5a3266214630a75f9)

## Why I used stack instead of queue

Using a stack with the implementation of depth first search will create long paths and it is challenging to do as well. However, using a queue with the implementation of Breadth first search would be simple and short maze with short branches and also it is not that much of a challenge

## Backtracking Solver

- The solver moves randomly through available paths 

- It pushes current positions onto a stack

- When the mouse get into the dead end it will mark the cell blue and backtracks by popping the stack

- The successful path is marked by the red dots currently in the stack

## Author

[Basliel Sisay G/mariyam - UGR/3563/16 (Section - 02)](mailto:jackboy2098@gmail.com)
