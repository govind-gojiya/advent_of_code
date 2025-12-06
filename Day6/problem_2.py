import bisect
import sys

# sys.stdin = open('p1_example.txt')
sys.stdin = open('p1.txt')

data = sys.stdin.read().splitlines()

signs = [sign for sign in data[-1].split(' ') if sign != '']

worksheet = [0] * (len(data[0]) + 1)
ans = 0

for i, line in enumerate(data):
    if i < len(data) - 1:
        for j, digit in enumerate(line):
            # print(j, digit, worksheet)
            if digit.strip() != '':
                worksheet[j] = worksheet[j] * 10 + int(digit)
        
print(worksheet)

ans = 0
sign_index = 0
crr_math = 0 if signs[0] == '+' else 1

for num in worksheet:
    if num != 0:
        if signs[sign_index] == '+':
            crr_math += num
        else:
            crr_math *= num
    else:
        ans += crr_math
        sign_index += 1
        crr_math = 0 if signs[sign_index%len(signs)] == '+' else 1
    # print(ans, crr_math, sign_index, num)

print(ans)