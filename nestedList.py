if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

scores = student_marks[query_name]

avg = 0
for i in scores:
    avg += i

average = avg/(len(scores))
print(format(average, '.2f')
