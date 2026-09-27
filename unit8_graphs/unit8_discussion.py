"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    pass
    
    # Handle edge case: start node not in graph
    if start not in graph:
        return []
    
    # A queue is used because BFS explores nodes level by level (FIFO).
    # Unlike a stack (used in DFS), a queue ensures that all nodes at
    # the current level are visited before moving to the next level.
    queue = deque([start])
    
    # Track visited nodes to prevent infinite loops and duplicate visits.
    # This is essential for graphs that may contain cycles.
    visited = set([start])
    
    # Store the order in which nodes are visited for output
    traversal_order = []
    
    # Process nodes level by level
    while queue:
        # Remove the first node from the queue (FIFO order)
        current = queue.popleft()
        traversal_order.append(current)
        
        # Neighbors are added to the queue so they can be visited next.
        # This ensures we explore all nodes at the current level before
        # moving deeper into the graph.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        
        # HOW BFS DIFFERS FROM DEPTH-FIRST TRAVERSAL (DFS):
        # - BFS uses a QUEUE (FIFO) while DFS uses a STACK (LIFO)
        # - BFS explores all neighbors at the current level before going deeper
        # - DFS explores as far as possible along each branch before backtracking
        # - BFS finds shortest paths in unweighted graphs
        # - DFS is better for exploring all possible paths or detecting cycles
    
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")
    
    # Creating a graph using adjacency list representation
    # This graph represents a social network where:
    # - Nodes represent people
    # - Edges represent friendships (bidirectional connections)
    
    graph = {
        'Alice': ['Bob', 'Charlie', 'David'],      # Alice is friends with Bob, Charlie, and David
        'Bob': ['Alice', 'Eve'],                   # Bob is friends with Alice and Eve
        'Charlie': ['Alice', 'Frank'],             # Charlie is friends with Alice and Frank
        'David': ['Alice', 'Eve'],                 # David is friends with Alice and Eve
        'Eve': ['Bob', 'David', 'Frank'],          # Eve is friends with Bob, David, and Frank
        'Frank': ['Charlie', 'Eve']                # Frank is friends with Charlie and Eve
    }
    
    # Display the graph structure
    print("\nSocial Network Graph (Adjacency List):")
    for person, friends in graph.items():
        print(f"  {person}: {friends}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")
    
    # Select starting node
    start_node = 'Alice'
    
    # Perform BFS traversal
    print(f"\nStarting BFS from '{start_node}':")
    traversal = bfs(graph, start_node)
    print(f"Traversal Order: {traversal}")
    
    # Explanation of level-by-level traversal:
    print("\nHow BFS visits nodes level by level:")
    print("  Level 0: Alice (starting node)")
    print("  Level 1: Bob, Charlie, David (direct neighbors of Alice)")
    print("  Level 2: Eve, Frank (neighbors of Level 1 nodes, not yet visited)")
    print("\nBFS guarantees that all nodes at level N are visited before any node at level N+1.")
    
    # Add a new node and edge to demonstrate updated traversal
    print("\n--- Adding New Node 'Grace' ---")
    graph['Grace'] = ['Frank']           # Grace is friends with Frank
    graph['Frank'].append('Grace')       # Add Grace to Frank's friend list
    
    print("\nUpdated Graph Structure:")
    for person, friends in graph.items():
        print(f"  {person}: {friends}")
    
    # Perform BFS again with the updated graph
    print(f"\nBFS Traversal after adding Grace (starting from '{start_node}'):")
    updated_traversal = bfs(graph, start_node)
    print(f"Traversal Order: {updated_traversal}")
    print("\nNotice: Grace appears at the end because she's connected through Frank,")
    print("who is at Level 2. Grace is therefore at Level 3.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    
    # EDGE CASE 1: Starting from a different node
    print("\n--- Edge Case 1: Different Starting Node ---")
    different_start = 'Frank'
    print(f"Starting BFS from '{different_start}':")
    traversal_frank = bfs(graph, different_start)
    print(f"Traversal Order: {traversal_frank}")
    print("Explanation: The traversal order changes based on the starting node.")
    print("From Frank, we visit his neighbors first (Charlie, Eve, Grace),")
    print("then their unvisited neighbors, and so on.")
    
    # EDGE CASE 2: Disconnected graph
    print("\n--- Edge Case 2: Disconnected Graph ---")
    disconnected_graph = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['A'],
        'X': ['Y'],        # X and Y form a separate component
        'Y': ['X'],
        'Z': []            # Z is completely isolated
    }
    print("Graph structure:")
    for node, neighbors in disconnected_graph.items():
        print(f"  {node}: {neighbors}")
    
    print("\nBFS from 'A':")
    traversal_a = bfs(disconnected_graph, 'A')
    print(f"Traversal Order: {traversal_a}")
    print("Explanation: BFS only visits nodes reachable from the start node.")
    print("Nodes X, Y, and Z are in different connected components, so they aren't visited.")
    
    # EDGE CASE 3: Missing start node
    print("\n--- Edge Case 3: Missing Start Node ---")
    missing_node = 'NonExistent'
    print(f"Attempting BFS from '{missing_node}' (not in graph):")
    traversal_missing = bfs(graph, missing_node)
    print(f"Traversal Order: {traversal_missing}")
    print("Explanation: The function safely returns an empty list when the")
    print("start node doesn't exist in the graph.")
    
    # EDGE CASE 4: Single node graph
    print("\n--- Edge Case 4: Single Node Graph ---")
    single_node_graph = {'OnlyNode': []}
    print("Graph structure:")
    for node, neighbors in single_node_graph.items():
        print(f"  {node}: {neighbors}")
    
    print("\nBFS from 'OnlyNode':")
    traversal_single = bfs(single_node_graph, 'OnlyNode')
    print(f"Traversal Order: {traversal_single}")
    print("Explanation: With only one node and no edges, BFS simply")
    print("returns that single node.")
    
    # EDGE CASE 5: Empty graph
    print("\n--- Edge Case 5: Empty Graph ---")
    empty_graph = {}
    print("Graph structure: {} (empty)")
    print("\nBFS from 'AnyNode':")
    traversal_empty = bfs(empty_graph, 'AnyNode')
    print(f"Traversal Order: {traversal_empty}")
    print("Explanation: With an empty graph, no nodes exist to traverse,")
    print("so an empty list is returned.")



if __name__ == "__main__":
    main()
