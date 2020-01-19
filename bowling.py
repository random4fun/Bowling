import requests
import json

def roundSum(p):
    return p[0]+p[1]

def bowlSum(p):
    if roundSum(p[0]) < 10:
        return roundSum(p[0])
    if p[0][0] == 10:
            if roundSum(p[1]) > 10: #bonus roll are in same frame even if first is strike
                return 10 + roundSum(p[1])
            if p[1][0] == 10:
                    return 20+p[2][0]
            return 10+roundSum(p[1])
    return roundSum(p[0]) + p[1][0]
        
def bowlScore(plist):
    results = [0]           #zeroes are added to avoid idex out of bounds error
    plist.append([0,0])
    while plist != []:
        results.append(bowlSum(plist)+results[-1])
        plist.pop(0)
    results.pop(0)
    results.pop(-1)
    if (len(results) ==  11):   #removes eleventh frame in case of strike or spare in final round
        results.pop(-1)
    return results

  
def get(URL):
    r = requests.get(url = URL)
    data = r.json()
    return data

def post(token, results, URL):
    re = {"token": token, "points": json.dumps(results)}
    r = requests.post(url = URL, data = re)
    return r.text
