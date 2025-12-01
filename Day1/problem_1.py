# dial_inputs = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
import sys

sys.stdin = open('problem_1.txt', 'r')

dial_inputs = sys.stdin.read().splitlines()

current_position = 50
zero_dial_frequency = 0

for dial in dial_inputs:
    direction = dial[0]
    dial_number = int(dial[1:])
    dial_number = dial_number % 100
    if direction.lower() == 'l':
        if dial_number > current_position:
            current_position = 100 - (dial_number - current_position)
        else:
            current_position = current_position - dial_number
    else:
        if (dial_number + current_position) >= 100:
            current_position = (dial_number + current_position) % 100
        else:
            current_position = current_position + dial_number

    if current_position == 0:
        zero_dial_frequency += 1

print(zero_dial_frequency)
exit()