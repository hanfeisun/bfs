class NetworkHasCircleException(Exception):
    pass


def parse_network(path):
    network = {}
    for line in open(path):
        source_node, target_node = line.strip().split(" ")
        source_node_neighbors = network.setdefault(source_node, [])
        source_node_neighbors.append(target_node)
    return network


def check_circle(source, network):
    def helper(current_node, visited):
        if current_node in visited:
            raise NetworkHasCircleException
        visited.append(current_node)
        for neighbor in network.get(current_node, []):
            helper(neighbor, visited)
            visited.pop(len(visited) - 1)
    helper(source, [])



def get_connections(source, target, network):
    queue = []
    connection = {}
    queue.append(source)

    while len(queue) != 0:
        current_node = queue.pop()
        for neighbor in network.get(current_node, []):
            neighbor_parent_connection = connection.setdefault(neighbor, [])
            neighbor_parent_connection.append(current_node)
            queue.append(neighbor)
    return connection


def get_paths(source, target, connections):
    paths = set()
    if target not in connections:
        # No available path
        return

    def helper(current_node, acc):
        if current_node == source:
            one_path = [source]
            one_path.extend(acc)
            paths.add(",".join(one_path))
            return
        acc.insert(0, current_node)
        for prev in connections[current_node]:
            helper(prev, acc)
        acc.pop(0)

    helper(target, [])
    return paths


def bfs(source, target, network):
    check_circle(source, network)
    connections = get_connections(source, target, network)
    paths = get_paths(source, target, connections)
    return paths


def main():
    print(bfs("A", "C", parse_network("./network.txt")))


if __name__ == '__main__':
    main()
