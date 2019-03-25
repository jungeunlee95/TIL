class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        HeadNode = Node("HEAD")
        self.head = HeadNode
        self.tail = HeadNode
        self.NumOfData = 0

    def insert(self, data):
        insertNode = Node(data)
        self.tail.next = insertNode
        self.tail = insertNode
        self.NumOfData += 1

    def delete(self):
        if self.NumOfData == 0:
            print("List is empty!")
            return False
        elif self.NumOfData == 1:
            delete_node = self.head.next
            self.head.next = None
            self.tail = self.head
            self.NumOfData -= 1
            # print("리스트에서", delete_node.data, "데이터를 삭제하였습니다.")
            return delete_node.data
        else:
            delete_node = self.head.next
            self.head.next = self.head.next.next
            self.NumOfData -= 1
            # print("리스트에서 ", delete_node.data, "데이터를 삭제하였습니다.")
            return delete_node.data

    def search(self, data):
        check = self.head
        for i in range(self.NumOfData):
            if check.next.data == data:
                print(data, "데이터는", i + 1, "번째에 있습니다.")
                return None
            check = check.next
        print(data, "데이터는 리스트에 없습니다.")
        return None

    def listNum(self):
        # print("현재 리스트에는", self.NumOfData, "개의 요소가 있습니다.")
        return self.NumOfData

    def printList(self):
        current = self.head
        if self.NumOfData == 0:
            print("List is empty!")
            return None
        print("HEAD::", end='')
        for i in range(self.NumOfData - 1):
            print(current.next.data, "->", end='')
            current = current.next
        print(current.next.data)


list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.printList()
list.delete()
list.printList()
list.listNum()
list.insert(5)
list.insert(6)
list.insert(8)
list.insert(9)
list.insert(10)
list.printList()
list.listNum()
list.search(8)
list.search(7)

