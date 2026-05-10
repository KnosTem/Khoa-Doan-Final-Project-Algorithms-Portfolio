# =============================================================================
# Dijkstra's Shortest Path — Interactive CLI
#
# This program lets the user build an undirected weighted graph by entering
# nodes and edges, displays the graph as ASCII art, then finds and highlights
# the shortest path between two chosen nodes using Dijkstra's algorithm.
#
# Flow:
#   1. User enters node names
#   2. User enters edge weights for each pair of nodes
#   3. Graph is displayed
#   4. User picks a source and destination node
#   5. Dijkstra's algorithm finds the shortest path
#   6. Graph is re-displayed with the shortest path highlighted
# =============================================================================


def get_nodes():
    """
    Prompt the user to enter node names one at a time.

    Nodes are the vertices of the graph — e.g. cities, routers, or any
    named location. The user types each name and presses Enter, then types
    'done' to finish.

    Duplicate names are rejected so every node is unique.

    Returns:
        list[str]: Ordered list of node names as entered by the user.
    """
    print("=== Dijkstra's Shortest Path ===\n")
    print("Enter node names one per line.")
    print("Type 'done' when finished.\n")

    nodes = []

    while True:
        line = input("Node: ").strip()

        # Stop collecting nodes when the user types 'done'
        if line.lower() == "done":
            break

        # Ignore blank lines
        if not line:
            continue

        # Prevent duplicate node names
        if line in nodes:
            print(f"  '{line}' already added.")
            continue

        nodes.append(line)
        print(f"  Added: {line}")

    return nodes


def get_edges(nodes):
    """
    Prompt the user to enter a weight for each pair of nodes.

    Since edges are undirected (same weight in both directions), we only
    ask once per pair. If the user presses Enter without entering a weight,
    no edge is created between that pair — meaning they are not directly
    connected.

    Internally, each edge is stored in both directions (a→b and b→a) so
    that Dijkstra's algorithm can traverse the graph freely from any node.

    Args:
        nodes (list[str]): The list of node names collected in get_nodes().

    Returns:
        dict[str, dict[str, float]]: Adjacency dictionary where
            graph[a][b] = weight means there is an edge between a and b
            with the given weight (and graph[b][a] = weight also exists).
    """
    print("\nFor each pair of nodes, enter the edge weight if connected, or press Enter to skip.\n")

    # Initialise every node with an empty neighbour dictionary
    graph = {n: {} for n in nodes}

    # Iterate over every unique pair (i, j) where i < j to avoid duplicates.
    # nodes[i+1:] ensures we only look at pairs we haven't seen yet.
    for i, frm in enumerate(nodes):
        for to in nodes[i + 1:]:
            raw = input(f"  {frm} <--> {to}  (weight or Enter to skip): ").strip()

            # Empty input means no edge between this pair — skip it
            if raw == "":
                continue

            try:
                weight = float(raw)

                # Store the edge in both directions so the graph is undirected
                graph[frm][to] = weight
                graph[to][frm] = weight

                print(f"    Added: {frm} <--{raw}--> {to}")
            except ValueError:
                # The user typed something that isn't a number
                print("    Skipped (not a number).")

    return graph


def draw_ascii_graph(graph, nodes, path_edges=None, start=None, end=None, path=None):
    """
    Print an ASCII representation of the graph to the console.

    Each edge is shown once (since the graph is undirected) with a <-> arrow.
    When a shortest path has been found, edges on that path are shown with
    <=> and highlighted in green, and nodes on the path are wrapped in
    square brackets instead of round ones.

    Args:
        graph      (dict): Adjacency dictionary from get_edges().
        nodes      (list): Ordered list of node names.
        path_edges (set):  Set of (from, to) tuples representing path edges.
                           Can be in either direction since the graph is undirected.
        start      (str):  Source node chosen by the user (unused visually now,
                           kept for potential future use).
        end        (str):  Destination node (same as above).
        path       (list): Ordered list of nodes on the shortest path, used to
                           decide which nodes get square bracket labels.
    """
    # Default to an empty set if no path has been calculated yet
    if path_edges is None:
        path_edges = set()

    # Column width for right-aligning the left-hand node label
    col_w = 12

    def node_label(n):
        """
        Return a formatted label for a node.

        Nodes on the shortest path are shown as [node] to make them stand out.
        All other nodes are shown as (node).
        """
        if path and n in path:
            return f"[{n}]"
        else:
            return f"({n})"

    # Print the graph header
    print("\n" + "─" * 52)
    print("  GRAPH")
    print("─" * 52)

    any_edges = False

    # Track which pairs we've already printed so each edge appears only once
    seen = set()

    for frm in nodes:
        for to, weight in graph.get(frm, {}).items():

            # Sort the pair alphabetically so (a, b) and (b, a) map to the same key
            pair = tuple(sorted([frm, to]))
            if pair in seen:
                continue  # Already printed this edge from the other direction
            seen.add(pair)

            any_edges = True

            # Check if this edge is part of the shortest path (either direction)
            on_path = (frm, to) in path_edges or (to, frm) in path_edges

            # Use <=> for path edges, <-> for all others
            arrow = "<=>" if on_path else "<->"

            # Display whole numbers without a decimal point for tidiness
            w_str = int(weight) if weight == int(weight) else weight

            line = f"  {node_label(frm):>{col_w}}  {arrow}  {w_str:<6}  {node_label(to)}"

            # Wrap path edges in ANSI green escape codes (colour-capable terminals only)
            if on_path:
                line = f"\033[92m{line}\033[0m"

            print(line)

    # Inform the user if no edges were defined at all
    if not any_edges:
        print("  (no edges)")

    print("─" * 52)

    # Only show the legend when a path has been calculated
    if path:
        print("  [node] = on shortest path    (node) = not on path    <=> = path edge    <-> = other edge")

    print()


