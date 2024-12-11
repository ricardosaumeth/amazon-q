class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
          return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
          self.head = None
          self.tail = None
        temp.next = None  
        return temp 

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): 
            temp = temp.next
        return temp         


my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(30)

# print("Before prepend():")
# print("----------------")
# print("Head:", my_linked_list.head.value)
# print("Tail:", my_linked_list.tail.value)
# print("Length:", my_linked_list.length, "\n")
# print("Linked List:")
# my_linked_list.print_list()


#my_linked_list.prepend(1)


# print("\n\nAfter prepend():")
# print("---------------")
# print("Head:", my_linked_list.head.value)
# print("Tail:", my_linked_list.tail.value)
# print("Length:", my_linked_list.length, "\n")
# print("Linked List:")
# my_linked_list.print_list()
# print('\n')
# print(f"{my_linked_list.pop_first().value} *** pop_firts" )
my_linked_list.print_list()

print('//////////////////////////')
print(my_linked_list.get(2).value)