# DFS-BFS
## implemented methods
- depth first search dfs()
  - tells if there is a cycle in the graph
- breadth first search bfs()
  - tells how far away each "node" is from the root
### how to run
```
(venv) C:\school\cs320\graphsPA2>dfbf.py [input graph you'd like to use] [root node you'd like to use] [debug mode (optional)

```

- Example output
```
(venv) C:\school\cs320\graphsPA2>dfbf.py in1.txt a
root key: a
BFS
[('a', 0), ('b', 1), ('c', 1), ('d', 1), ('e', 2), ('f', 2), ('g', 3)]
DFS
cycle in a
cycle in f
```
