import networkx as nx
import re
import matplotlib.pyplot as plt


with open("input") as f:
    puzInput = f.readlines()

'''puzInput = [    "pbga (66)",
                "xhth (57)",
                "ebii (61)",
                "havc (66)",
                "ktlj (57)",
                "fwft (72) -> ktlj, cntj, xhth",
                "qoyq (66)",
                "padx (45) -> pbga, havc, qoyq",
                "tknk (41) -> ugml, padx, fwft",
                "jptl (61)",
                "ugml (68) -> gyxo, ebii, jptl",
                "gyxo (61)",
                "cntj (57)"]
'''
G = nx.DiGraph()

for row in puzInput:
    #print row
    if "->" in row:
        node,branch = row.split(" -> ")
        result = re.match("([a-z]+) \([\d]+\)", node)
        #print result.group(0)
        branch = [x.strip() for x in branch.split(',')]
        #print branch
        for x in branch:
            G.add_edge(result.group(1), x)
        
    #else:
    #    result = re.match("([a-z]+) \([\d]+\)", row)


print list(nx.topological_sort(G))[0]
