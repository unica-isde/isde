# transition_table = {
#     (state_0, input_0): {action: action, next_state: next_state},
#     (state_0, input_1): {action: action, next_state: next_state},
#     ...
#     (state_n, input_k): {action: action, next_state: next_state},
# }
#
# transition_table = {
#     state_0: {
#         input_0: {action: action, next_state: next_state},
#         input_1: {action: action, next_state: next_state},
#         default_input: {action: action, next_state: next_state}
#     },
#     state_1: {
#         input_0: {action: action, next_state: next_state},
#         input_1: {action: action, next_state: next_state},
#         default_input: {action: action, next_state: next_state}
#     }
# }


class State_version_a:
    def f_null(self, v):
        pass

    def f_sum(self, v):
        self.sum_val += v

    def __init__(self, val_to_skip, start_state=0):
        self.sum_val = 0
        self.id_state = start_state
        self.transition_table = {
            0: {  # state 0
                val_to_skip: {'action': self.f_null, 'next_state': 1},
                'default_input': {'action': self.f_sum, 'next_state': 0},
            },
            1: {  # state 1
                val_to_skip: {'action': self.f_null, 'next_state': 1},
                'default_input': {'action': self.f_null, 'next_state': 0}
            }
        }

    def process_input(self, v_input):
        entry_state = self.transition_table[self.id_state]

        # how to manage a 'default' input?
        # action = entry_state[v_input]['action']
        # next_state = entry_state[v_input]['next_state']

        entry_input = entry_state.get(v_input, entry_state['default_input'])
        action = entry_input['action']
        next_state = entry_input['next_state']

        action(v_input)
        self.id_state = next_state


"""
We can improve the design.
The method process_input is responsible for both 
the state transition and the action. 

We can apply the single responsibility principle by writing two different methods,
state_transition() and action()

"""


class State_version_b:

    def f_null(self, v):
        pass

    def f_sum(self, v):
        self.sum_val += v

    def __init__(self, val_to_skip, start_state=0):
        self.sum_val = 0
        self.id_state = start_state
        self.transition_table = {
            0: {  # state 0
                val_to_skip: {'action': self.f_null, 'next_state': 1},
                'default_input': {'action': self.f_sum, 'next_state': 0},
            },
            1: {  # state 1
                val_to_skip: {'action': self.f_null, 'next_state': 1},
                'default_input': {'action': self.f_null, 'next_state': 0}
            }
        }

    def process_input(self, v_input):
        entry_state_input = self._entry_state_input(v_input)
        self.action(entry_state_input, v_input)
        self.state_transition(entry_state_input)

        # ATTENTION - in this code, the correct entry in the state transition table
        # is identified by _entry_state_input (),
        # and therefore the order in which methods .action() and .state_transition() are called does not matter.
        #
        # If not, you should be careful about the order of .action() and .state_transition() calls

    def _entry_state_input(self, v_input):
        entry_state = self.transition_table[self.id_state]
        entry_state_input = entry_state.get(v_input, entry_state['default_input'])
        return entry_state_input

    def state_transition(self, entry_state_input):
        self.id_state = entry_state_input['next_state']

    def action(self, entry_state_input, v_input):
        entry_state_input['action'](v_input)

