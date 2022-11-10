class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        if self.head is None:
            node = Node(data,self.head,None)
            self.head = node
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None,itr)

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next,itr)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                    break
            itr = itr.next
            count += 1

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self):
        if self.head is None:
            print("the linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print("the linked list is empty")
            return
        last_node = self.get_last_node()
        itr = last_node
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.prev
        print("linked list in reverse:",llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

ll = DoubleLinkedList()
# ll.insert_at_beginning(5)
# ll.insert_at_beginning(89)
# ll.insert_at_beginning(79)
# ll.print_forward()
# last = ll.get_last_node()
# print(last.data)
# ll.print_backward()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print_forward()
ll.print_backward()
ll.insert_at_end("figs")
ll.print_forward()
ll.insert_at(0,"jackfruit")
ll.print_forward()
ll.insert_at(6,"dates")
ll.print_forward()
ll.insert_at(2,"kiwi")
ll.print_forward()




