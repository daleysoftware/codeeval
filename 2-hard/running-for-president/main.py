import sys
import copy

class State:
    def __init__(self, name, votes, issues):
        self.name = name
        self.votes = votes
        # Issue to voting preference dictionary.
        self.issues = issues

def count_votes(strategy, states):
    total_votes = 0
    for state in states:
        votes = 0
        for issue in strategy:
            votes += state.issues[issue]
        if float(votes) / state.votes >= 0.51:
            total_votes += state.votes
    return total_votes

def is_winning_strategy(strategy, states):
    return count_votes(strategy, states) >= 270

def compute_strategy_cost(strategy, issue_name_to_cost):
    total_cost = 0
    for issue in strategy:
        total_cost += issue_name_to_cost[issue]
    return total_cost

def get_possibilities_of_length_n(n, prefix=None, result=None):
    if prefix is None: prefix = []
    if result is None: result = []
    if len(prefix) == n:
        result.append(copy.deepcopy(prefix))
        return
    get_possibilities_of_length_n(n, prefix + [False], result)
    get_possibilities_of_length_n(n, prefix + [True], result)
    return result

def possibility_to_strategy(possibility, issues):
    strategy = []
    for i in range(len(issues)):
        if possibility[i]: strategy.append(issues[i])
    return strategy

def compute_best_winning_strategy(issue_name_to_cost, states):
    possibilities = get_possibilities_of_length_n(len(issue_name_to_cost))
    issues = list(issue_name_to_cost.keys())

    best_cost = float('inf')
    best_strategy = []

    for possibility in possibilities:
        strategy = possibility_to_strategy(possibility, issues)
        if is_winning_strategy(strategy, states):
            cost = compute_strategy_cost(strategy, issue_name_to_cost)
            if cost < best_cost:
                best_cost = cost
                best_strategy = strategy

    return best_strategy

def parse(data):
    # Parse issues and cost.
    issue_name_to_cost = {}
    for issue_data in data[1].split('\n'):
        name = issue_data.split(':')[0].strip()
        cost = int(issue_data.split(':')[1].strip())
        issue_name_to_cost[name] = cost

    # Parse states and value.
    states = []
    for state_data in data[2:]:
        state_data = state_data.strip().split('\n')
        name = state_data[0]
        votes = int(state_data[1].split(':')[1].strip())
        state_issues = {}
        for issue in state_data[2:]:
            issue_name = issue.split(':')[0].strip()
            issue_value = int(issue.split(':')[1].strip())
            state_issues[issue_name] = issue_value
        states.append(State(name, votes, state_issues))

    return issue_name_to_cost, states

def main():
    with open(sys.argv[1], 'r') as fh:
        data = fh.read().strip().split('\n\n')
        issue_name_to_cost, states  = parse(data)
        result = compute_best_winning_strategy(issue_name_to_cost, states)
        print('\n'.join(sorted(result)))

if __name__ == '__main__':
    main()
