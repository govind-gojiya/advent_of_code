import bisect
import sys

# sys.stdin = open('p1_example.txt')
sys.stdin = open('p1.txt')

data = sys.stdin.read().splitlines()

worksheet_ans = []
ans = 0

for i, line in enumerate(data):
    line = line.split(' ')
    if 0 <= i < len(data) - 1:
        crr_nums = [(int(num), int(num)) for num in line if num != '']
        # print(crr_nums)
        if i == 0:
            worksheet_ans = crr_nums
        elif i != len(data) - 1:
            worksheet_ans = [(worksheet_ans[j][0] + num[0], worksheet_ans[j][1] * num[1]) for j, num in enumerate(crr_nums)]
    else:
        # print(worksheet_ans)
        i = 0
        for sign in line:
            if sign != '' and sign == '+':
                ans += worksheet_ans[i][0]
                i += 1
            elif sign != '' and sign == '*':
                ans += worksheet_ans[i][1]
                i += 1

print(ans)