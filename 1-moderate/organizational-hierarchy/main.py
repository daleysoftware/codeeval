import sys
import collections
import itertools


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        test = [x.strip() for x in test.split("|")]
        # Construct the hierarchy.
        hierarchy = collections.defaultdict(list)
        for pair in test:
            hierarchy[pair[0]].append(pair[1])
        # Determine the top-level managers.
        top_level_managers = []
        subordinates = list(itertools.chain(*hierarchy.values()))
        for manager in hierarchy.keys():
            if manager not in subordinates:
                top_level_managers.append(manager)
        # We now the hierarchy and the top level managers. Print the result.
        def employee_to_string(employee):
            result_string = employee
            if employee in hierarchy:
                result_string += " ["
                subordinates_string_list = []
                for subordinate in sorted(hierarchy[employee]):
                    subordinates_string_list.append(employee_to_string(subordinate))
                result_string += ", ".join(subordinates_string_list) + "]"
            return result_string
        result_list = []
        for manager in sorted(top_level_managers):
            result_list.append(employee_to_string(manager))
        print(", ".join(result_list))
    test_cases.close()


if __name__ == '__main__':
    main()
