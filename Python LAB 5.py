#Design a "Graph" class that represent a Graph where edges are represented as {Node1: (Node2, Weight1), Node2: (Node3, Weight2)}

class AdjNode:
	def _init_(self, data):
		self.vertex = data
		self.next = None
class Graph:
	def _init_(self, vertices):
		self.V = vertices
		self.graph = [None] * self.V
	def add_edge(self, src, dest):
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node
		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node
	def print_graph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			print(" \n")

def main():
	n=int(input("Enter The Number of Nodes"))	
	g = Graph(n)
	for i in range (n):
		x=int(input("source "))
		y=int(input("destination"))
		g.add_edge(x, y)
	g.print_graph()
	
	
if __name__ == '_main_':
	main()
