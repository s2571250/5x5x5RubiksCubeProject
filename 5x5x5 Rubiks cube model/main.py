import kociemba
import random
import solver
from cube import Cube, CubeRepr

solved_cube_string = "UUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLBBBBBBBBBBBBBBBBBBBBBBBBB"

valid_moves = ["U ", "2U ", "2Uw ", "U' ", "2U' ", "2Uw' ", "U2 ", "2U2 ", "2Uw2 ",
               "R ", "2R ", "2Rw ", "R' ", "2R' ", "2Rw' ", "R2 ", "2R2 ", "2Rw2 ",
               "F ", "2F ", "2Fw ", "F' ", "2F' ", "2Fw' ", "F2 ", "2F2 ", "2Fw2 ",
               "D ", "2D ", "2Dw ", "D' ", "2D' ", "2Dw' ", "D2 ", "2D2 ", "2Dw2 ",
               "L ", "2L ", "2Lw ", "L' ", "2L' ", "2Lw' ", "L2 ", "2L2 ", "2Lw2 ",
               "B ", "2B ", "2Bw ", "B' ", "2B' ", "2Bw' ", "B2 ", "2B2 ", "2Bw2 "]

outer_moves = ["U ", "U' ", "U2 ", "R ", "R' ", "R2 ", "F ", "F' ", "F2 ",
               "D ", "D' ", "D2 ", "L ", "L' ", "L2 ", "B ", "B' ", "B2 "]

valid_corners = ['UFL', 'URF', 'UBR', 'ULB', 'DFR', 'DRB', 'DBL', 'DLF']
valid_edges = ['UF', 'UR', 'UB', 'UL', 'LB', 'LF', 'RB', 'RF', 'DF', 'DR', 'DB', 'DL']

def scramble_cube(cube, n):
    scramble = ""
    for _ in range(n):
        new_move = random.choice(valid_moves)
        cube.move(new_move)
        scramble += new_move
    return scramble

def is_solved(cube : Cube):
    return cube.cube_string == solved_cube_string


# cube = Cube("LUUDDFFDDDRUUDLDFFDBBRBLUBLFLBLLBUUURRLFURLBUDBBRULFDDRFUDBFFLFUBDBBDBUDRDRRFBRFUDLFRRDDFLFRRLUULLRLFRUFDLURRLUBLURBFFRBBUDBFRBFFDRLRBUDFBULLUBLRFDDBL")
# cube = Cube("BUDUURDUURUUUURBLBLDLLLDFDLDUFBRFRURRRUUDUFUFBFFLBDBBBLLFDDLDLFFBFULFFRLLFRDDULDDRFFLRLDDUBFBLUUDDUUUDRRBDLRDULDLRFRDBBRLUFFFRFLBLRBDBRBBBRFRBLRBRFBBF")

# print(cube.cube_string)
# solution = solver.solve(cube)
# print(solution)

#cube = Cube("RFLBRDLFFRRBUFRDDLURBRFRUFDDDUUDUULDLRDLFDDLURLUFFDBDULFLFBLBBFRLRBBRRBFBRBLLRFUFFDUBFRDFLUULBULBDFLDLULRDLRBDFRLDUUFBRBULRUDFUFDFBDURBBUBUUBRLFRDLBDB")
# N = 25
# for x in range(N): 
#     cube = Cube(solved_cube_string)
#     scramble_cube(cube, 60)
#     print(cube.cube_string)
#     solution = solver.solve(cube)
#     print(solution)

# cube = Cube(solved_cube_string)
# solver.solve(cube)

def count_len(result):
    score = 0
    for r in result:
        if r == 2:
            score += 2
        if r == 3:
            score += 1
    return score

freq = {None: 0}
N = 100
f = open("simulation/states.txt", "r")
for x in range(N):
    state = f.readline().strip()
    cube = Cube(state)
    result = solver.solve(cube)
    if result == None:
        freq[None] += 1
    elif count_len(result) in freq:
        freq[count_len(result)] += 1
    else: 
        freq[count_len(result)] = 1
    fw = open("simulation_results.txt", "a")
    fw.write(str(result) + "\n")
    fw.close()
f.close()
print(freq)

# cube = Cube(solved_cube_string)
# corners, edges = solver.cube_str_to_pieces(cube.get_3x3_repr_cube_string())
# correct_corners = solver.correct_corners_edges(corners)
# correct_edges = solver.correct_corners_edges(edges)
# print(corners, correct_corners, len(correct_corners))
# print(edges, correct_edges, len(correct_edges))
# print(set(solver.ordered_correct_corners) - set(correct_corners))
# print(set(solver.ordered_correct_edges) - set(correct_edges))

# freqC = {}
# freqE = {}

# for x in range(100):
#     cube = Cube(solved_cube_string)
#     scramble = scramble_cube(cube, 60)
#     bestC, parC, bestE, parE, alg = solver.check_pieces(cube, [])
#     if (bestC + parC) not in freqC:
#         freqC[bestC + parC] = 1
#     else:
#         freqC[bestC + parC] += 1

#     if (bestE + parE) not in freqE:
#         freqE[bestE + parE] = 1
#     else:
#         freqE[bestE + parE] += 1
#     f = open("firstStep.txt", "a")
#     f.write(cube.cube_string + "\n")
#     f.write(str(bestC + bestE) + ":" + str(bestC) + "," + str(bestE) + "|" + str(parC) + "," + str(parE) + "|" + alg + "\n")
#     f.close()
# print(freqC, freqE)
# {16: 250, 15: 493, 14: 208, 17: 37, 13: 9, 18: 3}
# {2: 4, 3: 69, 4: 278, 5: 378, 6: 224, 7: 47 } {7: 1, 8: 28, 9: 164, 10: 411, 11: 302, 12: 94}
# {3: 5, 4: 127, 5: 365, 6: 386, 7: 112, 8: 5 } {6: 3, 7: 20, 8: 129, 9: 322, 10: 306, 11: 187, 12: 33}