#AoC2015 day4 part1&2

import hashlib

key = 'ckczppom'

coin = 0
while not hashlib.md5(key+str(coin)).hexdigest().startswith('000000'):
    coin += 1

print hashlib.md5(key+str(coin)).hexdigest()
print coin
