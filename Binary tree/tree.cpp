//  c++ implement binary tree

#include <bits/stdc++.h>
using namespace std;

// function to add an edge btwn vertices x and y
void addEdge(int x, int y, vector<vector<int>> & adj)
{
    adj[x].push_back(y);
    adj[y].push_back(x);
}
// function to print the parent of each nodes
void printParents(int node, vector<vector<int>>& adj,
                  int parent)

{
    // current node is root thus has no parents
    if (parent == 0)
      cout << node << "---.Root" << endl;

    else
      cout << node << "--->" << parent << endl;

    // using DFS
    for (auto cur : adj[node])
      if (cur != parent)
          printParents(cur, adj, node);
}
// function to print the children of each nodes
void printChildren(int Root, vector<vector<int>>& adj)
{
    // Queue for the BFS
    queue<int> q;
    // push the Root
    q.push(Root);
    // visit array to keep track of nodes that have been 
    // visited

    int vis[adj.size()] = {0};
    // BFS
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        vis[node] = 1;
        cout << node << "--->";
        for (auto cur : adj[node])
            if (vis[cur] == 0) {
                cout<< cur << " ";
                q.push(cur);
            }
        cout << endl;
    }
}
// funtion to print the leaf nodes
void printLeafNodes(int Root, vector<vector<int>>& adj)
{
    // leaf nodes have only one edge and are not the root
    for (int i = 1; i < adj.size(); i++)
         cout << i << " ";

    cout << endl;
}
// function to print the degrees of each nodes
void printDegrees(int  Root, vector<vector<int>>& adj)
{
    for (int i = 1; i < adj.size(); i++){
        cout << i << ": ";
        // Root has no parent, thus, its degree is equal to
        // the edges it is connected to
        if (i == Root)
            cout << adj[i].size() << endl;
        else 
            cout << adj[i].size() - 1 << endl;
    }
}

// Driver Code
int main()
{
    // number of nodes
    int N = 7, Root = 1;
    // Adjacency list to store the tree
    vector<vector<int> > adj(N + 1, vector<int>());
    // creating the tree
    addEdge(1, 2, adj);
    addEdge(1, 3, adj);
    addEdge(1, 4, adj);
    addEdge(2, 5, adj);
    addEdge(2, 6, adj);
    addEdge(4, 7, adj);
    // Printing the parents of each node
    cout << "The parents of each node are:" << endl;
    printParents(Root, adj, 0);
 
    // Printing the children of each node
    cout << "The children of each node are:" << endl;
    printChildren(Root, adj);
 
    // Printing the leaf nodes in the tree
    cout << "The leaf nodes of the tree are:" << endl;
    printLeafNodes(Root, adj);
 
    // Printing the degrees of each node
    cout << "The degrees of each node are:" << endl;
    printDegrees(Root, adj);
 
    return 0;

}