#!/usr/bin/python

import hashlib, string

s = string.ascii_letters + string.digits + ' ,./?><\'";:\|]}[{=+-_)(*&^%$#@!~`' 
d_sha = {hashlib.sha256(c).hexdigest(): c for c in s}
d_md5 = {hashlib.md5(c).hexdigest(): c for c in s}

f = open('submit_the_flag_that_is_here.txt', 'r')
inp = f.read()[:-1]
f.close()

result = []
for word in inp.split(' '):
    if len(word) == 32:
        result.append(d_md5[word])
    elif len(word) == 64:
        result.append(d_sha[word])

string_result = ''.join(result)
assert len(string_result) == len(inp)

f = open('maybe_flag.txt', 'w')
f.write(string_result)
f.close()

# use less and comb through until you find it
