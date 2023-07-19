from math import floor
INDEX_U = 0
INDEX_R = 1
INDEX_F = 2
INDEX_D = 3
INDEX_L = 4
INDEX_B = 5

def rotate_slice(fl, i, j, k, l, il, dir):
    if dir == 1:
        for x in range(len(il)):
            fl[i][il[x][0]], fl[j][il[x][1]], fl[k][il[x][2]], fl[l][il[x][3]] = fl[l][il[x][3]], fl[i][il[x][0]], fl[j][il[x][1]], fl[k][il[x][2]] 
    elif dir == -1:
        for x in range(len(il)):
            fl[i][il[x][0]], fl[j][il[x][1]], fl[k][il[x][2]], fl[l][il[x][3]] = fl[j][il[x][1]], fl[k][il[x][2]], fl[l][il[x][3]], fl[i][il[x][0]] 
    elif dir == 2:
        for x in range(len(il)):
            fl[i][il[x][0]], fl[j][il[x][1]], fl[k][il[x][2]], fl[l][il[x][3]] = fl[k][il[x][2]], fl[l][il[x][3]], fl[i][il[x][0]], fl[j][il[x][1]]

def rotate_face5x5(fl, dir):
    if dir == 1:
        for i in range(4):        
            fl[i], fl[4+5*i], fl[24-i], fl[20-5*i] = fl[20-5*i], fl[i], fl[4+5*i], fl[24-i]
        for i in range(2):        
            fl[6+i], fl[8+5*i], fl[18-i], fl[16-5*i] = fl[16-5*i], fl[6+i], fl[8+5*i], fl[18-i]
    elif dir == -1:
        for i in range(4):   
            fl[i], fl[4+5*i], fl[24-i], fl[20-5*i] = fl[4+5*i], fl[24-i], fl[20-5*i], fl[i]
        for i in range(2):   
            fl[6+i], fl[8+5*i], fl[18-i], fl[16-5*i] = fl[8+5*i], fl[18-i], fl[16-5*i], fl[6+i]
    elif dir == 2:
        for i in range(4):        
            fl[i], fl[4+5*i], fl[24-i], fl[20-5*i] = fl[24-i], fl[20-5*i], fl[i], fl[4+5*i]
        for i in range(2):        
            fl[6+i], fl[8+5*i], fl[18-i], fl[16-5*i] = fl[18-i], fl[16-5*i], fl[6+i], fl[8+5*i]

def rotate_face3x3(fl, dir):
    if dir == 1:        
        fl[0], fl[2], fl[8], fl[6] = fl[6], fl[0], fl[2], fl[8]
        fl[1], fl[5], fl[7], fl[3] = fl[3], fl[1], fl[5], fl[7]
    elif dir == -1:
        fl[0], fl[2], fl[8], fl[6] = fl[2], fl[8], fl[6], fl[0]
        fl[1], fl[5], fl[7], fl[3] = fl[5], fl[7], fl[3], fl[1]
    elif dir == 2:
        rotate_face3x3(fl, 1)
        rotate_face3x3(fl, 1)

def update_cubestring(fl):
    new_str = ""
    for i in range(6):
        for j in range(len(fl[i])):
            new_str += fl[i][j]
    return new_str

class Edge:
    def __init__(self, str, i, j):
        self.str = str
        self.i = i
        self.j = j
        self.fi = floor(i / 9)
        self.fj = floor(j / 9)
        self.i5 = 6 + (i % 9) + 2 * floor((i % 9) / 3) + 25 * floor(i / 9)
        self.j5 = 6 + (j % 9) + 2 * floor((j % 9) / 3) + 25 * floor(j / 9)
        self.orderedstr = "".join(sorted(str))


    def __str__(self):
        return self.str
class Corner:
    def __init__(self, str, i, j, k):
        self.str = str
        self.i = i
        self.j = j
        self.k = k
        self.fi = floor(i / 9)
        self.fj = floor(i / 9)
        self.jk = floor(i / 9)
        self.i5 = 6 + (i % 9) + 2 * floor((i % 9) / 3) + 25 * floor(i / 9)
        self.j5 = 6 + (j % 9) + 2 * floor((j % 9) / 3) + 25 * floor(j / 9)
        self.k5 = 6 + (k % 9) + 2 * floor((k % 9) / 3) + 25 * floor(k / 9)
        self.orderedstr = "".join(sorted(str))

    def __str__(self):
        return self.str
