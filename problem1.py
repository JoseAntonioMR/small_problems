'''
You are given the head of a single linked list and you need to write
a function to return the new head of the reversed linked list.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        if not self.head:
            return self.head

        new_next = None
        actual = self.head

        while (actual is not None):
            next_node = actual.next  # save actual next to no lose the node with the change
            actual.next = new_next   # the next node of the current one will be the node on the 'left'
            new_next = actual        # move new_next to actual to asign it in the next iteration
            actual = next_node       # move actual to old next_node to repeat the operation

        # self.head is in the first value, the new self.head is the last new_next value
        self.head = new_next

    def showList(self):
        """Print the list node by node and the next value of the actual node"""
        aux = self.head
        while(aux):
            print aux.value + '  '
            if aux.next:
                print ' NEXT ' + aux.next.value
            else:
                print ' << END of LIST >>'
            aux = aux.next

    def push(self, data):
        """Push data into the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

simpleList = SimpleLinkedList()
simpleList.push('E')
simpleList.push('D')
simpleList.push('C')
simpleList.push('B')
simpleList.push('A')

print "\n\nList -> "
simpleList.showList()
simpleList.reverse()
print "\n\nReversed List -> "
simpleList.showList()
