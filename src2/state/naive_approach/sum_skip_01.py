# 1

def sum_skip_el1(nums, el_to_skip):
    sum_val = 0
    last_el = None
    for el in nums:
        if el != el_to_skip and last_el != el_to_skip:
            sum_val += el
        last_el = el
    return sum_val


# -------------------------------------------------
# 2


def _go_to_the_next(nums, el_to_skip, i):
    len_nums = len(nums)
    while nums[i] == el_to_skip:
        i += 1
        if i == len_nums:
            break
    return i


def sum_skip_el2(nums, el_to_skip):
    sum_val = 0
    i = 0
    len_nums = len(nums)
    while i < len_nums:
        if nums[i] != el_to_skip:
            sum_val += nums[i]
            i += 1
        else:
            i = _go_to_the_next(nums, el_to_skip, i) + 1
    return sum_val


# -------------------------------------------------

# 3

def sum_skip_el3(nums, el_to_skip):
    sum_val = 0
    len_nums = len(nums)

    for i in range(len_nums - 1, 0, -1):
        if nums[i] != el_to_skip and nums[i - 1] != el_to_skip:
            sum_val += nums[i]

    if nums[0] != el_to_skip:
        sum_val += nums[0]

    return sum_val


# ------------------------------------------
# 4

# attention, there is a bug! can you find it?

def sum_skip_el4(nums, el_to_skip):
    len_nums = len(nums)
    tmp_nums = [0] + nums

    sum_val = sum([tmp_nums[i + 1]
                   for i in range(len_nums)
                   if tmp_nums[i] != el_to_skip and tmp_nums[i + 1] != el_to_skip])

    return sum_val


if __name__ == '__main__':
    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

    list_f = [sum_skip_el1, sum_skip_el2, sum_skip_el3, sum_skip_el4]

    for f in list_f:
        print(f(nums1, 13) == 3)
        print(f(nums2, 13) == 3)
        print(f(nums3, 13) == 2)
