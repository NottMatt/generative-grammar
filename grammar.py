#!/bin/python3
# mtiemersma19@georgefox.edu
# generative grammar writer

from operator import ge
import sys
import random


# parse arguments
num_args = len(sys.argv)
g_file = sys.argv[1]

f = open(g_file, "r")

# load in production rules
rules_txt = f.read().split("{")[1:]

rules = {}

for r in rules_txt:
    r_name = r.split("\n")[1]
    r_rhs = r.split("}")[0].split("\n")[2:-1]
    for i in range(0, len(r_rhs)):
        r_rhs[i] = r_rhs[i].split(";")[0].strip()
    rules[r_name] = r_rhs

# stack based generation
genstack = []

# start with start
genstack.append("<start>")

keep_going = True

while(keep_going):
    curr = genstack.pop()

    # if terminal, print
    if "<" in curr:
        rhs = rules[curr][random.randint(0, len(rules[curr]) - 1)].split(" ")
        for i in range(len(rhs) -1, -1, -1):
            genstack.append(rhs[i])
    else:
        print(curr, end=" ")
    # if non-terminal, push random option to stack
    # if stack empty, stop

    if len(genstack) == 0:
        keep_going = False

print("")
