import sys
import collections

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        test = [[int(team) for team in country.strip().split(' ')] for country in test.split('|')]
        team_to_fan_countries = collections.defaultdict(list)
        for country in range(len(test)):
            liked_teams = test[country]
            for team in liked_teams:
                team_to_fan_countries[team].append(country+1)
        result = []
        for team in sorted(team_to_fan_countries.keys()):
            result.append(str(team) + ':' + ','.join([str(c) for c in team_to_fan_countries[team]]))
        print('; '.join(result) + ';')
    test_cases.close()

if __name__ == '__main__':
    main()