class Cube:
    def __init__(self, cube_string):
        self.cube_string = cube_string
        self.facelets = [[],[],[],[],[],[]]
        for i in range(25):
            self.facelets[INDEX_U].append(cube_string[INDEX_U * 25 + i])
            self.facelets[INDEX_R].append(cube_string[INDEX_R * 25 + i])
            self.facelets[INDEX_F].append(cube_string[INDEX_F * 25 + i])
            self.facelets[INDEX_D].append(cube_string[INDEX_D * 25 + i])
            self.facelets[INDEX_L].append(cube_string[INDEX_L * 25 + i])
            self.facelets[INDEX_B].append(cube_string[INDEX_B * 25 + i])

    def get_facelets(self):
        return self.facelets
    
    def move(self, move_name):
        outer = True
        inner = False
        move_name = move_name.replace(" ", "")
        m = move_name[0]
        dir = 1
        if move_name[0] == "2":
            outer = False
            inner = True
            m = move_name[1]
        if move_name[-1] == "2":
            dir = 2
            move_name = move_name[:-1]
        elif move_name[-1] == "'":
            dir = -1
            move_name = move_name[:-1]
        if move_name[-1] == "w":
            outer = True
            inner = True
        if outer:
            if m == "U":
                rotate_face5x5(self.facelets[INDEX_U], dir)
                rotate_slice(self.facelets, INDEX_F, INDEX_L, INDEX_B, INDEX_R, [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]], dir)
            if m == "D":
                rotate_face5x5(self.facelets[INDEX_D], dir)
                rotate_slice(self.facelets, INDEX_F, INDEX_R, INDEX_B, INDEX_L, [[24,24,24,24],[23,23,23,23],[22,22,22,22],[21,21,21,21],[20,20,20,20]], dir)
            if m == "L":
                rotate_face5x5(self.facelets[INDEX_L], dir)
                rotate_slice(self.facelets, INDEX_U, INDEX_F, INDEX_D, INDEX_B, [[0,0,0,24],[5,5,5,19],[10,10,10,14],[15,15,15,9],[20,20,20,4]], dir)
            if m == "R":
                rotate_face5x5(self.facelets[INDEX_R], dir)
                rotate_slice(self.facelets, INDEX_U, INDEX_B, INDEX_D, INDEX_F, [[24,0,24,24],[19,5,19,19],[14,10,14,14],[9,15,9,9],[4,20,4,4]], dir)
            if m == "F":
                rotate_face5x5(self.facelets[INDEX_F], dir)
                rotate_slice(self.facelets, INDEX_U, INDEX_R, INDEX_D, INDEX_L, [[20,0,4,24],[21,5,3,19],[22,10,2,14],[23,15,1,9],[24,20,0,4]], dir)
            if m == "B":
                rotate_face5x5(self.facelets[INDEX_B], dir)
                rotate_slice(self.facelets, INDEX_U, INDEX_L, INDEX_D, INDEX_R, [[4,0,20,24],[3,5,21,19],[2,10,22,14],[1,15,23,9],[0,20,24,4]], dir)
        if inner:
            if m == "U":
                rotate_slice(self.facelets, INDEX_F, INDEX_L, INDEX_B, INDEX_R, [[5,5,5,5],[6,6,6,6],[7,7,7,7],[8,8,8,8],[9,9,9,9]], dir)
            if m == "D":
                rotate_slice(self.facelets, INDEX_F, INDEX_R, INDEX_B, INDEX_L, [[19,19,19,19],[18,18,18,18],[17,17,17,17],[16,16,16,16],[15,15,15,15]], dir)
            if m == "L":
                rotate_slice(self.facelets, INDEX_U, INDEX_F, INDEX_D, INDEX_B, [[1,1,1,23],[6,6,6,18],[11,11,11,13],[16,16,16,8],[21,21,21,3]], dir)
            if m == "R":
                rotate_slice(self.facelets, INDEX_U, INDEX_B, INDEX_D, INDEX_F, [[23,1,23,23],[18,6,18,18],[13,11,13,13],[8,16,8,8],[3,21,3,3]], dir)
            if m == "F":
                rotate_slice(self.facelets, INDEX_U, INDEX_R, INDEX_D, INDEX_L, [[15,1,9,23],[16,6,8,18],[17,11,7,13],[18,16,6,8],[19,21,5,3]], dir)
            if m == "B":
                rotate_slice(self.facelets, INDEX_U, INDEX_L, INDEX_D, INDEX_R, [[9,1,15,23],[8,6,16,18],[7,11,17,13],[6,16,18,8],[5,21,19,3]], dir)
        self.cube_string = update_cubestring(self.facelets)

    def alg(self, alg_str):
        move_list = alg_str.split(" ")
        for m in move_list:
            if len(m) > 0:
                self.move(m)

    def get_3x3_repr_cube_string(self):
        output = ""
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    output += self.facelets[i][(j+1)*5 + (k+1)]
        return output

    def get_3x3_repr_str(self):
        output = ""
        for i in range(3):
            output += "      "
            for j in range(3):
                output += self.cube_string[(i+1)*5 + (j+1) + INDEX_U * 25] + " "
            output += "\n" 
        for i in range(3):
            for j in range(3):
                output += self.cube_string[(i+1)*5 + (j+1) + INDEX_L * 25] + " "
            for j in range(3):
                output += self.cube_string[(i+1)*5 + (j+1) + INDEX_F * 25] + " "
            for j in range(3):
                output += self.cube_string[(i+1)*5 + (j+1) + INDEX_R * 25] + " "
            for j in range(3):
                output += self.cube_string[(i+1)*5 + (j+1) + INDEX_B * 25] + " "
            output += "\n"
        for i in range(3):
            output += "      "
            for j in range(3):
                output += self.cube_string[(i+1)*5 + (j+1) + INDEX_D * 25] + " "
            output += "\n"  
        return output

    def __str__(self):
        output = ""
        for i in range(5):
            output += "          "
            for j in range(5):
                output += self.cube_string[i*5 + j + INDEX_U * 25] + " "
            output += "\n"        
        for i in range(5):
            for j in range(5):
                output += self.cube_string[i*5 + j + INDEX_L * 25] + " "
            for j in range(5):
                output += self.cube_string[i*5 + j + INDEX_F * 25] + " "
            for j in range(5):
                output += self.cube_string[i*5 + j + INDEX_R * 25] + " "
            for j in range(5):
                output += self.cube_string[i*5 + j + INDEX_B * 25] + " "
            output += "\n"
        for i in range(5):
            output += "          "
            for j in range(5):
                output += self.cube_string[i*5 + j + INDEX_D * 25] + " "
            output += "\n"   
        return output
    
