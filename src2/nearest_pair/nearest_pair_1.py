
def idx_sum_is(elements, target):
    idx_solution = (None, None)  # None means 'no solution'
    n = len(elements)
    distance_between_idx = n  # fake value. The maximum possible value for a solution is n-1

    #  for _idx_0 in range(n):
    #      for _idx_1 in range(_idx_0 + 1, n):
    # You can skip the possible solutions that are worse than the previous one.

    for _idx_0 in range(n):
        if distance_between_idx == 1:
            # no better solution is possible
            return idx_solution

        n_elements_to_check = min(distance_between_idx, n - _idx_0)
        for _idx_1 in range(_idx_0 + 1, _idx_0 + n_elements_to_check):
            if elements[_idx_0] + elements[_idx_1] == target:
                idx_solution = (_idx_0, _idx_1)
                distance_between_idx = _idx_1 - _idx_0
                break

    return idx_solution


# TEST idx_sum_is
elements = [1, 2, 3, 4]
targets = [0, 3, 4, 5, 6, 7]
solution = [(None, None), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
for i in range(len(targets)):

    print('\ntarget: ', targets[i])

    idx_0, idx_1 = idx_sum_is(elements, targets[i])
    if idx_0 is None:
        print('target ', targets[i], ': no solution\n')
    else:
        print('POSITIONS (', idx_0, idx_1, '): ', elements[idx_0], '+', elements[idx_1], ' = ',
              elements[idx_0] + elements[idx_1])

    if (solution[i][0] != idx_0) or (solution[i][1] != idx_1):
        print('ERROR!')
