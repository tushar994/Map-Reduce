#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = []
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    # try:
    #     count = int(count)
    # except ValueError:
    #     # count was not a number, so silently
    #     # ignore/discard this line
    #     continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        # print("appending ", count)
        current_count.append(count)
    else:
        # print(current_word, "is different from",word)
        if current_word:
            # write result to STDOUT
            print(current_word.capitalize(), ":", ",".join(current_count))
        current_count = [count]
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print(current_word.capitalize(), ":", ",".join(current_count))
