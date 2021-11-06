#!/usr/bin/env python3
"""mapper.py"""

import sys

class Node:
    def __init__(self,num):
        self.up = num
        self.number = 1

nodes = []

# input comes from STDIN (standard input)
flag = 0
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    if not flag:
        node_num = int(words[0])
        for i in range(0,node_num):
            nodes.append(Node(i))
        flag = 1
    else:
        node1 = int(words[0])
        node2 = int(words[1])
        node1 -=1
        node2 -=1
        while(node1 != nodes[node1].up):
            node1 = nodes[node1].up
        while(node2 != nodes[node2].up):
            node2 = nodes[node2].up
        if(nodes[node1].number < nodes[node2].number):
            nodes[node1].up = node2
            nodes[node2].number += nodes[node1].number
        else:
            nodes[node2].up = node1
            nodes[node1].number += nodes[node2].number

# now we have the nodes, we make the list
done = []
for i in range(1,node_num+1):
    done.append([])

for i in range(0,node_num):
    copy = i
    while(copy!=nodes[copy].up):
        copy = nodes[copy].up
    done[copy].append(i+1)

final = [x for x in done if x !=[]]

print("number\t",len(final))
k = 0
for i in final:
    for j in i:
        print(k,"\t",j)
    k+=1