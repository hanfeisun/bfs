import re
class NetworkHasCircleException(Exception):
    pass

DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def parse_network(path):
    network = {}
    with open(path) as f:
        for line in f:
            source_node, target_node = re.split(r" |\t", line.strip())
            source_node_neighbors = network.setdefault(source_node, [])
            source_node_neighbors.append(target_node)
    return network


def check_circle(source, network):

    def helper(current_node, visited):
        if current_node in visited:
            print("Found a circle %s -> %s" % (",".join(visited), current_node))
            source_neighbors = network[visited[-1]]
            source_neighbors.remove(current_node)
            debug("remove ", current_node, " from ", visited[-1])
            debug(network)
            return False
        else:
            for neighbor in network.get(current_node, [])[:]:
                debug("from ", current_node, " to ", neighbor, " visited ", visited)
                visited.append(current_node)
                helper(neighbor, visited)
                visited.pop(len(visited) - 1)
            return True

    helper(source, [])
    return network



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
    print("Check circle finished")
    connections = get_connections(source, target, network)
    print("Finish get connections")
    paths = get_paths(source, target, connections)
    return paths


def main():
    print(bfs("Myc", "Ptma", parse_network("./ESCAPE_Net.txt")))


if __name__ == '__main__':
    main()
