# Alphabet

For the [first crypto problem](https://github.com/Sporax/ctf-writeups/blob/master/2018/fireshell-ctf/submit_the_flag_that_is_here.7z) in fireshell CTF, we are given this input file containing a bunch of strings that look like hashes. Checking their lengths tells us they have length 64 and 32, which suggests they might be sha256 and md5 of some input.

Run a quick test to see whether all characters of the "alphabet" are directly hashed:
`echo -n e | sha256sum`
searching for the result in the large text file, `3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea` gives multiple matches.

The script solve.py contains the rest of the solution
