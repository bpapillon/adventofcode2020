import re


def valid_ecl(value):
    valid_ecls = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    return value in valid_ecls


def valid_hcl(value):
    pattern = r'#[0-9a-f]+'
    return re.match(pattern, value)


def valid_hgt(value):
    pattern = r'^([0-9]+)(cm|in)$'
    match = re.match(pattern, value)
    if not match:
        return False
    unit = match.group(2)
    number = int(match.group(1))
    if unit == 'cm':
        return valid_range(number, 150, 193)
    if unit == 'in':
        return valid_range(number, 59, 76)
    return False


def valid_range(value, valid_min, valid_max):
    return int(value) >= valid_min and int(value) <= valid_max


def parse_passport(lines):
    return dict(map(lambda x: x.split(':'), re.split(r'\s+', lines)))


def passport_is_valid(passport):
    required_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    if len(required_keys - set(passport.keys())) > 0:
        return False
    if not valid_range(passport['byr'], 1920, 2002):
        return False
    if not valid_range(passport['iyr'], 2010, 2020):
        return False
    if not valid_range(passport['eyr'], 2020, 2030):
        return False
    if not valid_hgt(passport['hgt']):
        return False
    if not valid_hcl(passport['hcl']):
        return False
    if not valid_ecl(passport['ecl']):
        return False
    if not len(passport['pid']) == 9:
        return False
    return True


def passports_from_file(filename):
    passport_entries = open(filename, 'rb').read().strip().split("\n\n")
    return map(parse_passport, passport_entries)


def valid_passports_from_file(filename):
    passports = passports_from_file(filename)
    return [passport for passport in passports if passport_is_valid(passport)]


filename = 'input.txt'
print len(valid_passports_from_file(filename))
