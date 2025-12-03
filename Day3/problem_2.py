import sys

# sys.stdin = open('p1_example.txt')
sys.stdin = open('p1.txt')

banks = sys.stdin.read().splitlines()

def find_max_12_digit_subsequence(s):
    length = len(s)
    result_chars = []
    start_index = 0
    
    for current_digit_pos in range(12):
        end_bound = length - (12 - current_digit_pos - 1)   
        max_digit_char = ''
        best_index = -1

        for i in range(start_index, end_bound):
            if s[i] > max_digit_char:
                max_digit_char = s[i]
                best_index = i
            
            if max_digit_char == '9':
                break
        
        result_chars.append(max_digit_char)
        start_index = best_index + 1
        
    return int("".join(result_chars))

total_max_joltage = 0

for bank in banks:
    num = int(bank)
    joltage = find_max_12_digit_subsequence(bank)
    print("For bank: ", bank, "\nMax Jotlage: ", joltage)
    total_max_joltage += joltage

print("Total joltage: ", total_max_joltage)
    