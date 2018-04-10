



class GraphNode:
    def __init__( self, number ):
        self.number = number

class Graph:
    def __init__( self, vertice_number ):
        self._vertice_number = vertice_number
        self._graph_list = []
        self._initializeGraph()

    def _initializeGraph( self ):
        for i in range( 0, self._vertice_number ):

