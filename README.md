# 5x5x5RubiksCubeProject
Software used for bachelors assignment: 5x5x5 Rubik's cube: Heuristic approach

main.py is used to run the main simulation
cube.py contains all created classes. These classes are: cube, edge and corner. 
It also contains all functions needed to perform moves on the cube.
solver.py contains the (not finished) implementation of the proposed algorithm.
Each step of this algorithm is a different function

The input to create a cube is a string of 150 characters in the following form:

          U U U U U 
          U U U U U 
          U U U U U 
          U U U U U 
          U U U U U 
L L L L L F F F F F R R R R R B B B B B 
L L L L L F F F F F R R R R R B B B B B 
L L L L L F F F F F R R R R R B B B B B 
L L L L L F F F F F R R R R R B B B B B 
L L L L L F F F F F R R R R R B B B B B 
          D D D D D 
          D D D D D 
          D D D D D 
          D D D D D
          D D D D D

The first 25 characters of the string represents the facelets on the U face
The second 25 characters of the string represents the facelets on the R face
The third 25 characters of the string represents the facelets on the F face
The fourth 25 characters of the string represents the facelets on the D face
The fifth 25 characters of the string represents the facelets on the L face
The sixth 25 characters of the string represents the facelets on the B face
A solved cube is represented as:

UUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLBBBBBBBBBBBBBBBBBBBBBBBBB