import bowling

scores1 = [[3,3],[9,0],[3,4],[1,4],[7,0],[8,0],[4,6],[6,4],[2,7],[10,0],[8,1]]
print ("input", scores1)
expected1 = [6,15,22,27,34,42,58,70,79,98]
a1 = bowling.bowlScore(scores1)
b1 = expected1
print ("output", a1)
print ("expected", expected1)
print ("is same:", a1==b1)

scores2 = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,10]]
print ("input", scores2)
expected2 = [30,60,90,120,150,180,210,240,270,300]
a2 = bowling.bowlScore(scores2)
b2 = expected2
print ("output", a2)
print ("expected", expected2)
print ("is same:", a2==b2)

scores3 = [[1,2],[6,3],[10,0]]
print ("input", scores3)
expected3 = [3,12,22]
a3 = bowling.bowlScore(scores3)
b3 = expected3
print ("output", a3)
print ("expected", expected3)
print ("is same:", a3==b3)

scores4 = [[6,4],[7,3],[8,2],[9,1],[1,9],[2,8],[3,7],[4,6],[5,5],[6,4],[7,0]]
print ("input", scores4)
expected4 = [17,35,54,65,77,90,104,119,135,152]
a4 = bowling.bowlScore(scores4)
b4 = expected3
print ("output", a4)
print ("expected", expected4)
print ("is same:", a4==b4)

URL = "http://13.74.31.101/api/points"
g = bowling.get(URL)
results = bowling.bowlScore(g["points"])
res = bowling.post(g["token"], results , URL)
print (res)
