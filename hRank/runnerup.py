if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

winner = max(arr)
initRunnerUp = min(arr)

for i in range(n):
    if arr[i] > initRunnerUp and arr[i] < winner:
        initRunnerUp = arr[i]

print(initRunnerUp)
