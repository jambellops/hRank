data = open('data', mode='r')
entry = []
for line in data:
    entry.append(line)
def check(a):
    try:
        end=len(a)-1
        if end == 0:
            print('last number')
            return "Yes"
        elif a[1]>a[0] and a[1]>a[end]:
            print('ends less than left plus one')
            return "No"
        elif a[end-1]>a[0] and a[end-1]>a[end]:
            print('ends less than right minus one')
            return "No"
        elif a[0]>=a[end]:
            if a[0] > a[end]:
                print('left greater, recursing')
                return check(a[1:])
            elif a[0] == a[end]:
                print('ends equal, recursing')
                return check(a[1:end])
        elif a[end]> a[0]:
            print('right greater, recursing')
            return check(a[:end])
    except:
        return "Yes"
# T = int(input())
T = int(entry.pop(0))
for case in range(T):
    # n = int(input())
    # inList = list(input().split())
    n = int(entry.pop(0))
    inList = list(entry.pop(0).split())

    print(check(inList))

close('data')
