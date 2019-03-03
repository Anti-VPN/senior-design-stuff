"""
A Python program to demonstrate the adjacency
list representation of the graph
"""


# weights arreay by value
weights = [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]

""" no longer in use 
# data object for nodes.
class Node:

  # construct a fully defined node
  def __init__(self, account_name, charcter_name, IP, UUID, IP_geolocation, is_banned, active_playtime ):
    self.account_name = account_name
    self.charcter_name = charcter_name
    self.IP = IP
    self.UUID = UUID # a unique id stored in a file on the clients computer
    self.IP_geolocation = IP_geolocation
    self.is_banned = is_banned
    self.active_playtime = active_playtime

  # print out a specific node
  def print_node(self):
      print(F"Account Name: {self.account_name}")
      print(F"Charcter Name: {self.charcter_name}")
      print(F"IP: {self.IP}")
      print(F"UUID: {self.UUID}")
      print(F"IP_geolocation: {self.IP_geolocation}")
      print(F"is_banned: {self.is_banned}")
      print(F"active_playtime: {self.active_playtime}\n")
"""


# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data, weight):
        self.vertex = data
        self.weight = weight
        self.next = None



# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest, weight):
        # Adding the node to the source node
        node = AdjNode(dest, weight)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src, weight)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                #print(" -> {}".format(temp.vertex), end="")
                print(F" -> Node Position = {temp.vertex} : weight = {temp.weight}", end="")
                temp = temp.next
            print(" \n")


# calculate the connected-ness of each node
def calculate_weights(node1, node2):
    w=0
    # calculate weight - does not include play time
    for i in range(0,6):
        if node1[i] == node2[i]:
            w+= weights[i]

    return w

# goes through and adds edges to adjancey list
def add_edges(NodeArray, graph):

    for i in range(len(NodeArray)):
        for j in range(i+1, len(NodeArray)):
            # get weight of each node with others
            w = calculate_weights(NodeArray[i], NodeArray[j])

            if w > (2/7):
                graph.add_edge(i,j,w)


    print()

if __name__ == "__main__":


    NodeArray = [["hello_gator", "Bob", "127.1.0.1", 56897, "US", True, 105],
        ["what_account", "Jason", "265.2.0.2", 63541, "Canada", False, 212],
        ["jello_pie", "Jason", "315.6.4.7", 88541, "Mexico", False, 105],
        ["jason_565", "Bob", "127.1.0.1", 56897, "US", False, 2],
        ["not_hello_gator", "Bob", "127.1.0.1", 56897, "US", False, 5],
        ["random", "Ryan", "666.3.2.1", 78912, "Mexico", False, 88],
        ["jello_man", "Simba", "265.2.0.2", 63541, "Canada", False, 12]]

    V = len(NodeArray)
    graph = Graph(V)
    add_edges(NodeArray, graph)


    graph.print_graph()