import state as st


class SumSkip:  # THIS IS THE 'CONTEXT'

    def __init__(self):
        self.state = st.StateSum()
        self.sum_val = 0

    def process_input(self, v):
        self.state.process_input(self, v)

    def set_state(self, new_state):
        self.state = new_state

    def sum(self, v):
        self.sum_val += v


if __name__ == '__main__':
    n = 20
    values = list(range(n))

    # ------------------------------
    # make correct output
    results_ok = 0
    list_results_ok = []
    flag = True
    for i in range(n):
        if flag:
            results_ok += values[i]
        flag = not flag
        list_results_ok.append(results_ok)
    # list_results_ok == [0, 0, 2, 2,  6, 6,  12, 12,  20, 20  30, 30, 42, 42, 56, 56 72,72 90, 90] if n==20
    # ------------------------------

    s = SumSkip()
    list_results = []
    for el in values:
        s.process_input(el)

        list_results.append(s.sum_val)

    print(list_results == list_results_ok)
