def _partial_solution(elements, idx_0, distance_between_idx, target):
    # Starting from idx_0, returns the idx_1, such that
    # elements[idx_0] +  elements[idx_0] == target
    #
    # returns None if the solution does not exist
    #
    # distance_between_idx is the distance between the indices of the partial solution found so far

    idx_1 = idx_0 + 1
    while (idx_1 - idx_0 < distance_between_idx) and (idx_1 < len(elements)):
        cond = (elements[idx_0] + elements[idx_1]) == target
        if cond:
            return idx_1
        else:
            idx_1 += 1
    return None


def idx_sum_is(elements, target):
    idx_solution = (None, None)
    n = len(elements)
    distance_between_idx = n  # fake value. The maximum possible value for a solution is n-1

    for _idx_0 in range(n - 1):

        _idx_1 = _partial_solution(elements, _idx_0, distance_between_idx, target)

        if _idx_1 is not None:
            # A possible solution. It is better that the previous one.
            # But we need to look for better solutions
            idx_solution = (_idx_0, _idx_1)
            distance_between_idx = _idx_1 - _idx_0

            if distance_between_idx == 1:
                # no better solution is possible
                return idx_solution

    return idx_solution



## TEST PARTIAL SOLUTION
elements = [0, 1, 2]
targets = [0, 1, 2, 3, 4]
solutions = [None, None]
solutions[0] = [None, 1, 2, None, None]  # correct value of idx_1 when idx_0==0
solutions[1] = [None, None, None, 2, None]  # correct value of idx_1 when idx_0==1

distance_between_solution = len(elements)
for idx_0 in range(len(elements) - 1):
    for i in range(len(targets)):
        idx_1 = _partial_solution(elements, idx_0, distance_between_solution, targets[i])
        if (solutions[idx_0][i] != idx_1):
            print('\nERROR! IDX_1= ', idx_1, 'should be ', solutions[idx_0][i])
print('\nOK\n')




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
        print('POSITIONS (', idx_0, idx_1, '):', elements[idx_0], '+', elements[idx_1], ' = ',
              elements[idx_0] + elements[idx_1])

    if (solution[i][0] != idx_0) or (solution[i][1] != idx_1):
        print('ERROR!')
