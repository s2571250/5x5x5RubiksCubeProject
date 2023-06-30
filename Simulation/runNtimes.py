import subprocess

#result = subprocess.run(["python", "test.py"])

N = 1000
f = open("scrambles.txt", "r")
for x in range(N):
    scramble = f.readline().strip()
    fw = open("output.txt", "a")
    fw.write(str(x+1) + ". " + scramble + "\n")
    fw.close()
    result = subprocess.run(["bash", "-c", "./rubiks-cube-solver.py --state "+scramble+" 2> /dev/null 1>> output.txt"])
f.close()