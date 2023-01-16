![Screenshot](./img/dfs-graph-traversal.jpg)

# Intuition

![Screenshot](./img/dfs-graph-traversal-01.jpg)
![Screenshot](./img/dfs-graph-traversal-02.jpg)
![Screenshot](./img/dfs-graph-traversal-03.jpg)
![Screenshot](./img/dfs-graph-traversal-04.jpg)

# DFS Implementation 1

![Screenshot](./img/dfs-implementation-01.jpg)

## Solution 1

```python
def dfs(G,v):
    visit(v)
    for w in G.neighbors(v):
        dfs(G,w)
```

Issue : infinite cycle because of node 0

## Solution 2

Mark nodes as visited

```python
marked = [False] * G.size()
def dfs(G,v):
    visit(v)
    marked[v]= True
    for w in G.neighbors(v):
        if not marked[w]:
            dfs(G,w)
```

pre-order implementation

# DFS Implementation 2

```python
marked = [False] * G.size()
def dfs_iter(G,v):
    stack = [v]
    while len(stack) > 0:
        v= stack.pop()
        if not marked[v]:
            visit(v)
            marked[v]= True
            for w in G.neighbors(v):
                stack.append(w)
```

Useful if we need to identify the DFS ordering by hand

![Screenshot](./img/dfs-implementation-02-stack.jpg)
![Screenshot](./img/dfs-implementation-02-stack-b.jpg)
![Screenshot](./img/dfs-implementation-02-stack-c.jpg)
![Screenshot](./img/dfs-implementation-02-stack-d.jpg)
![Screenshot](./img/dfs-implementation-02-stack-e.jpg)

## Performance perspective :

Both run in O(V + E) time

# Preorder vs PostOrder

![Screenshot](./img/preorder-postorder.jpg)

post-order implementation

```python
marked = [False] * G.size()
def dfs(G,v):
    # visit(v) pre-order implementation
    marked[v]= True
    for w in G.neighbors(v):
        if not marked[w]:
            dfs(G,w)
    visit(v) # post-order implementation
```

# DFS Application

- Cycle Detection
- Finding Connected Components
- Topological Sort

# DFS Game : Maze Generator

![Screenshot](./img/maze_units.jpg)
![Screenshot](./img/maze_cell.jpg)
