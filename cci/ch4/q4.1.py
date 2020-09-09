from collections import deque

def has_path(adj_list, source, target):
    if source == None or target ==  None:
        return False

    queue = deque()
    queue.append(source)
    source.visited = True

    while(queue):
        node = queue.popleft()
        if (node.id == target.id):
            return True

        if node.id in adj_list.keys():
            for neighbor in adj_list[node.id]:
                if not neighbor.visited:
                    neighbor.visited = True
                    queue.append(neighbor)

    return False

class Node:

    def __init__(self, id):
        self.id = id
        self.visited = False

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)

    adj_list = {1: [n2, n3], 2: [n4], 3: [n7], 4: [n5, n6], 7: [n2, n4, n8], 9: [n10], 10: [n6]}

    print(has_path(adj_list, n1, n10))


