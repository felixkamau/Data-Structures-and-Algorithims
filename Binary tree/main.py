# Function to add an edge between vertices x and y

# Function to print the parent of each node

def printParents(node, adj, parent):

    # current node is root thus has no parent
    if (parent == 0):
        print(node, "--->", parent)
    else:
        print(node, "--->", parent)

    # Using DFS Depth first search Depth-first search (DFS) is
    # a method for exploring a tree or graph. In a DFS, you go
    # as deep as possible down one path before backing up and
    # trying a different one. Depth-first search is like walking
    # through a corn maze. You explore
    # one path, hit a dead end, and go back and try a different one
    for cur in adj[node]:
        if (cur != parent):
            printParents(cur, adj, node)
            # (cur) --> A cursor is an object which helps to execute the
            # query and fetch the records from the database.

# function to print the children of each node


def printChildren(Root, adj):

    # BFS ---> (Breadth First Search) − It is a tree traversal
    # algorithm that is also known as Level Order Tree Traversal.
    # In this traversal we will traverse the tree row by row i.e.
    # 1st row, then 2nd row, and so on. DFS (Depth First Search ) −
    # It is a tree traversal algorithm that traverses the structure
    # to its deepest node

    # Queue for the BFS
    q = []
    # pushing the Root

    # visit array to keep track of nodes that have been
    # visited

    vis = [0]*len(adj)

    # BFS ---> Breadth First Search
    while (len(q) > 0):
        node = q[0]
        q.pop(0)  # remove [0]
        vis[node] = 1
        print(node, "--->", end=" ")


# function to print the leaf nodes

def printLeafNodes(Root, adj):
    for i in range(0, len(adj)):
        if (len(adj[i]) == 1 and i != Root):
            print(i, end=" ")
    print("\n")

# Function to print the degrees of each node


def printDegrees(Root, adj):

    for i in range(1, len(adj)):
        print(i, ": ", end=" ")

        # Root has no parent, thus, its degree is equal to
        # the edges it is connected to
        if (i == Root):
            print(len(adj[i]))
        else:
            print(len(adj[i])-1)

# Driver code


# Number of nodes
N = 7
Root = 1

# Adjacency list to store the tree
adj = []
for i in range(0, N+1):
    adj.append([])

# Creating the tree
adj[1].append(2)
adj[2].append(1)

adj[1].append(3)
adj[3].append(1)

adj[1].append(4)
adj[4].append(1)

adj[2].append(5)
adj[5].append(2)

adj[2].append(6)
adj[6].append(2)

adj[4].append(7)
adj[7].append(4)

# Printing the parents of each node
print("The parents of each node are:")
printParents(Root, adj, 0)

# Printing the children of each node
print("The children of each node are:")
printChildren(Root, adj)

# Printing the leaf nodes in the tree
print("The leaf nodes of the tree are:")
printLeafNodes(Root, adj)

# Printing the degrees of each node
print("The degrees of each node are:")
printDegrees(Root, adj)