class CubeRepr:
    def __init__(self, cube_string):
        self.cube_string = cube_string
        self.facelets = [[],[],[],[],[],[]]
        for i in range(9):
            self.facelets[INDEX_U].append(cube_string[INDEX_U * 9 + i])
            self.facelets[INDEX_R].append(cube_string[INDEX_R * 9 + i])
            self.facelets[INDEX_F].append(cube_string[INDEX_F * 9 + i])
            self.facelets[INDEX_D].append(cube_string[INDEX_D * 9 + i])
            self.facelets[INDEX_L].append(cube_string[INDEX_L * 9 + i])
            self.facelets[INDEX_B].append(cube_string[INDEX_B * 9 + i])

    def move(self, move_name):
        outer = True
        inner = False
        move_name = move_name.replace(" ", "")
        m = move_name[0]
        dir = 1
        if move_name[0] == "2":
            outer = False
            inner = True
            m = move_name[1]
        if move_name[-1] == "2":
            dir = 2
            move_name = move_name[:-1]
        elif move_name[-1] == "'":
            dir = -1
            move_name = move_name[:-1]
        if move_name[-1] == "w":
            outer = True
            inner = True
        if outer:
            if m == "U":
                rotate_face3x3(self.facelets[INDEX_U], dir)
            if m == "R":
                rotate_face3x3(self.facelets[INDEX_R], dir)
            if m == "F":
                rotate_face3x3(self.facelets[INDEX_F], dir)
            if m == "D":
                rotate_face3x3(self.facelets[INDEX_D], dir)
            if m == "L":
                rotate_face3x3(self.facelets[INDEX_L], dir)
            if m == "B":
                rotate_face3x3(self.facelets[INDEX_B], dir)
        if inner:
            if m == "U":
                rotate_slice(self.facelets, INDEX_F, INDEX_L, INDEX_B, INDEX_R, [[0,0,0,0],[1,1,1,1],[2,2,2,2]], dir)
            if m == "D":
                rotate_slice(self.facelets, INDEX_F, INDEX_R, INDEX_B, INDEX_L, [[8,8,8,8],[7,7,7,7],[6,6,6,6]], dir)
            if m == "L":
                rotate_slice(self.facelets, INDEX_U, INDEX_F, INDEX_D, INDEX_B, [[0,0,0,8],[3,3,3,5],[6,6,6,2]], dir)
            if m == "R":
                rotate_slice(self.facelets, INDEX_U, INDEX_B, INDEX_D, INDEX_F, [[8,0,8,8],[5,3,5,5],[2,6,2,2]], dir)
            if m == "F":
                rotate_slice(self.facelets, INDEX_U, INDEX_R, INDEX_D, INDEX_L, [[6,0,2,8],[7,3,1,5],[8,6,0,2]], dir)
            if m == "B":
                rotate_slice(self.facelets, INDEX_U, INDEX_L, INDEX_D, INDEX_R, [[2,0,6,8],[1,3,7,5],[0,6,8,2]], dir)
        self.cube_string = update_cubestring(self.facelets)
    
    def alg(self, alg_str):
        move_list = alg_str.split(" ")
        for m in move_list:
            if len(m) > 0:
                self.move(m)

    def get_facelets(self):
        return self.facelets
        
    def get_cube_str(self):
        return self.cube_string

    def __str__(self):
        output = ""
        for i in range(3):
            output += "      "
            for j in range(3):
                output += self.cube_string[i*3 + j + INDEX_U * 9] + " "
            output += "\n"        
        for i in range(3):
            for j in range(3):
                output += self.cube_string[i*3 + j + INDEX_L * 9] + " "
            for j in range(3):
                output += self.cube_string[i*3 + j + INDEX_F * 9] + " "
            for j in range(3):
                output += self.cube_string[i*3 + j + INDEX_R * 9] + " "
            for j in range(3):
                output += self.cube_string[i*3 + j + INDEX_B * 9] + " "
            output += "\n"
        for i in range(3):
            output += "      "
            for j in range(3):
                output += self.cube_string[i*3 + j + INDEX_D * 9] + " "
            output += "\n"   
        return output
    