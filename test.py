import bowling

URL = "http://13.74.31.101/api/points"
g = bowling.get(URL)
results = bowling.bowlScore(g["points"])
res = bowling.post(g["token"], results , URL)
print ("responce from get followed by post:\n", res, "\n")

print ("general test")
scores1 = [[3,3],[9,0],[3,4],[1,4],[7,0],[8,0],[4,6],[6,4],[2,7],[10,0],[8,1]]
print ("input", scores1)
expected1 = [6,15,22,27,34,42,58,70,79,98]
res1 = bowling.bowlScore(scores1)
print ("output", res1, "\nis correct:", res1==expected1,"\n")

print("test all strikes")
scores2 = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,10]]
print ("input", scores2)
expected2 = [30,60,90,120,150,180,210,240,270,300]
res2 = bowling.bowlScore(scores2)
print ("output", res2, "\nis correct:", res2==expected2,"\n")

print ("test unfinished ends on strike")
scores3 = [[1,2],[10,0],[10,0]]
print ("input", scores3)
expected3 = [3,23,33]
res3 = bowling.bowlScore(scores3)
print ("output", res3,"\nis correct:", res3==expected3,"\n")

print("test variations of spares")
scores4 = [[6,4],[7,3],[8,2],[9,1],[0,10],[10,0],[3,7],[0,10],[0,10],[6,4],[7,0]]
print ("input", scores4)
expected4 = [17,35,54,64,84,104,114,124,140,157]
res4 = bowling.bowlScore(scores4)
print ("output", res4, "\nis correct:", res4==expected4,"\n")

print ("test unfinished ends on spare")
scores5 = [[1,2],[3,4],[6,4]]
print ("input", scores5)
expected5 = [3,10,20]
res5 = bowling.bowlScore(scores5)
print ("output", res5,"\nis correct:", res5==expected5,"\n")


print("test variation of strikes, spares and zeroes")
scores6 = [[0,0],[10,0],[10,0],[0,10],[0,10],[0,0],[10,0],[10,0],[10,0],[0,0]]
print ("input", scores6)
expected6 = [0,20,40,50,60,60,90,110,120,120]
res6 = bowling.bowlScore(scores6)
print ("output", res6, "\nis correct:", res6==expected6,"\n")
