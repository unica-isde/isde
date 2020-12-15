from unittest import TestCase
from sum_skip import State_version_a, State_version_b


class TestState_a(TestCase):
    def test_process_input(self):
        nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
        nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
        nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

        list_of_nums = [nums1, nums2, nums3]
        list_of_results = [3, 3, 2]

        for nums, r in zip(list_of_nums, list_of_results):
            obj = State_version_a(13)

            for el in nums:
                obj.process_input(el)
            self.assertEqual(obj.sum_val, r)


class TestState_b(TestCase):
    def test_process_input(self):
        nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
        nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
        nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

        list_of_nums = [nums1, nums2, nums3]
        list_of_results = [3, 3, 2]

        for nums, r in zip(list_of_nums, list_of_results):
            obj = State_version_b(13)

            for el in nums:
                obj.process_input(el)
            self.assertEqual(obj.sum_val, r)
