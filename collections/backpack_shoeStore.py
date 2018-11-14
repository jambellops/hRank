'''
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the
 shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the  desired by the
 customer and shoeSize, the price of the shoe.
'''
from collections import Counter
moneyEarned = 0
if __name__ == '__main__':
    numShoes = int(input())
    listShoes = Counter(map(int, input().split())) #by shoeSize
    numCustomers = int(input())
    for n in range(numCustomers):
        loopList = list(map(int, input().split())) # list of shoesize and purchase price
        if listShoes[loopList[0]] > 0:
            listShoes[loopList[0]] -= 1
            moneyEarned += loopList[1]
        else:
            moneyEarned += 0

print(moneyEarned)
# minScore = min(scoreList)
# secondLowest = max(scoreList)
# result = []
# for i in outList:
#     if i[1] > minScore and i[1] < secondLowest:
#         secondLowest = i[1]
#         result = [i[0]]
#     elif i[1] > minScore and i[1] == secondLowest:
#         result.append(i[0])
# result.sort()
# for r in result:
#     print(r)
