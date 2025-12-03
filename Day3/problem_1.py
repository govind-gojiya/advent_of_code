import sys

# sys.stdin = open('p1_example.txt')
sys.stdin = open('p1.txt')

banks = sys.stdin.read().splitlines()

total_max_joltage = 0

for bank in banks:
    num = int(bank)
    max_post_digit = [0] * len(bank)
    crr_max_digit = rnum = 0

    for i in range(len(bank) - 1, -1, -1):
        temp = num % 10
        rnum = rnum * 10 + temp
        if temp > crr_max_digit:
            crr_max_digit = temp
        num = num // 10
        max_post_digit[i] = crr_max_digit
    
    # print(max_post_digit)
    bank_max_joltage = 0
    for i in range(1, len(bank)):
        temp = rnum % 10
        joltage = temp * 10 + max_post_digit[i]
        # print(joltage, bank_max_joltage, max_post_digit[i])
        if joltage > bank_max_joltage:
            bank_max_joltage = joltage
        rnum = rnum // 10

    total_max_joltage += bank_max_joltage

print("Total joltage: ", total_max_joltage)
    
