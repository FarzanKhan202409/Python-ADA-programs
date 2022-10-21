# WAP to represent Graph using Adjaceny Matrix:

class Graph(object):	
	def _init_(self, size):
		self.adjMatrix = []
		for i in range(size):
			self.adjMatrix.append([0 for i in range(size)])
		self.size = size
	def add_edge(self, v1, v2):
		if v1 == v2:
			print("Same vertex %d and %d" % (v1, v2))
		self.adjMatrix[v1][v2] = 1
		self.adjMatrix[v2][v1] = 1
	def _len_(self):
		return self.size
	def print_matrix(self):
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
	g.print_matrix()
	
	
if _name_ == '_main_':
	main()
