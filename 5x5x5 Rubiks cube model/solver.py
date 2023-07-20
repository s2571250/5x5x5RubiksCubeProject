from cube import Cube, Corner, Edge
import kociemba
ordered_correct_corners = ['FLU', 'FRU', 'BRU', 'BLU', 'DFR', 'BDR', 'BDL', 'DFL']
ordered_correct_edges = ['FU', 'RU', 'BU', 'LU', 'BL', 'FL', 'BR', 'FR', 'DF', 'DR', 'BD', 'DL']
solved_cube_string = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"


def is_valid_3x3x3_state(state):
    try:
        kociemba.solve(state)
        return True
    except Exception:
        return False

def same_piece(p1, p2):
    return sorted(p1) == sorted(p2)

def cube_str_to_pieces(cube_str):
    corners = [cube_str[6]+cube_str[18]+cube_str[38],   # UFL
               cube_str[8]+cube_str[9]+cube_str[20],    # URF
               cube_str[2]+cube_str[45]+cube_str[11],   # UBR
               cube_str[0]+cube_str[36]+cube_str[47],   # ULB
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

def cube_str_to_piecesO(cube_str):
    corners = [Corner(cube_str[6]+cube_str[18]+cube_str[38], 6, 18, 38),   # UFL
               Corner(cube_str[8]+cube_str[9]+cube_str[20], 8, 9, 20),    # URF
               Corner(cube_str[2]+cube_str[45]+cube_str[11], 2, 45, 11),   # UBR
               Corner(cube_str[0]+cube_str[36]+cube_str[47], 0, 36, 47),   # ULB
               Corner(cube_str[29]+cube_str[26]+cube_str[15], 29, 26, 15),  # DFR
               Corner(cube_str[35]+cube_str[17]+cube_str[51], 35, 17, 51),  # DRB
               Corner(cube_str[33]+cube_str[53]+cube_str[42], 33, 53, 42),  # DBL
               Corner(cube_str[27]+cube_str[44]+cube_str[24], 27, 44, 24)]  # DLF
    edges = [Edge(cube_str[7]+cube_str[19], 7, 19),  # UF
             Edge(cube_str[5]+cube_str[10], 5, 10),  # UR
             Edge(cube_str[1]+cube_str[46], 1, 46),  # UB
             Edge(cube_str[3]+cube_str[37], 3, 37),  # UL
             Edge(cube_str[39]+cube_str[50], 39, 50), # LB
             Edge(cube_str[41]+cube_str[21], 41, 21), # LF
             Edge(cube_str[14]+cube_str[48], 14, 48), # RB
             Edge(cube_str[12]+cube_str[23], 12, 23), # RF
             Edge(cube_str[28]+cube_str[25], 28, 25), # DF
             Edge(cube_str[32]+cube_str[16], 32, 16), # DR
             Edge(cube_str[34]+cube_str[52], 34, 52), # DB
             Edge(cube_str[30]+cube_str[43], 30, 43)] # DL
    return corners, edges

def correct_corners_edges(list):
    correct = []
    corners = len(list) == 8
    for c in list:
        ordered = "".join(sorted(set(c)))
        if (len(ordered) == 3 and corners) or (len(ordered) == 2 and not corners):
            if ("U" not in c or "D" not in c) and ("L" not in c or "R" not in c) and ("F" not in c or "B" not in c):
                if ordered not in correct:
                    correct.append(ordered)
    return correct

def no_edge_parity(cube_string):
    nw_cube_str = solved_cube_string
    indices = [1,3,5,7,10,12,14,16,19,21,23,25,28,30,32,34,37,39,41,43,46,48,50,52]
    for i in indices:
        nw_cube_str = nw_cube_str[:i] + cube_string[i] + nw_cube_str[i + 1:]
    return is_valid_3x3x3_state(nw_cube_str)

def no_corner_parity(cube_string):
    nw_cube_str = solved_cube_string
    indices = [0,2,6,8,9,11,15,17,18,20,24,26,27,29,33,35,36,38,42,44,45,47,51,53]
    for i in indices:
        nw_cube_str = nw_cube_str[:i] + cube_string[i] + nw_cube_str[i + 1:]
    return is_valid_3x3x3_state(nw_cube_str)

def NxMoveStr(n, move):
    if n == 1:
        return move + " "
    elif n == 2:
        return move + "2 "
    elif n == 3:
        return move + "' "
    else:
        return ""

def get_most_correct_pieces(cube: Cube):
    best = 0
    bestalg = ""
    ccube = Cube(cube.cube_string)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        for f in range(4):
                            corners, edges = cube_str_to_pieces(ccube.get_3x3_repr_cube_string())
                            correct_corners = correct_corners_edges(corners)
                            correct_edges = correct_corners_edges(edges)
                            total = 3*len(correct_corners)+2*len(correct_edges) 
                            if len(correct_corners) == 8:
                                if not no_corner_parity(ccube.get_3x3_repr_cube_string()): 
                                    total -= 6    
                            if len(correct_edges) == 12:
                                if not no_edge_parity(ccube.get_3x3_repr_cube_string()): 
                                    total -= 4
                            if total > best:  
                                best = total
                                bestalg = NxMoveStr(a, "U") + NxMoveStr(b, "R") + NxMoveStr(c, "F") + NxMoveStr(d, "D") + NxMoveStr(e, "L") + NxMoveStr(f, "B")
                            ccube.move("B")
                        ccube.move("L")
                    ccube.move("D")
                ccube.move("F")
            ccube.move("R")
        ccube.move("U")
    return best, bestalg

def check_pieces(cube : Cube, solution):
    _, bestalg = get_most_correct_pieces(cube)
    cube.alg(bestalg)
    corners, edges = cube_str_to_pieces(cube.get_3x3_repr_cube_string())
    correct_corners = correct_corners_edges(corners)
    correct_edges = correct_corners_edges(edges)
    corner_parity, edge_parity = 0, 0
    if len(correct_corners) == 8:
        if not no_corner_parity(cube.get_3x3_repr_cube_string()): 
            corner_parity = -2    
    if len(correct_edges) == 12:
        if not no_edge_parity(cube.get_3x3_repr_cube_string()): 
            edge_parity -= 2
    return len(correct_corners), corner_parity, len(correct_edges), edge_parity, bestalg
 
def find_simple_3cycle(wrong_corners, corners_to_make, start_wc, start_ctm, excess, need):
    for wc1 in wrong_corners:
        if wc1 == start_wc:
            continue
        for ctm1 in corners_to_make:
            if ctm1 == start_ctm:
                continue
            need1 = set(ctm1.str) - set(wc1.str) 
            excess1 = set(wc1.str) - set(ctm1.str)   
            if need1 == excess:
                for wc2 in wrong_corners:
                    if wc2 == start_wc or wc2 == wc1:
                        continue
                    for ctm2 in corners_to_make:
                        if ctm2 == start_ctm or ctm2 == ctm1:
                            continue
                        need2 = set(ctm2.str) - set(wc2.str) 
                        excess2 = set(wc2.str) - set(ctm2.str)   
                        if need2 == excess1 and excess2 == need:
                            return [[start_wc, start_ctm, list(need)], [wc1, ctm1, list(need1)], [wc2, ctm2, list(need2)]]
    return []

def find_other_3cycle(wrong_corners, corners_to_make, start_wc, start_ctm, excess, need):
    for wc1 in wrong_corners:
        if wc1 == start_wc:
            continue
        for ctm1 in corners_to_make:
            if ctm1 == start_ctm:
                continue
            excess1 = set(wc1.str) - set(ctm1.str)  
            # print(excess, need, excess1) 
            if need == excess1:
                for wc2 in wrong_corners:
                    if wc2 == start_wc or wc2 == wc1:
                        continue
                    for ctm2 in corners_to_make:
                        if ctm2 == start_ctm or ctm2 == ctm1:
                            continue
                        excess2 = set(wc2.str) - set(ctm2.str)   
                        return [[start_wc, start_ctm, list(need)], [wc2, ctm2, list(excess)], [wc1, ctm1, list(excess2)]]
    return []

def find_2cycle(wrong_corners, corners_to_make, start_wc, start_ctm, excess, need):
    for wc1 in wrong_corners:
        if wc1 == start_wc:
            continue
        for ctm1 in corners_to_make:
            if ctm1 == start_ctm:
                continue
            excess1 = set(wc1.str) - set(ctm1.str)  
            if need == excess1:
                return [[start_wc, start_ctm, list(need)], [wc1, ctm1, list(excess)]]
    return []

def cycleNpieces(cube_str, mycycle):    
    for x in range(len(mycycle)):
        index = 0
        excess = mycycle[(x + 1) % len(mycycle)][2][0]
        if mycycle[x][0].str[0] == excess:
            index = mycycle[x][0].i5
        elif mycycle[x][0].str[1] == excess:
            index = mycycle[x][0].j5
        elif mycycle[x][0].str[2] == excess:
            index = mycycle[x][0].k5
        cube_str = cube_str[:index] + mycycle[x][2][0] + cube_str[index + 1:]
    return cube_str   

def step1(cube : Cube, solution):
    _, bestalg = get_most_correct_pieces(cube)
    cube.alg(bestalg)
    step1corners(cube, solution)
    #step1edges(cube, solution)

def step1corners(cube : Cube, solution):    
    cornersO, _ = cube_str_to_piecesO(cube.get_3x3_repr_cube_string())
    correct_cornersO, _ = cube_str_to_piecesO(solved_cube_string)
    correct_corners_dir = {} 
    corners_to_make = []
    for c in correct_cornersO:
        correct_corners_dir[c.orderedstr] = c
        corners_to_make.append(c)
    wrong_corners = [] 
    wrong_corners_dict = {}
    for c in cornersO:
        if c.orderedstr not in ordered_correct_corners:
            wrong_corners.append(c)
            wrong_corners_dict[c.str] = c
        else:
            if correct_corners_dir[c.orderedstr] in corners_to_make:
                corners_to_make.remove(correct_corners_dir[c.orderedstr])
            else:
                wrong_corners.append(c)
                wrong_corners_dict[c.str] = c
    
    if len(corners_to_make) > 0:
        ctm_dict = {}
        lowest_freq = 3
        lowest_freq_corner = corners_to_make[0].str
        for ctm in corners_to_make:
            lowest_count = 3
            lowest_diff_corners = []
            for wc in wrong_corners:
                diff_count = len(set(ctm.str) - set(wc.str))
                # print(wc.str, ctm.str, diff_count)
                if diff_count < lowest_count:
                    lowest_count = diff_count
                    lowest_diff_corners = [wc]
                elif diff_count == lowest_count:
                    lowest_diff_corners.append(wc)
            # print("===")
            freq = len(lowest_diff_corners)
            if freq < lowest_freq:
                lowest_freq = freq
                lowest_freq_corner = ctm.str
            ctm_dict[ctm.str] = [ctm, lowest_count, lowest_diff_corners]

        start_wc = ctm_dict[lowest_freq_corner][2][0]
        start_ctm = ctm_dict[lowest_freq_corner][0]
        
        
        # print(">", start_wc.str, start_ctm.str)
        
        need = set(start_ctm.str) - set(start_wc.str)

        excess = list(set(start_wc.str) - set(start_ctm.str))   
        wc_dict = {}
        for i in range(3):
            if start_wc.str[i] in wc_dict:
                wc_dict[start_wc.str[i]] += 1
            else:
                wc_dict[start_wc.str[i]] = 0
        for char in wc_dict.keys():
            for _ in range(wc_dict[char]):
                excess.append(char)
        excess = set(excess)

        if len(excess) == 1 and len(wrong_corners) == 2:
            my2cycle = find_2cycle(wrong_corners, corners_to_make, start_wc, start_ctm, excess, need)
            if len(my2cycle) == 2:
                cube = Cube(cycleNpieces(cube.cube_string, my2cycle))
                solution.append(2)
                step1corners(cube, solution)
            else:
                print("error")
                return 0
        else:
        # check if anyone needs the excess
            my3cycle = find_simple_3cycle(wrong_corners, corners_to_make, start_wc, start_ctm, excess, need)
            if len(my3cycle) == 3:
                cube = Cube(cycleNpieces(cube.cube_string, my3cycle))
                solution.append(3)
                step1corners(cube, solution)
            else:
                find_other_3cycle(wrong_corners, corners_to_make, start_wc, start_ctm, excess, need)
                if len(my3cycle) == 3:
                    cube = Cube(cycleNpieces(cube.cube_string, my3cycle))
                    solution.append(3)
                    step1corners(cube, solution)
                else:
                    print("error")
                    return 0
    else:
        no_parity = no_corner_parity(cube.get_3x3_repr_cube_string())
        if not no_parity:
            cube_str_copy = cube.cube_string
            a,b,c = cube_str_copy[18],cube_str_copy[34],cube_str_copy[56]
            cube_str_copy = cube_str_copy[:18] + b + cube_str_copy[18 + 1:]
            cube_str_copy = cube_str_copy[:34] + c + cube_str_copy[34 + 1:]
            cube_str_copy = cube_str_copy[:56] + a + cube_str_copy[56 + 1:]
            if no_corner_parity(Cube(cube_str_copy).get_3x3_repr_cube_string()):
                print("clockwise parity")
                solution.append(3)
            else:
                cube_str_copy = cube.cube_string
                a,b,c = cube_str_copy[18],cube_str_copy[34],cube_str_copy[56]
                cube_str_copy = cube_str_copy[:18] + c + cube_str_copy[18 + 1:]
                cube_str_copy = cube_str_copy[:34] + a + cube_str_copy[34 + 1:]
                cube_str_copy = cube_str_copy[:56] + b + cube_str_copy[56 + 1:]
                if no_corner_parity(Cube(cube_str_copy).get_3x3_repr_cube_string()):
                    print("counter-clockwise parity")
                    solution.append(3)
                else:
                    print("parity error")
                    return 0
            cube = Cube(cube_str_copy)
        print(solution)
        print("done")


        
                                

    # corners, edges = cube_str_to_pieces(cube.get_3x3_repr_cube_string())
    # correct_corners = correct_corners_edges(corners)
    # correct_edges = correct_corners_edges(edges)
    # corners_to_make = list(set(ordered_correct_corners) - set(correct_corners))
    # edges_to_make = list(set(ordered_correct_edges) - set(correct_edges))
    # corners_wrong = []
    # for c in corners:
    #     if not "".join(sorted(c)) in correct_corners:
    #         corners_wrong.append(c)
    # # edges_wrong = list(set(edges) - set(correct_edges))
    # excess_need_list = {}
    # if len(correct_corners) < 8:
    #     for i in range(len(corners_wrong)):
    #         tmp = {}
    #         for j in range(len(corners_to_make)):
    #             tmp[corners_to_make[j]] = [list(set(corners_wrong[i]) - set(corners_to_make[j])), list(set(corners_to_make[j]) - set(corners_wrong[i]))]
    #         excess_need_list[corners_wrong[i]] = tmp
        
        
    #     bestWrongCorner = {}
    #     for cornerWrong, v in excess_need_list.items():
    #         for cornerToMake,excessNeed in v.items():
    #             if cornerToMake not in bestWrongCorner:
    #                 bestWrongCorner[cornerToMake] = [[cornerWrong, len(excessNeed[0])]]
    #             elif len(excessNeed[0]) < bestWrongCorner[cornerToMake][0][1]:
    #                 bestWrongCorner[cornerToMake] = [[cornerWrong, len(excessNeed[0])]]
    #             elif len(excessNeed[0]) == bestWrongCorner[cornerToMake][0][1]:
    #                 bestWrongCorner[cornerToMake].append([[cornerWrong, len(excessNeed[0])]])
    #     print("=======")
    #     minV = len(corners_to_make) + 1
    #     bestStart = []
    #     for k, v in bestWrongCorner.items():
    #         if len(v) < minV:
    #             minV = len(v)
    #             bestStart = [v[0][0], k]
    #     print(bestStart)
    #     cycle = []
    #     excessNeedStart = excess_need_list[bestStart[0]][bestStart[1]]
    #     cycle = [excessNeedStart[0][0], excessNeedStart[1][0]]
    #     cyclePieces = [bestStart[0]]
    #     for k, v in excess_need_list.items():
    #         if k is not bestStart[0]:
    #             for toMake, excessNeed in v.items():
    #                 for i in range(len(excessNeed[0])):
    #                     if excessNeed[0][i] == excessNeedStart[1][0]:
    #                         print(k, toMake, excessNeed[0][i], excessNeed[1][i])
    #         # print(k, v)

    # if len(correct_edges) < 12:
    #     pass

def step1edges(cube : Cube, solution):    
    _, edgesO = cube_str_to_piecesO(cube.get_3x3_repr_cube_string())
    _, correct_edgesO = cube_str_to_piecesO(solved_cube_string)
    correct_edges_dir = {} 
    edges_to_make = []
    for c in edgesO:
        correct_edges_dir[c.orderedstr] = c
        edges_to_make.append(c)
    wrong_edges = [] 
    wrong_edges_dict = {}
    for c in edgesO:
        if c.orderedstr not in ordered_correct_edges:
            wrong_edges.append(c)
            wrong_edges_dict[c.str] = c
        else:
            if correct_edges_dir[c.orderedstr] in edges_to_make:
                edges_to_make.remove(correct_edges_dir[c.orderedstr])
            else:
                wrong_edges.append(c)
                wrong_edges_dict[c.str] = c
    
    if len(edges_to_make) > 0:
        ctm_dict = {}
        lowest_freq = 2
        lowest_freq_corner = edges_to_make[0].str
        for etm in edges_to_make:
            lowest_count = 2
            lowest_diff_corners = []
            for we in wrong_edges:
                diff_count = len(set(etm.str) - set(we.str))
                # print(wc.str, ctm.str, diff_count)
                if diff_count < lowest_count:
                    lowest_count = diff_count
                    lowest_diff_corners = [we]
                elif diff_count == lowest_count:
                    lowest_diff_corners.append(we)
            # print("===")
            freq = len(lowest_diff_corners)
            if freq < lowest_freq:
                lowest_freq = freq
                lowest_freq_corner = etm.str
            ctm_dict[etm.str] = [etm, lowest_count, lowest_diff_corners]

        start_we = ctm_dict[lowest_freq_corner][2][0]
        start_etm = ctm_dict[lowest_freq_corner][0]
        
        
        # print(">", start_wc.str, start_ctm.str)
        
        need = set(start_etm.str) - set(start_we.str)

        excess = list(set(start_we.str) - set(start_etm.str))   
        we_dict = {}
        for i in range(3):
            if start_we.str[i] in we_dict:
                we_dict[start_we.str[i]] += 1
            else:
                we_dict[start_we.str[i]] = 0
        for char in we_dict.keys():
            for _ in range(we_dict[char]):
                excess.append(char)
        excess = set(excess)

        if len(excess) == 1 and len(wrong_edges) == 2:
            my2cycle = find_2cycle(wrong_edges, edges_to_make, start_we, start_etm, excess, need)
            if len(my2cycle) == 2:
                cube = Cube(cycleNpieces(cube.cube_string, my2cycle))
                solution.append(2)
                step1corners(cube, solution)
            else:
                print("error")
                return 0
        else:
        # check if anyone needs the excess
            my3cycle = find_simple_3cycle(wrong_edges, edges_to_make, start_we, start_etm, excess, need)
            if len(my3cycle) == 3:
                cube = Cube(cycleNpieces(cube.cube_string, my3cycle))
                solution.append(3)
                step1corners(cube, solution)
            else:
                find_other_3cycle(wrong_edges, edges_to_make, start_we, start_etm, excess, need)
                if len(my3cycle) == 3:
                    cube = Cube(cycleNpieces(cube.cube_string, my3cycle))
                    solution.append(3)
                    step1corners(cube, solution)
                else:
                    print("error")
                    return 0
    else:
        no_parity = no_edge_parity(cube.get_3x3_repr_cube_string())
        if not no_parity:
            cube_str_copy = cube.cube_string
            a,b = cube_str_copy[13],cube_str_copy[32]
            cube_str_copy = cube_str_copy[:13] + b + cube_str_copy[13 + 1:]
            cube_str_copy = cube_str_copy[:32] + a + cube_str_copy[32 + 1:]
            if no_corner_parity(Cube(cube_str_copy).get_3x3_repr_cube_string()):
                print("edge flip parity")
                solution.append(2)
            else:
                cube_str_copy = cube.cube_string
                a,b,c,d = cube_str_copy[17],cube_str_copy[57],cube_str_copy[67],cube_str_copy[82]
                cube_str_copy = cube_str_copy[:17] + d + cube_str_copy[17 + 1:]
                cube_str_copy = cube_str_copy[:57] + c + cube_str_copy[57 + 1:]
                cube_str_copy = cube_str_copy[:67] + b + cube_str_copy[67 + 1:]
                cube_str_copy = cube_str_copy[:82] + a + cube_str_copy[82 + 1:]
                if no_corner_parity(Cube(cube_str_copy).get_3x3_repr_cube_string()):
                    print("edge parity")
                    solution.append(3)
                    solution.append(3)
                else:
                    print("parity error")
                    return 0
            cube = Cube(cube_str_copy)
        print(solution)
        print("done")

def step2(cube, solution):
    pass

def step3(cube, solution):
    pass

def step4(cube, solution):
    pass

def solve(cube : Cube):
    solution = []
    step1(cube, solution)
    # step2(cube, solution)
    # step3(cube, solution)
    # step4(cube, solution)
    # return cube, solution