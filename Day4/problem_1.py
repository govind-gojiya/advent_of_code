import sys

# sys.stdin = open('p1_example.txt')
sys.stdin = open('p1.txt')

paper_rolls_data = sys.stdin.read().splitlines()

paper_rolls = []

for roll_line in paper_rolls_data:
    crr_line = []
    for roll in roll_line:
        if roll == '@':
            crr_line.append(1)
        else:
            crr_line.append(0)
    paper_rolls.append(crr_line)

total_accessible_roll = 0
total_col = len(paper_rolls[0])
total_row = len(paper_rolls)

# print("Paper rolls")
# print(paper_rolls)

def is_accessible(r, c):
    adjecent = 0
    pre_row = pre_col = False
    post_row = post_col = False

    if r - 1 > -1:
        pre_row = True

    if c - 1 > -1:
        pre_col = True
    
    if r + 1 < total_row:
        post_row = True

    if c + 1 < total_col:
        post_col = True

    if pre_row:
        adjecent += paper_rolls[r-1][c] # 2
        if pre_col:
            adjecent += paper_rolls[r-1][c-1] # 1
        if post_col:
            adjecent += paper_rolls[r-1][c+1] # 3
    
    if post_row:
        adjecent += paper_rolls[r+1][c] # 7
        if pre_col:
            adjecent += paper_rolls[r+1][c-1] # 6
        if post_col:
            adjecent += paper_rolls[r+1][c+1] # 8

    if pre_col:
        adjecent += paper_rolls[r][c-1] # 4

    if post_col:
        adjecent += paper_rolls[r][c+1] # 5

    # print("For ", r, " ", c, " - ", adjecent)
    return adjecent < 4
    
for i in range(total_row):
    for j in range(total_col):
        if paper_rolls[i][j] and is_accessible(i, j):
            total_accessible_roll += 1

print("Total accessible rolls: ", total_accessible_roll)
