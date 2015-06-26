import sys
import collections

def suggested_groups_for_user(user, user_to_friends, group_to_members):
    result = []
    for group in group_to_members.keys():
        count = 0
        if user in group_to_members[group]:
            continue
        for friend in user_to_friends[user]:
            if friend in group_to_members[group]:
                count += 1
        if (count * 2) >= len(user_to_friends[user]):
            result.append(group)
    return result

def main():
    test_cases = open(sys.argv[1], 'r')
    user_to_friends = {}
    group_to_members = collections.defaultdict(list)
    for test in test_cases:
        test = test.strip().split(':')
        user = test[0]
        friends = test[1].split(',')
        groups = [] if len(test[2]) == 0 else test[2].split(',')
        user_to_friends[user] = friends
        for group in groups:
            group_to_members[group].append(user)
    test_cases.close()

    for user in sorted(user_to_friends.keys()):
        suggested_groups = suggested_groups_for_user(user, user_to_friends, group_to_members)
        if len(suggested_groups) >= 1:
            print("%s:%s" % (user, ','.join(sorted(suggested_groups))))

if __name__ == '__main__':
    main
