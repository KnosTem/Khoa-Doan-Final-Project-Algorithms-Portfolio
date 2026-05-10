"""
Lab 6: Graph Implementation
Adjacency list representation for city road network.
"""
from typing import Dict, List, Set
from collections import defaultdict


class Graph:
    """
    Undirected graph using adjacency list.
    
    Adjacency list: Each node stores list of neighbors
    - Space efficient for sparse graphs
    - O(1) to add edge
    - O(degree) to check if edge exists
    """
    
    def __init__(self):
        # defaultdict creates empty list for new keys
        self.adjacency_list: Dict[str, List[str]] = defaultdict(list)
        self.vertices: Set[str] = set()
    
    def add_vertex(self, vertex: str) -> None:
        """Add a vertex to the graph."""
        self.vertices.add(vertex)
    
    def add_edge(self, v1: str, v2: str) -> None:
        """
        Add undirected edge between v1 and v2.
        For directed graph, only add v1 -> v2.
        """
        self.vertices.add(v1)
        self.vertices.add(v2)
        
        # Undirected: add both directions
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append(v2)
        if v1 not in self.adjacency_list[v2]:
            self.adjacency_list[v2].append(v1)
    
    def get_neighbors(self, vertex: str) -> List[str]:
        """Get all neighbors of a vertex."""
        return self.adjacency_list[vertex]
    
    def has_edge(self, v1: str, v2: str) -> bool:
        """Check if edge exists between v1 and v2."""
        return v2 in self.adjacency_list[v1]
    
    def display(self) -> None:
        """Display the graph structure."""
        print("\nGraph Adjacency List:")
        print("-" * 40)
        for vertex in sorted(self.vertices):
            neighbors = self.adjacency_list[vertex]
            print(f"{vertex}: {neighbors}")
    
    def __len__(self) -> int:
        return len(self.vertices)


def create_texas_road_network() -> Graph:
    """
    Create a simplified Texas highway network.
    Edges represent direct highway connections.
    """
    g = Graph()
    
    # Major highway connections (simplified)
    roads = [
        # I-45 corridor
        ("Houston", "Dallas"),
        
        # I-35 corridor  
        ("Dallas", "Austin"),
        ("Austin", "San Antonio"),
        ("San Antonio", "Laredo"),
        
        # I-10 corridor
        ("Houston", "San Antonio"),
        ("San Antonio", "El Paso"),
        
        # I-20 corridor
        ("Dallas", "Fort Worth"),
        ("Fort Worth", "Lubbock"),
        ("Lubbock", "El Paso"),
        
        # Other connections
        ("Dallas", "Arlington"),
        ("Fort Worth", "Arlington"),
        ("Houston", "Corpus Christi"),
        ("Corpus Christi", "San Antonio"),
        ("Austin", "Killeen"),
        ("Dallas", "Plano"),
        ("Dallas", "Irving"),
        ("Dallas", "Garland"),
        ("Plano", "Frisco"),
        ("Plano", "McKinney"),
        ("Corpus Christi", "Brownsville"),
        ("Brownsville", "McAllen"),
        ("McAllen", "Laredo"),
    ]
    
    for city1, city2 in roads:
        g.add_edge(city1, city2)
    
    return g
