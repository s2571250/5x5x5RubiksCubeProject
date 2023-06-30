import numpy as np
f = open('results.txt', 'r')
lines = f.readlines()
 
count = 0
succes = 0
fail = 0
movecount = []
for line in lines:
    if count % 2 == 1:
        words = line.strip().split(" ")
        if words[0] == "Solution:":
            succes += 1
            movecount.append(len(words)-1)
        elif words[0] == "Exception:":
            fail += 1
    count += 1
print(succes / (succes + fail), np.mean(np.array(movecount)))
# 0.999 79.13213213213213