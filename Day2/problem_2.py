product_id_ranges = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224','1698522-1698528','446443-446449','38593856-38593862','565653-565659','824824821-824824827','2121212118-2121212124']

product_id_ranges = [
    '69810572-69955342','3434061167-3434167492','76756725-76781020','49-147','296131-386620','910523-946587','34308309-34358652','64542-127485','640436-659023','25-45','35313993-35393518','753722181-753795479','1544-9792','256-647','444628-483065','5863911-6054673','6969623908-6969778569','658-1220','12631-63767','670238-830345','1-18','214165106-214245544','3309229-3355697'
]

# 999 , 1010, 6006006, 20202, 30303, 40404

def is_invalid_id(num):
    str_num = str(num)
    len_of_num = len(str_num)
    window_size = 1
    while window_size <= (len_of_num // 2):
        repeated_part = num % (10**window_size)
        crr_num = num // (10**window_size)
        is_valid = False
        # print(f"Window: {window_size}, repeated_part: {repeated_part}, crr_num: {crr_num}")
        while crr_num > 0:
            temp = crr_num % (10**window_size)
            if temp != repeated_part:
                is_valid = True
                break
            crr_num = crr_num // (10**window_size)
        if not is_valid and len_of_num % window_size == 0:
            return True, window_size
        window_size += 1
    return False, None

sum_of_invalid_id = 0
for product_id in product_id_ranges:
    first_id, last_id = int(product_id.split('-')[0]), int(product_id.split('-')[1])
    for id in range(first_id, last_id+1):
        is_invalid, repeated_window = is_invalid_id(id)
        if is_invalid:
            # print("Repeated number: ", id, " Window Size: ", repeated_window, "Range: ", first_id, "-", last_id)
            sum_of_invalid_id += id

print(sum_of_invalid_id)

# 27187178531 -- Too High