# no default definition of linked list
# there is no pre-defined data structure that helps in making link list
# this simply means you need to make the link list all by yourself, by using classes.

# link list is a linear datastructure where we can only access the data in a sequence.
# that means if we are accessing data from start then we need to go from start to end and if we are accessing data from end then we
# need to access data from end to start.

# there is no concept of indexing
# there are nodes in the link list and each node of the link list is having the refenrence to the next node and
# sometimes the previous node as well

# if we try to demonstrate the visual look of link list -
# if the input data is - 1, 2, 3, 4, 5, 6, 7, 8, 9
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
# 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1
# 9 <=> 8 <=> 7 <=> 6 <=>5 <=>4 <=> 3<=> 2 <=>1

# <----------------------Node------------------------->
# [Head]1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9[tail]
# <----------------------Node------------------------->

# a link list has a head, nodes, tail
# NOTE: that head and tail are also nodes

# but `head` is the very first node of the link list OR you can say it is the entry point of the link list
# the `tail` is the very last node of the link list OR you can say it is the exit point of the link list

# [Head]9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1[tail]

# [Head/Tail]9 <=> 8 <=> 7 <=> 6 <=>5 <=>4 <=> 3<=> 2 <=>1[Head/Tail]

# to make a link list in python you need two classes
# 1. Node class
# 2. Actual link list class

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
            output += str(ll.data) + " -> "
            ll = ll.ref  # I moved from one node to next referenced node
        output += "None"
        return output

    def __repr__(self):  # represent the class
        return str(self)


ll = Node(data="Anurag")
ll.ref = Node(data="Chilion")
next_ = ll.ref
next_.ref = Node(data="Abhinav")
next_ = next_.ref
next_.ref=Node(data="Ayushi")

# Anurag -> Chilion -> Abhinav -> Ayushi -> None
print(ll)




