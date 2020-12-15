import state as st


class SumSkip:  # THIS IS THE 'CONTEXT'

    def __init__(self, value_to_skip):
        self.state = st.StateSum()
        self.sum_val = 0
        self.value_to_skip = value_to_skip

    def process_input(self, v):
        self.state.process_input(self, v)

    def set_state(self, new_state):
        self.state = new_state

    def sum(self, v):
        self.sum_val += v


if __name__ == '__main__':

    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

    list_of_nums = [nums1, nums2, nums3]
    list_of_results = [3, 3, 2]

    for nums, r in zip(list_of_nums, list_of_results):
        s = SumSkip(13)

        for el in nums:
            s.process_input(el)

        print(s.sum_val == r)
