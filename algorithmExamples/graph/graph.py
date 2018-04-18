#!/usr/bin/python


from collections import deque

__all__ = ["Graph"]
__author__ = "umit aykurt"


class Queue:
    def __init__( self ):
        self._que = deque()
        
    def enqueue( self, element ):
        self._que.append(element)
        
    def dequeue( self ):
        return self._que.popleft() 
        
    def __str__( self ):
        return str( self._que )
       
       


class Edge():
    
    def __init__( self, dst, weight ):
        self.dst = dst
        self.weight = weight
        
    def __str__( self ):
        return " to %s cost is %s " %( str(dst), str(weight))
        
        
        
class Graph():
    
    def __init__( self, vertice_number ):
        self.graph = {}
        self.vertices = {}
        self.vertice_number = vertice_number
        
        for i in range( vertice_number ):
            self.graph[i] = []
            
        
        
        
    def addVertice( self, src, label ):
        self.vertices[src] = label
        
    
        
    def addEdge( self, src, dst, weight ):
        new_edge = Edge( dst, weight )
        adjacency_list = self.graph[src]
    
    #Check if edge already exists in the adjacency list
    #if it does then change weight of the edge    
        for edge in adjacency_list:
            if edge.dst == dst:
                edge.weight = weight
                return
                
            
        adjacency_list.append( new_edge )
        
        
        
    def printGraph( self ):
        for vertice, edges in self.graph.iteritems():
            for edge in edges:
                print "From %s to %s cost is %s" %( self.vertices[vertice], self.vertices[edge.dst], str(edge.weight))
                

    def getReachablewithBFS( self, start ):
        discovered = [ 0 ]
                        
                
                

if __name__ == "__main__":
    """ 
    graph = Graph(10)
    
    graph.addVertice( 0, "Ankara" )
    graph.addVertice( 1, "Istanbul" )
    graph.addVertice( 2, "Izmir" )
    graph.addVertice( 3, "Adana" )
    graph.addVertice( 4, "Antalya" )
    
    graph.addEdge( 0, 1, 600 )
    graph.addEdge( 0, 2, 800 )
    graph.addEdge( 1, 3, 1000 )
    
    
    
    graph.printGraph()
    
    """
    
            
            
        
                
                
            
        
        

        
        
    
        