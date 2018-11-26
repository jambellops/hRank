if __name__ == '__main__':
    outList = []
    scoreList = []
    for _ in range(int(input())):
        inList = []
        name = input()
        inList.append(name)
        score = float(input())
        inList.append(score)
        outList.append(inList)
        scoreList.append(score)

minScore = min(scoreList)
secondLowest = max(scoreList)
result = []
for i in outList:
    if i[1] > minScore and i[1] < secondLowest:
        secondLowest = i[1]
        result = [i[0]]
    elif i[1] > minScore and i[1] == secondLowest:
        result.append(i[0])
result.sort()
for r in result:
    print(r)
