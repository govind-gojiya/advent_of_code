# dial_inputs = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
import sys

sys.stdin = open('problem_1.txt', 'r')

dial_inputs = sys.stdin.read().splitlines()

current_position = 50
zero_dial_position = 0
zero_dial_frequency = 0

for dial in dial_inputs:
    direction = dial[0]
    dial_number = int(dial[1:])
    rotated_dial_number = dial_number // 100
    if rotated_dial_number > 0:
        # print(f'Rotated {rotated_dial_number} times')
        zero_dial_frequency += rotated_dial_number
    dial_number = dial_number % 100
    if direction.lower() == 'l':
        if dial_number > current_position:
            if current_position != 0:
                zero_dial_frequency += 1
            current_position = 100 - (dial_number - current_position)
        else:
            current_position = current_position - dial_number
    else:
        if (dial_number + current_position) >= 100:
            current_position = (dial_number + current_position) % 100
            if current_position != 0:
                zero_dial_frequency += 1
        else:
            current_position = current_position + dial_number

    if current_position == 0:
        zero_dial_frequency += 1
    # print(current_position, zero_dial_frequency)


print(zero_dial_position, zero_dial_frequency)
exit()