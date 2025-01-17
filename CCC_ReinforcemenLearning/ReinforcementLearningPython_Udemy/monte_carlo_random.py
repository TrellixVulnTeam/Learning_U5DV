import numpy as np
import matplotlib.pyplot as plt
from grid_world import standard_grid, negative_grid
from iterative_policy_evaluation import print_values, print_policy

# grid = standard_grid()
# start_states = list(grid.actions)
# start_idx = np.random.choice(len(start_states))
# print(grid.current_state())
# grid.set_state(start_states[start_idx])
# print(grid.current_state())
# print(grid.game_over())

SMALL_ENOUGH = 1e-3
GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = ('U', 'D' ,'R', 'L')

def random_action(a):
    p = np.random.random()
    if p < 0.5:
        return a
    else:
        tmp = list(ALL_POSSIBLE_ACTIONS)
        tmp.remove(a)
        return np.random.choice(tmp)
    
def play_game(grid, policy):
    # Random starts to make sure all possible states are explored randomnly
    start_states = list(grid.actions)
    start_idx = np.random.choice(len(start_states))
    grid.set_state(start_states[start_idx])

    s = grid.current_state()
    states_and_rewards = [(s, 0)]
    while not grid.game_over():
        a = policy[s]
        a = random_action(a)
        r = grid.move(a)
        s = grid.current_state()
        states_and_rewards.append((s,r))
    
    # Calculate the rewards by working backwards from the terminal state
    G = 0
    states_and_returns = []
    first = True
    for s,r in reversed(states_and_rewards):
        if first:
            first = False
        else:
            states_and_returns.append((s, G))
        G = r + GAMMA*G
    states_and_returns.reverse()
    return states_and_returns

if __name__ == "__main__":
    grid = standard_grid()

    print('rewards:')
    print_values(grid.rewards, grid)

    policy = {
        (2, 0): 'U',
        (1, 0): 'U',
        (0, 0): 'R',
        (0, 1): 'R',
        (0, 2): 'R',
        (1, 2): 'U',
        (2, 1): 'L',
        (2, 2): 'U',
        (2, 3): 'L',
    }

    # Initialize V(s) and returns
    V = {}
    returns = {}
    states = grid.all_states()
    for s in states:
        if s in grid.actions:
            returns[s] = []
        else:
            V[s] = 0

    # repeat until convergence
    for t in range(5000):

        # generate an episode using pi
        states_and_returns = play_game(grid, policy)
        seen_states = set()
        for s,G in states_and_returns:
            if s not in seen_states:
                returns[s].append(G)
                V[s] = np.mean(returns[s])
                seen_states.add(s)
    print('values:')
    print_values(V, grid)
    print('policy:')
    print_policy(policy, grid)




