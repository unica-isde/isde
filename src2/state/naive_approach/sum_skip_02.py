"""
This solution uses an integer variable to store the state,
and a conditional structure to manage the action and the state transition.

You can implement this solution using a function (#1) or a class (#2).
"""



# 1

def sum_skip_el1(nums, el_to_skip):
    sum_val = 0
    state = 0
    for el in nums:
        if state == 0:
            if el == el_to_skip:
                state = 1
            else:
                sum_val += el
        if state == 1:
            if el == el_to_skip:
                pass
            else:
                state = 0

    return sum_val


# -------------------------------------------------
# 2


class SumSkip:
    def __init__(self, el_to_skip):
        self.el_to_skip = el_to_skip
        self.state = 0
        self.sum_val = 0

    def sum_skip_el(self, el):
        if self.state == 0:
            if el == self.el_to_skip:
                self.state = 1
            else:
                self.sum_val += el
        if self.state == 1:
            if el == self.el_to_skip:
                pass
            else:
                self.state = 0


if __name__ == '__main__':

    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

    list_of_nums = [nums1, nums2, nums3]
    list_of_results = [3, 3, 2]

    for nums, r in zip(list_of_nums, list_of_results):

        print(sum_skip_el1(nums, 13) == r)

        obj = SumSkip(13)
        for el in nums:
            obj.sum_skip_el(el)
        print(obj.sum_val == r)

