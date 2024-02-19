class Node:
    # a node in link list is at least one data and on reference to any other node.
    """
    A node where only on data is to be stored
    a reference to the next node is to be stored
    """
    def __init__(self, data=None, ref=None):
        self.data = data
        self.ref = ref

    def __str__(self):
        ll = self
        output = ""
        while ll is not None:
            print(output)
            output += str(ll.data) + " -> "
            ll = ll.ref  # I moved from one node to next referenced node
        output += "None"
        return output

    def __repr__(self):  # represent the class
        return str(self)


class LinkList:
    def __init__(self, head=None):
        self.head = head

    def addNewNode(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
        else:
            node.ref = self.head
            self.head = node
        return self.head

    def deleteStartNode(self):
        if self.head is None:
            return
        self.head = self.head.ref
        return self.head

    def parseList(self):
        lst = []
        node = self.head
        while node is not None:
            lst.insert(0, node.data)
            node = node.ref
        return lst
    # 5 -> 7-> 8-> 3-> 1->None

    def move_to_desired_position(self, position: int):
        count = 1
        node = self.head
        while node.ref is not None and count < position-1:
            node = node.ref
            count += 1

        return node, node.ref

    def appendData(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return self.head
        cur_node = self.head
        while cur_node.ref is not None:
            cur_node = cur_node.ref

        # insert the new node in the ref of cur_node
        cur_node.ref = node
        return self.head

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.ref:
            # till fast is not None and fast.ref is not None
            slow = slow.ref  # it moves one step forward
            fast = fast.ref.ref  # it moves two steps forward

            # now we will check after the above movement, that slow and fast are not equal
            if slow == fast:
                return True  # true means there is a cycle detected in the linked list

        return False


def main():
    arr = [1, 2, 3, 4, 5]
    ll = LinkList()
    for i in arr:
        ll.addNewNode(i)

    print(ll.head)

    ll.deleteStartNode()
    print(ll.head)

    parsed_list = ll.parseList()
    print(parsed_list)

    ll.appendData(0)
    print(ll.head)

    ll.head.ref.ref.ref = ll.head.ref
    if ll.has_cycle():
        print("Cycle detected.")
        return

    # otherwise I will print it.
    print(ll.head)


if __name__ == '__main__':
    main()
