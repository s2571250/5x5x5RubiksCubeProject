import kociemba
import random
import itertools
from cube import Cube, CubeRepr

solved_cube_string = "UUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLBBBBBBBBBBBBBBBBBBBBBBBBB"

valid_moves = ["U ", "2U ", "2Uw ", "U' ", "2U' ", "2Uw' ", "U2 ", "2U2 ", "2Uw2 ",
               "R ", "2R ", "2Rw ", "R' ", "2R' ", "2Rw' ", "R2 ", "2R2 ", "2Rw2 ",
               "F ", "2F ", "2Fw ", "F' ", "2F' ", "2Fw' ", "F2 ", "2F2 ", "2Fw2 ",
               "D ", "2D ", "2Dw ", "D' ", "2D' ", "2Dw' ", "D2 ", "2D2 ", "2Dw2 ",
               "L ", "2L ", "2Lw ", "L' ", "2L' ", "2Lw' ", "L2 ", "2L2 ", "2Lw2 ",
               "B ", "2B ", "2Bw ", "B' ", "2B' ", "2Bw' ", "B2 ", "2B2 ", "2Bw2 "]

valid_corners = ['UFL', 'URF', 'UBR', 'ULB', 'DFR', 'DRB', 'DBL', 'DLF']
valid_edges = ['UF', 'UR', 'UB', 'UL', 'LB', 'LF', 'RB', 'RF', 'DF', 'DR', 'DB', 'DL']

def is_valid_3x3x3_state(state):
    try:
        kociemba.solve(state)
        return True
    except Exception:
        return False

def scramble_cube(cube, n):
    scramble = ""
    for _ in range(n):
        new_move = random.choice(valid_moves)
        cube.move(new_move)
        scramble += new_move
    return scramble

def is_solved(cube : Cube):
    return cube.cube_string == solved_cube_string

def cube_str_to_pieces(cube_str):
    corners = [cube_str[6]+cube_str[18]+cube_str[38],   # UFL
               cube_str[8]+cube_str[9]+cube_str[20],    # URF
               cube_str[2]+cube_str[45]+cube_str[11],   # UBR
               cube_str[0]+cube_str[36]+cube_str[46],   # ULB
               cube_str[29]+cube_str[26]+cube_str[15],  # DFR
               cube_str[35]+cube_str[17]+cube_str[51],  # DRB
               cube_str[33]+cube_str[53]+cube_str[42],  # DBL
               cube_str[27]+cube_str[44]+cube_str[24]]  # DLF
    edges = [cube_str[7]+cube_str[19],  # UF
             cube_str[5]+cube_str[10],  # UR
             cube_str[1]+cube_str[46],  # UB
             cube_str[3]+cube_str[37],  # UL
             cube_str[39]+cube_str[50], # LB
             cube_str[41]+cube_str[21], # LF
             cube_str[14]+cube_str[48], # RB
             cube_str[12]+cube_str[23], # RF
             cube_str[28]+cube_str[25], # DF
             cube_str[32]+cube_str[16], # DR
             cube_str[34]+cube_str[52], # DB
             cube_str[30]+cube_str[43]] # DL
    return corners, edges

def correct_corners_edges(list):
    correct = []
    corners = len(list) == 8
    for c in list:
        if (len(set(c)) == 3 and corners) or (len(set(c)) == 2 and not corners):
            if ("U" not in c or "D" not in c) and ("L" not in c or "R" not in c) and ("F" not in c or "B" not in c):
                correct.append(c)
    return set(correct)


print(is_valid_3x3x3_state("DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD"))
print(is_valid_3x3x3_state("UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"))
print(is_valid_3x3x3_state("URUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"))

# 2Rw F' 2Uw L B2 2Dw 2Lw' F' 2Lw' D' 2Bw R' 2Dw2 L' U 2Bw' 2Dw2 L' 2Fw' 2Uw2 B' D' R U 2Uw2 D2 F' D 2Dw2 F2 2Lw2 U2 2Lw2 U' R2 2Uw2 2Lw2 2Fw2 2Lw2 B2 U 2Dw2 L 2Fw2 2Dw2 R2 2Fw2 R2 D2 R 2Bw2 U2 2Fw2 U2 L 2Bw2 B' U2 B' U F U B2 R' U L B' U2 L B2 R' D2 L' D2 F2
cube = Cube("BBRLRBULBUDRUFRFLLLLDDFLLBUFRUFDDFRDRRBLDFLFFDDBDDRRUDUURFRRBLFUFBLBDRBRRLFRFUBLFDRDBDUDDUFLBBLFBLRRLULUBFUDULLULBDBRRBRUDRLUFFBLDUFUUDBDBFFURFBUFBUDL")
print(cube)
cube.alg("2Rw F' 2Uw L B2 2Dw 2Lw' F' 2Lw' D' 2Bw R' 2Dw2 L' U 2Bw' 2Dw2 L' 2Fw' 2Uw2 B' D' R U 2Uw2 D2 F' D 2Dw2 F2 2Lw2 U2 2Lw2 U' R2 2Uw2 2Lw2 2Fw2 2Lw2 B2 U 2Dw2 L 2Fw2 2Dw2 R2 2Fw2 R2 D2 R 2Bw2 U2 2Fw2 U2 L 2Bw2 B' U2 B' U F U B2 R' U L B' U2 L B2 R' D2 L' D2 F2")
print(cube)
# scramble_cube(cube, 60)
# cube3x3repr = CubeRepr(cube.get_3x3_repr_cube_string())
# corners, edges = cube_str_to_pieces(cube3x3repr.get_cube_str())
# print(corners, edges)
# print(correct_corners_edges(corners))
# print(correct_corners_edges(edges))

for x in range(1000):
    cube = Cube(solved_cube_string)
    scramble = scramble_cube(cube, 60)
    f = open("states.txt", "a")
    f.write(cube.cube_string + "\n")
    f.close()
