import bisect
import sys

sys.stdin = open('p1_example.txt')
# sys.stdin = open('p1.txt')

data = sys.stdin.read().splitlines()

ranges = []
ingredient_ids = []

for line in data:
    if '-' in line:
        ranges.append(line)
    elif line.isdigit():
        ingredient_ids.append(int(line))

# print(ranges, ingredient_ids)

# Time Complexity: O(n log n)
def merge_intervals(ranges):
    intervals = []
    for r in ranges:
        a, b = map(int, r.split('-'))
        intervals.append((a, b))

    # print(intervals)
    intervals.sort()  # sort by start --- log n
    # print(intervals)

    # Merge intervals --- n
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged

merged_ranges = merge_intervals(ranges)
high_range = [merge_range[1] for merge_range in merged_ranges]
fresh_ingredient_ids = 0

# Time Complexity: O(m log n) -- m is no of ingredient ids
for id in ingredient_ids:
    i = bisect.bisect_left(high_range, id) # log n
    if i < len(high_range) and i >= 0 and id >= merged_ranges[i][0] and id <= merged_ranges[i][1]:
        fresh_ingredient_ids += 1

# Time Complexity: O(n log n + m log n)
print(f"Total fresh ingredient ids: {fresh_ingredient_ids}")