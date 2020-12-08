import functools
import re


def eventually_containing(rules, bag_name):
    containers = set([bag for bag, contents in rules if bag_name in contents])
    f = functools.partial(eventually_containing, rules)
    return containers | reduce(lambda accum, container: accum | f(container), containers, set())


def parse_line(line):
    match = re.match(r'^([a-z ]+) bags contain ([a-z0-9, ]+|no other bags)\.$', line)
    return (match.group(1), match.group(2))


filename = 'input.txt'
rules = map(parse_line, open(filename, 'rb').read().strip().split('\n'))
print len(eventually_containing(rules, 'shiny gold'))
