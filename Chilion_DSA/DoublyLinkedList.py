class Node:
    def __init__(self, data, prev=None, next_=None):
        self.data = data
        self.prev = prev
        self.next = next_


class LinkedList:
    def __init__(self, data=None):
        if data is not None:
            self.head = Node(data)
        else:
            self.head = None

        self.__tail = self.head

    def add_node(self, data):
        node = Node(data)
        if self.head is not None:
            self.__tail.next = node
            # now we need to add prev attribute of new node
            node.prev = self.__tail

            # make newly added node the tail of the linked list
            self.__tail = node

        else:
            self.head = self.__tail = node

    def display(self):
        node = self.head
        while node is not None:
            if node.next is not None:
                print(node.data, end=" <=> ")
            else:
                print(node.data, end=" -> ")
            node = node.next

        print(None)


def main():
    linked_list = LinkedList()
    while True:
        value = input("enter any value or leave blank and press enter to exit entering into linked list: ")
        if value.strip() == "":
            break
        else:
            linked_list.add_node(value)

    linked_list.display()


if __name__ == "__main__":
    main()