def dijkstra(graph, nodes, start, end):
    """
    Find the shortest path between two nodes using Dijkstra's algorithm.

    How it works:
      - Assign every node a tentative cost of infinity, except the start
        node which gets a cost of 0.
      - Repeatedly pick the unvisited node with the lowest known cost,
        then update the costs of its neighbours if a cheaper route is found
        through the current node.
      - Track each node's 'parent' — the node we came from on the cheapest
        route — so we can reconstruct the path at the end.
      - Repeat until all nodes have been processed.

    Because edges are undirected and stored in both directions, Dijkstra's
    naturally finds the shortest undirected path.

    Args:
        graph (dict): Adjacency dictionary from get_edges().
        nodes (list): Full list of node names.
        start (str):  The node to start from.
        end   (str):  The node to reach.

    Returns:
        tuple(list[str] | None, float | None):
            - The ordered list of node names forming the shortest path,
              or None if no path exists.
            - The total cost of that path, or None if no path exists.
    """
    infinity = float("inf")

    # costs[n] = the cheapest known total cost to reach node n from start
    costs = {n: infinity for n in nodes}
    costs[start] = 0  # It costs nothing to be at the start

    # parents[n] = the node we came from to reach n on the cheapest route
    parents = {n: None for n in nodes}

    # Keep track of nodes whose cheapest path has been finalised
    processed = []

    def find_lowest_cost_node():
        """
        Scan the costs table and return the cheapest unprocessed node.

        Returns None when all reachable nodes have been finalised, which
        signals the main loop to stop.
        """
        lowest = infinity
        result = None
        for n in costs:
            if costs[n] < lowest and n not in processed:
                lowest = costs[n]
                result = n
        return result

    # --- Main Dijkstra loop ---
    node = find_lowest_cost_node()
    while node is not None:
        cost = costs[node]  # Cheapest known cost to reach this node

        # Look at every neighbour of the current node
        for neighbor, weight in graph.get(node, {}).items():
            new_cost = cost + weight  # Cost via the current node

            # If this route is cheaper than what we previously knew, update it
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node  # Remember we came through 'node'

        # Mark this node as done — we won't find a cheaper route to it
        processed.append(node)

        # Move on to the next cheapest unprocessed node
        node = find_lowest_cost_node()

    # If the end node still has infinite cost, it was never reached
    if costs[end] == infinity:
        return None, None

    # --- Reconstruct the path by walking backwards through parents ---
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]

    # We built the path from end to start, so reverse it
    path.reverse()

    return path, costs[end]


# TODO: Implement the Dijkstra's algorithm function
# 1. Initialize the costs dictionary with infinity for each node, set the start node cost to 0.
# 2. Initialize the parents dictionary to keep track of the shortest path.
# 3. Create a list to track processed nodes.
# 4. Create a helper function to find the lowest cost node that hasn't been processed.
# 5. While there are unprocessed nodes:
#    a. Get the node with the lowest cost.
#    b. For each neighbor, calculate the new cost through the current node.
#    c. If it's cheaper, update the cost and set the parent to the current node.
#    d. Mark the current node as processed.
# 6. If the end node cost is infinity, return None for path and cost.
# 7. Reconstruct the path from end to start using parents and return it along with the total cost.


def main():
    """
    Entry point — orchestrates the full user interaction flow:

      1. Collect node names
      2. Collect edge weights between node pairs
      3. Display the graph
      4. Ask the user which two nodes to route between
      5. Run Dijkstra's algorithm
      6. Display the graph again with the shortest path highlighted
      7. Print the path and its total cost
    """
    # Step 1: Build the list of nodes
    nodes = get_nodes()
    if len(nodes) < 2:
        print("Need at least 2 nodes. Exiting.")
        return

    # Step 2: Build the edge connections between those nodes
    graph = get_edges(nodes)

    # Step 3: Show the graph before any path is calculated
    draw_ascii_graph(graph, nodes)

    # Step 4: Ask which nodes to route between
    print(f"Nodes: {', '.join(nodes)}")
    start = input("From: ").strip()
    end   = input("To:   ").strip()

    # Validate that both nodes actually exist in the graph
    if start not in nodes:
        print(f"Error: '{start}' is not in the graph.")
        return
    if end not in nodes:
        print(f"Error: '{end}' is not in the graph.")
        return

    # Step 5: Run Dijkstra's algorithm
    path, total_cost = dijkstra(graph, nodes, start, end)

    # Handle the case where no path exists (disconnected graph)
    if path is None:
        print(f"\nNo path found from '{start}' to '{end}'.")
        return

    # Build a set of directed edge tuples that form the shortest path,
    # used by draw_ascii_graph to highlight the correct edges
    path_edges = {(path[i], path[i + 1]) for i in range(len(path) - 1)}

    # Step 6: Re-display the graph with the path highlighted
    draw_ascii_graph(graph, nodes, path_edges=path_edges, start=start, end=end, path=path)

    # Step 7: Print the result summary
    print(f"  Shortest path: {' -> '.join(path)}")
    # Show whole numbers without a trailing .0 for tidiness
    cost_str = int(total_cost) if total_cost == int(total_cost) else total_cost
    print(f"  Total cost:    {cost_str}\n")


# Only run main() when this file is executed directly,
# not when it is imported as a module by another script
if __name__ == "__main__":
    main()
