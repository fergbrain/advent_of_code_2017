import pydot
import re

#with open("input") as f:
#    puzInput = f.readlines()

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

graph = pydot.Dot(graph_type='digraph')

for row in puzInput:
    #print row
    if "->" in row:
        node,branch = row.split(" -> ")
        result = re.match("([a-z]+) \([\d]+\)", node)
        #print result.group(0)
        branch = [x.strip() for x in branch.split(',')]
        #print branch
        for x in branch:
            graph.add_edge(pydot.Edge(pydot.Node(result.group(1)), pydot.Node(x)))        
    #else:
    #    result = re.match("([a-z]+) \([\d]+\)", row)


print graph.get_edge_list()

graph.write_png('example2_graph.png')
