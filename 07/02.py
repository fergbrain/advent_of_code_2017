import networkx as nx
import re
import matplotlib.pyplot as plt


with open("input") as f:
    puzInput = f.readlines()
'''
puzInput = [    "pbga (66)",
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
    
def odd_item_out(this_dict):
    if not isinstance(this_dict, dict):
        print "Dict not provided"
        exit()
    if len(this_dict) < 2:
        print "Dict not long enough"
        exit()
    a_key = this_dict.iterkeys().next()
    a = this_dict[a_key]
    a_count = 0
    b_count = 0
    for key, value in this_dict.iteritems():
        if value != a:
            b = value
            b_key = key
    try:
        b
    except NameError:
        return -1, -1
    for key, value in this_dict.iteritems():
        if value == a:
            a_count += 1
        elif value == b:
            b_count += 1
        else:
            print "More than two types in this dict"
            print "Item A: %s" % a
            print "Item B: %s" % b
            print "This item: %s" % value
            exit()
    if a_count > b_count:
        return b_key, int(b) - int(a)
    else:
        return a_key, int(a) - int(b)
    
    
G = nx.DiGraph()

for row in puzInput:
    #print row
    if "->" in row:
        node,branch = row.split(" -> ")
        result = re.match("([a-z]+) \(([\d]+)\)", node)
        branch = [x.strip() for x in branch.split(',')]
        #print branch
        G.add_node(result.group(1), weight=result.group(2))
        for x in branch:
            G.add_edge(result.group(1), x)
        
    else:
        result = re.match("([a-z]+) \(([\d]+)\)", row)
        G.add_node(result.group(1), weight=result.group(2))


top = list(nx.topological_sort(G))[0]
print "Top Node %s: %s" % (top, G.node[top]['weight'])

def check_balance(top_node):
    sub_prog_result = {}

    for sub_prog_node in list(G.neighbors(top_node)):
        sum_node_weight = int(G.node[sub_prog_node]["weight"])
        for node in nx.descendants(G, sub_prog_node):
            sum_node_weight += int(G.node[node]["weight"])
        #print "%s (%s): %s" % (sub_prog_node, G.node[sub_prog_node]["weight"], sum_node_weight)
        sub_prog_result[sub_prog_node] = sum_node_weight

    return odd_item_out(sub_prog_result)

next_node, diff = check_balance(top)
last_node = next_node[:]
while True:
    if next_node == -1:
        node, diff = check_balance(last_last_node)
        print node
        print int(G.node[node]["weight"]) - diff
        break
    else:
        last_last_node = last_node[:]
        last_node = next_node[:]
        next_node, diff = check_balance(next_node)