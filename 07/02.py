import functools
import re


def eventually_contained(rules, bag_name):
    contents = reduce(lambda accum, (bag_name, quantity): accum + [bag_name] * quantity, rules[bag_name], [])
    f = functools.partial(eventually_contained, rules)
    return contents + reduce(lambda accum, content_item: accum + f(content_item), contents, [])


def parse_contents(item):
    match = re.match(r'^([0-9]+) ([a-z ]+) bag|bags$', item)
    return (match.group(2), int(match.group(1)))


def parse_line(line):
    match = re.match(r'^([a-z ]+) bags contain ([a-z0-9, ]+|no other bags)\.$', line)
    bag_name = match.group(1)
    if match.group(2) == 'no other bags':
        contents = []
    else:
        contents = map(parse_contents, match.group(2).split(', '))
    return (bag_name, contents)


filename = 'input.txt'
rules = dict(map(parse_line, open(filename, 'rb').read().strip().split('\n')))
print len(eventually_contained(rules, 'shiny gold'))
