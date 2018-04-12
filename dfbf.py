import sys

def read(fnm,db):
  """
  read file fnm into dictionary
  each line has a nodeName followed by its adjacent nodeNames
  """
  file = open(fnm)
  graph = {} #dictionary
  for line in file:
    l = line.strip().split(" ")
    if db: print("l:",l,"len(l):",len(l))
    # remove empty lines
    if l==['']:continue
    # dict: key: nodeName  value: (color, adjList of names)
    graph[l[0]]= ('white',l[1:]) 
  return graph

def dump(graph):
  print("dumping graph: nodeName (color, [adj list]) ")
  for node in graph:
    print(node, graph[node])

def bfs(graph,list):
  queue = []
  queue.append(root)
  graph[root] = ("black", graph[root][1], 0)

  if(len(graph[root][1]) == 0):
    return list

  while queue:
    node = queue.pop(0)
    for i in graph[node][1]:
      if graph[i][0] == "white":
        graph[i] = ('grey', graph[i][1], graph[node][2] + 1)
        list.append((i, graph[i][2]))
        queue.append(i)
    graph[node] = ("black", graph[node][1])
  return list

def white(graph) :
  """
   paint all graph nodes white
  """
  for node in graph :
    gr[node] = ('white',gr[node][1])


def dfs(r):
   gr[r] = ("grey", gr[r][1])
   for v in gr[r][1]:
     if gr[v][0] == "white":
       dfs(v)
     if gr[v][0] == "grey":
       print("cycle in {}".format(v))
   gr[r] = ("black", gr[r][1])

if __name__ == "__main__":
  # db: debug flag
  db = len(sys.argv)>3
  gr = read(sys.argv[1],db)
  root = sys.argv[2]
  if db: dump(gr)
  print("root key:", root)
  # don't need grey for bfs
  gr[root] = ('black',gr[root][1])
  q = bfs(gr,[(root,0)])
  print("BFS")
  print(q)
  if db: dump(gr)
  white(gr)
  if db: dump(gr)
  print("DFS");
  dfs(root)
  if db: dump(gr)
