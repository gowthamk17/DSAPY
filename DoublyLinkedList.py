class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)
    
    def insert_list(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Index Out of Bounds!")
        if index == 0:
            self.insert_at_start(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            newHead = self.head.next
            self.head.next = None
            self.head = newHead
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next is not None:
                    itr.next.prev = itr.prev
                itr.next = None
                itr.prev = None
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("LinkedList is empty")
        if self.head.data == data_after:
            self.insert_at(1, data_to_insert)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                if itr.next is not None:
                    itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
        raise Exception("Data does not exist in LinkedList")

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("LinkedList is empty")
        if self.head.data == data:
            newHead = self.head.next
            self.head.next = None
            self.head = newHead
            self.head.prev = None
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                node = itr.next
                if itr.next.next is not None:
                    itr.next.next.prev = itr
                itr.next = itr.next.next
                node.next = None
                node.prev = None
                break
            itr = itr.next


    def print(self):
        if self.head is None:
            print("DoublyLinkedList is empty")
            return
        itr = self.head
        itrStr = ""
        while itr:
            itrStr += str(itr.data) + "<-->"
            itr = itr.next
        itrStr = "None<-->" + itrStr + "None"
        print(itrStr)

    def print_forward(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        itr = self.head
        dllStr = ""
        while itr:
            dllStr += str(itr.data) + "-->"
            itr = itr.next
        dllStr += "None"
        print(dllStr)

    def print_backward(self):
        if self.head is None:
            print("LinkedList is Empty!")
            return
        itr = self.get_to_lastnode()
        dllStr = ""
        while itr:
            dllStr += str(itr.data) + "-->"
            itr = itr.prev
        dllStr += "None"
        print(dllStr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def get_to_lastnode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_start(3)
    dll.insert_at_start(2)
    dll.insert_at_start(1)
    dll.insert_at_start(0)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    # dll.insert_after_value(2,"three")
    # dll.insert_after_value(0,"six")
    # dll.remove_at(5)
    # dll.remove_by_value(5)

    # dll.insert_list(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    dll.print()
    dll.print_forward()
    dll.print_backward()