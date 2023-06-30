from cube import Cube
from main import is_solved

f = open('output.txt', 'r')
lines = f.readlines()
f.close()

even = True
state = ""
succes = 0
fail = 0
for line in lines:
    words = line.replace("\n","").split(" ")
    if even:
        state = words[1]
    else:
        cube = Cube(state)
        if words[0] == "Solution:": 
            words.pop(0)
            for m in words:
                cube.move(m)
        elif words[0] == "Exception:":
            cube.alg("2Rw F' 2Uw L B2 2Dw 2Lw' F' 2Lw' D' 2Bw R' 2Dw2 L' U 2Bw' 2Dw2 L' 2Fw' 2Uw2 B' D' R U 2Uw2 D2 F' D 2Dw2 F2 2Lw2 U2 2Lw2 U' R2 2Uw2 2Lw2 2Fw2 2Lw2 B2 U 2Dw2 L 2Fw2 2Dw2 R2 2Fw2 R2 D2 R 2Bw2 U2 2Fw2 U2 L 2Bw2 B' U2 B' U F U B2 R' U L B' U2 L B2 R' D2 L' D2 F2")
        if is_solved(cube):
            succes += 1
        else:
            fail += 1
    even = not even
print(succes / (succes + fail), fail / (succes + fail))