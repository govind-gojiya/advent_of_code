import sys

# sys.stdin = open('p1_example.txt')
sys.stdin = open('p1.txt')

data = sys.stdin.read().splitlines()

ranges = []

for line in data:
    if '-' in line:
        ranges.append(line)

def merge_intervals(ranges):
    intervals = []
    for r in ranges:
        a, b = map(int, r.split('-'))
        intervals.append((a, b))

    # print(intervals)
    intervals.sort()  # sort by start
    # print(intervals)
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged

merged_ranges = merge_intervals(ranges)

total_fresh_ingredient_ids = 0
for valid_range in merged_ranges:
    total_fresh_ingredient_ids += valid_range[1] - valid_range[0] + 1

print(f"Total fresh ingredient ids: {total_fresh_ingredient_ids}")
