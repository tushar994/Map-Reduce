#!/home/ds-m21-user0/HW4_team16/map_reduce_sample_code/venv/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = []
word = None
data = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    word = word.strip()
    count = count.strip()
    # convert count (currently a string) to int
    # try:
    #     count = int(count)
    # except ValueError:
    #     # count was not a number, so silently
    #     # ignore/discard this line
    #     continue  
    if(word not in data):
        data[word] = [count]
    else:
        data[word].append(count)
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    # if current_word == word:
    #     # print("appending ", count)
    #     current_count.append(count)
    # else:
    #     # print(current_word, "is different from",word)
    #     if current_word:
    #         # write result to STDOUT
    #         print(current_word, ":", ",".join(current_count))
    #     current_count = [count]
    #     current_word = word

# do not forget to output the last word if needed!
if "links" in data:
    print(data["links"][0],end=" ")
    del data["links"]
if "edges" in data:
    print(data["edges"][0])
    del data["edges"]
for i in data:
    for j in data[i]:
        print(i,j)