#python implementation of graph


class Graph:
	def __init__ (self, gdict = None):
		if gdict is None :
			gdict = {}
		else:
			self.gdict = gdict

	def addVertex(self, vertex):
		if vertex in self.gdict.keys():
			pass
		else:
			self.gdict[vertex]= []

	def addEdge(self, vertex, edge):
		self.gdict[vertex].append(edge)

	def removeEdge(self, vertex1, vertex2):
		if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
			try:
				self.gdict[vertex1].remove(vertex2)
				self.gdict[vertex2].remove(vertex1)
			except:
				print("This is not a edge")

	def removeVertex(self, vertex):
		if vertex in self.gdict.keys():
			for otherVertex in self.gdict[vertex]:
				self.gdict[otherVertex].remove(vertex)
			del self.gdict[vertex]

	def bfs(self, vertex):
		visited=[vertex]
		queue=[vertex]
		while len(queue)>0:
			deVertex=queue.pop(0)
			print(deVertex)
			for adjacentVertex in self.gdict[deVertex]:
				if adjacentVertex not in visited:
					visited.append(adjacentVertex)
					queue.append(adjacentVertex)



	def dfs(self, vertex):
		visited=[vertex]
		stack= [vertex]
		while len(stack)>0:
			popVertex= stack.pop()
			print(popVertex)
			for adjacentVertex in self.gdict[popVertex]:
				if adjacentVertex not in visited:
					visited.append(adjacentVertex)
					stack.append(adjacentVertex)


customDict= {"a" : ["b", "c"],
			 "b" : ["a", "d", "e"],
			 "c" : ["a", "e"],
			 "d" : ["b", "e", "f"],
			 "e" : ["d", "f"],
			 "f" : ["d", "e"],
			 }

graph= Graph(customDict)
graph.addEdge("e", "c")
print(graph.gdict)
print('\n')
graph.addVertex("x")
print(graph.gdict)
print('\n')
graph.removeEdge('a', 'd')
print(graph.gdict)
print('\n Removing Vertex ')
graph.removeVertex('d')
print(graph.gdict)


graph.bfs('a')
print('\n')
graph.dfs('a')

