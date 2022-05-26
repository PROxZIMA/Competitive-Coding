class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end = ' ')
            curr = curr.next

def main():
    llist = LinkedList()
    for _ in range(int(input())):
        data = int(input())
        llist.insert(data)

    llist.display()

if __name__ == "__main__":
    main()

